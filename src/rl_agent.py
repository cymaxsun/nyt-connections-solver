import random
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from collections import deque
from typing import List, Dict, Tuple, Any, Optional
from src.env import ConnectionsEnv
from src.dataset import ConnectionsPuzzle
from src.graph import ConnectionsGraph
from src.gcn import ConnectionsGCN
from src.features import FeatureExtractor
from src.candidates import PartitionGroupCandidate, build_partition_candidates, partition_groups_for_actions

CANDIDATE_FEATURE_DIM = 22

class QNetwork(nn.Module):
    def __init__(self, state_dim: int = 33, candidate_dim: int = CANDIDATE_FEATURE_DIM, hidden_dim: int = 64):
        super().__init__()
        # Takes state embedding + candidate feature representation
        self.net = nn.Sequential(
            nn.Linear(state_dim + candidate_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU(),
            nn.Linear(hidden_dim // 2, 1) # Outputs Q-value for this specific action/candidate
        )

    def forward(self, state: torch.Tensor, candidate_feats: torch.Tensor) -> torch.Tensor:
        """
        Args:
            state: Tensor of shape (batch_size, state_dim) or (state_dim,)
            candidate_feats: Tensor of shape (batch_size, num_candidates, candidate_dim) 
                             or (num_candidates, candidate_dim)
        Returns:
            Q-values: Shape (batch_size, num_candidates) or (num_candidates,)
        """
        # If single item (no batch dimension)
        if len(state.shape) == 1:
            num_cand = candidate_feats.shape[0]
            # Repeat state for each candidate
            state_rep = state.unsqueeze(0).expand(num_cand, -1)
            # Concatenate
            inp = torch.cat([state_rep, candidate_feats], dim=-1)
            return self.net(inp).squeeze(-1) # (num_candidates,)
        else:
            # Batched item
            batch_size = state.shape[0]
            num_cand = candidate_feats.shape[1]
            state_rep = state.unsqueeze(1).expand(-1, num_cand, -1) # (batch_size, num_cand, state_dim)
            inp = torch.cat([state_rep, candidate_feats], dim=-1) # (batch_size, num_cand, state_dim + candidate_dim)
            return self.net(inp).squeeze(-1) # (batch_size, num_cand)

class ReplayBuffer:
    def __init__(self, capacity: int = 10000):
        self.buffer = deque(maxlen=capacity)

    def push(self, state: np.ndarray, cand_feats: np.ndarray, action_idx: int, reward: float, next_state: np.ndarray, next_cand_feats: np.ndarray, done: bool):
        self.buffer.append((state, cand_feats, action_idx, reward, next_state, next_cand_feats, done))

    def sample(self, batch_size: int) -> List[Tuple]:
        return random.sample(self.buffer, min(batch_size, len(self.buffer)))

    def __len__(self):
        return len(self.buffer)

class DQNAgent:
    def __init__(
        self, 
        state_dim: int = 33, 
        candidate_dim: int = CANDIDATE_FEATURE_DIM, 
        lr: float = 1e-3, 
        gamma: float = 0.95,
        epsilon_start: float = 1.0,
        epsilon_end: float = 0.05,
        epsilon_decay: float = 0.995,
        device: str = "cpu"
    ):
        self.device = device
        self.gamma = gamma
        self.epsilon = epsilon_start
        self.epsilon_end = epsilon_end
        self.epsilon_decay = epsilon_decay
        
        self.q_net = QNetwork(state_dim, candidate_dim).to(device)
        self.target_net = QNetwork(state_dim, candidate_dim).to(device)
        self.target_net.load_state_dict(self.q_net.state_dict())
        
        self.optimizer = torch.optim.Adam(self.q_net.parameters(), lr=lr)
        self.buffer = ReplayBuffer()

    def update_target_network(self):
        self.target_net.load_state_dict(self.q_net.state_dict())

    def get_candidate_features(
        self, 
        candidates: List[PartitionGroupCandidate], 
        node_embeddings: torch.Tensor, 
        obs: np.ndarray
    ) -> Tuple[List[Tuple[int, ...]], torch.Tensor]:
        """
        Builds the candidate feature vectors.
        For each candidate group of 4 indices:
            - GCN Cohesion Score (1-dim)
            - Mean of the 4 GCN node embeddings (out_features-dim)
            - Mean submission history count of the 4 nodes (1-dim)
            - Partition context: score, weakest group score, rank, remaining quality (4-dim)
        """
        # Extract submission history from observation vector
        # State representation: active_mask (16) + mistakes_left (1) + submission_history (16)
        history = obs[17:]
        
        cand_list = []
        feats_list = []
        
        active_mask = obs[:16]
        
        for candidate in candidates:
            comb = candidate.group
            # Check if all 4 indices in combination are active
            if all(active_mask[i] == 1.0 for i in comb):
                # Valid candidate!
                cand_list.append(comb)
                
                # Fetch node embeddings
                embeddings = node_embeddings[list(comb)] # (4, out_features)
                mean_embedding = embeddings.mean(dim=0)
                
                # Fetch mean submission history
                mean_hist = history[list(comb)].mean()
                
                # Build feature tensor
                feat_tensor = torch.cat([
                    torch.tensor([candidate.group_score], dtype=torch.float32, device=node_embeddings.device),
                    mean_embedding,
                    torch.tensor([
                        mean_hist,
                        candidate.partition_score,
                        candidate.partition_min_score,
                        candidate.group_rank / 3.0,
                        candidate.remaining_mean_score,
                    ], dtype=torch.float32, device=node_embeddings.device)
                ])
                feats_list.append(feat_tensor)
                
                # Keep top 20 valid active candidates
                if len(cand_list) == 20:
                    break
                    
        # Fallback if no valid candidates found (should be rare/impossible unless board solved)
        if not cand_list:
            # Make a dummy candidate from remaining active indices
            active_indices = [i for i, active in enumerate(active_mask) if active == 1.0]
            if len(active_indices) >= 4:
                dummy_comb = tuple(active_indices[:4])
                cand_list.append(dummy_comb)
                mean_embedding = node_embeddings[list(dummy_comb)].mean(dim=0)
                mean_hist = history[list(dummy_comb)].mean()
                feat_tensor = torch.cat([
                    torch.tensor([0.0], dtype=torch.float32, device=node_embeddings.device),
                    mean_embedding,
                    torch.tensor([
                        mean_hist,
                        0.0,
                        0.0,
                        0.0,
                        0.0,
                    ], dtype=torch.float32, device=node_embeddings.device)
                ])
                feats_list.append(feat_tensor)
            else:
                # Board is solved, dummy values
                dummy_comb = (0, 1, 2, 3)
                cand_list.append(dummy_comb)
                feat_tensor = torch.zeros(
                    CANDIDATE_FEATURE_DIM,
                    dtype=torch.float32,
                    device=node_embeddings.device,
                )
                feats_list.append(feat_tensor)
                
        return cand_list, torch.stack(feats_list)

    def get_partition_action_candidates(
        self,
        candidates: List[Tuple[Tuple[int, ...], float]],
        obs: np.ndarray,
        rejected_groups: set,
    ) -> List[PartitionGroupCandidate]:
        """Build deduplicated one-group actions from whole-board candidate partitions."""
        active_mask = obs[:16]
        partitions = build_partition_candidates(
            candidates,
            active_mask,
            rejected_groups=rejected_groups,
        )
        return partition_groups_for_actions(
            partitions,
            candidates,
            active_mask,
            rejected_groups=rejected_groups,
        )

    def select_action(self, obs: np.ndarray, cand_list: List[Tuple[int, ...]], cand_feats: torch.Tensor) -> int:
        """Select action using epsilon-greedy strategy."""
        if random.random() < self.epsilon:
            return random.randint(0, len(cand_list) - 1)
            
        with torch.no_grad():
            state_t = torch.tensor(obs, dtype=torch.float32, device=self.device)
            # Shape of Q-values: (num_candidates,)
            q_vals = self.q_net(state_t, cand_feats)
            return int(torch.argmax(q_vals).item())

    def train_step(self, batch_size: int) -> Optional[float]:
        """Runs a single training update step, vectorized across the batch to avoid loop updates."""
        if len(self.buffer) < batch_size:
            return None
            
        samples = self.buffer.sample(batch_size)
        
        state_list = [s[0] for s in samples]
        cand_feats_list = [torch.as_tensor(s[1], dtype=torch.float32, device=self.device) for s in samples]
        action_idx_list = [s[2] for s in samples]
        reward_list = [s[3] for s in samples]
        next_state_list = [s[4] for s in samples]
        next_cand_feats_list = [torch.as_tensor(s[5], dtype=torch.float32, device=self.device) for s in samples]
        done_list = [float(s[6]) for s in samples]
        
        state_t = torch.tensor(np.stack(state_list), dtype=torch.float32, device=self.device)
        next_state_t = torch.tensor(np.stack(next_state_list), dtype=torch.float32, device=self.device)
        reward_t = torch.tensor(reward_list, dtype=torch.float32, device=self.device)
        action_idx_t = torch.tensor(action_idx_list, dtype=torch.long, device=self.device)
        done_t = torch.tensor(done_list, dtype=torch.float32, device=self.device)
        
        max_num_cand = max(t.shape[0] for t in cand_feats_list)
        max_num_next_cand = max(t.shape[0] for t in next_cand_feats_list)
        
        padded_cand_feats = torch.zeros(batch_size, max_num_cand, CANDIDATE_FEATURE_DIM, dtype=torch.float32, device=self.device)
        padded_next_cand_feats = torch.zeros(batch_size, max_num_next_cand, CANDIDATE_FEATURE_DIM, dtype=torch.float32, device=self.device)
        next_mask = torch.zeros(batch_size, max_num_next_cand, dtype=torch.bool, device=self.device)
        
        for i in range(batch_size):
            cand_len = cand_feats_list[i].shape[0]
            padded_cand_feats[i, :cand_len, :] = cand_feats_list[i]
            
            next_cand_len = next_cand_feats_list[i].shape[0]
            padded_next_cand_feats[i, :next_cand_len, :] = next_cand_feats_list[i]
            next_mask[i, :next_cand_len] = True
            
        self.optimizer.zero_grad()
        q_vals = self.q_net(state_t, padded_cand_feats) # (batch_size, max_num_cand)
        q_val = q_vals[torch.arange(batch_size), action_idx_t] # (batch_size,)
        
        with torch.no_grad():
            next_q_vals = self.target_net(next_state_t, padded_next_cand_feats) # (batch_size, max_num_next_cand)
            next_q_vals_masked = next_q_vals.masked_fill(~next_mask, -1e9)
            max_next_q = torch.max(next_q_vals_masked, dim=-1)[0]
            target = reward_t + self.gamma * max_next_q * (1.0 - done_t)
            
        loss = F.mse_loss(q_val, target)
        loss.backward()
        self.optimizer.step()
        
        # Decay epsilon
        self.epsilon = max(self.epsilon_end, self.epsilon * self.epsilon_decay)
        
        return loss.item()

def train_rl_episodes(
    agent: DQNAgent,
    gcn_model: ConnectionsGCN,
    puzzles: list,
    extractor: FeatureExtractor,
    episodes: int,
    batch_size: int = 16,
    target_update_frequency: int = 5
) -> List[Dict[str, Any]]:
    """Runs RL training loops with feedback-adaptive graph refinement."""
    gcn_model.eval()
    stats = []
    
    for ep in range(episodes):
        # Pick a random training puzzle
        puzzle = random.choice(puzzles)
        
        # Build the graph — clone edge features so mutations don't leak across episodes
        with torch.no_grad():
            if isinstance(puzzle, dict):
                graph = ConnectionsGraph(
                    puzzle["words"], 
                    device=agent.device, 
                    node_features=puzzle["node_features"], 
                    edge_features=puzzle["edge_features"]
                )
            else:
                graph = ConnectionsGraph(puzzle.words, extractor, device=agent.device)
            
            # Clone edge features so feedback mutations are episode-local
            graph.edge_features = graph.edge_features.clone()
            
        # Initialize environment
        env = ConnectionsEnv(puzzle)
        obs, info = env.reset()
        
        done = False
        episode_reward = 0.0
        steps = 0
        
        # Run GCN initially to get starting state embeddings and candidate features
        with torch.no_grad():
            node_embeddings, edge_probs, _, group_relation_logits = gcn_model(
                graph.node_features,
                graph.get_multi_relational_adjacency(),
                graph.edge_features,
                return_group_logits=True,
            )
            candidates = graph.filter_candidates(
                gcn_model.get_candidate_subgraphs(edge_probs, group_relation_logits)
            )
            action_candidates = agent.get_partition_action_candidates(
                candidates, obs, graph.rejected_groups
            )
        cand_list, cand_feats = agent.get_candidate_features(action_candidates, node_embeddings, obs)
        
        while not done:
            # Select action index
            action_idx = agent.select_action(obs, cand_list, cand_feats)
            action_indices = cand_list[action_idx]
            
            # Step in environment
            next_obs, reward, done, _, step_info = env.step(action_indices)
            episode_reward += reward
            
            # Update graph edges based on feedback
            feedback = step_info.get("feedback", "")
            graph.update_edges_from_feedback(action_indices, feedback)
            
            # Run GCN once to compute next-state candidate features (with updated graph)
            with torch.no_grad():
                next_node_embeddings, next_edge_probs, _, next_group_relation_logits = gcn_model(
                    graph.node_features,
                    graph.get_multi_relational_adjacency(),
                    graph.edge_features,
                    return_group_logits=True,
                )
                next_candidates = graph.filter_candidates(
                    gcn_model.get_candidate_subgraphs(next_edge_probs, next_group_relation_logits)
                )
                next_action_candidates = agent.get_partition_action_candidates(
                    next_candidates, next_obs, graph.rejected_groups
                )
            
            next_cand_list, next_cand_feats = agent.get_candidate_features(
                next_action_candidates, next_node_embeddings, next_obs
            )
            
            # Store in buffer
            agent.buffer.push(
                obs, 
                cand_feats.cpu().numpy(), 
                action_idx, 
                reward, 
                next_obs, 
                next_cand_feats.cpu().numpy(), 
                done
            )
            
            # Move state (carry over next state candidate features to next step)
            obs = next_obs
            cand_list = next_cand_list
            cand_feats = next_cand_feats
            steps += 1
            
            # Run optimizer training step
            loss = agent.train_step(batch_size)
            
        # Print stats
        won = step_info.get("win", False)
        stats.append({
            "episode": ep,
            "puzzle_id": puzzle["id"] if isinstance(puzzle, dict) else puzzle.id,
            "reward": episode_reward,
            "steps": steps,
            "won": won,
            "mistakes_left": step_info.get("mistakes_left", 0)
        })
        
        # Update target network
        if ep % target_update_frequency == 0:
            agent.update_target_network()
            
    return stats
