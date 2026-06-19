import os
import json
import time
import requests
import argparse
from typing import List, Dict, Any

# Define the 5 relation types
RELATION_TYPES = [
    "SYNONYM",
    "WORDPLAY",
    "PHRASE_COMPLETION",
    "TRIVIA_ENCYCLOPEDIC",
    "MORPHOLOGY"
]

def load_env(env_path: str = ".env") -> Dict[str, str]:
    if not os.path.exists(env_path):
        return {}
    env = {}
    with open(env_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("=", 1)
            if len(parts) == 2:
                key = parts[0].strip()
                val = parts[1].strip().strip('"').strip("'")
                env[key] = val
    return env

def make_cache_key(group: str, members: List[str]) -> str:
    sorted_members = sorted([m.strip().upper() for m in members])
    return f"{group.strip().upper()}|||{','.join(sorted_members)}"

def get_deepseek_labels(batch: List[Dict[str, Any]], api_key: str) -> List[str]:
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Format batch items for prompt
    items_str = []
    for item in batch:
        items_str.append(f"ID: {item['id']} | Group: {item['group']} | Words: {', '.join(item['members'])}")
    batch_text = "\n".join(items_str)

    system_prompt = (
        "You are an expert at analyzing word puzzles, specifically the NYT Connections game.\n"
        "Your task is to classify the relation type of the given group of 4 words into exactly one of these 5 categories:\n\n"
        "1. SYNONYM: The words are direct synonyms, close semantic relations, or share a common definition/category (e.g., 'WET WEATHER': HAIL, RAIN, SLEET, SNOW).\n"
        "2. WORDPLAY: Letter/sound manipulation, anagrams, homophones, puns, letter additions/subtractions, spelling reversals (e.g., 'LETTER HOMOPHONES': ARE, QUEUE, SEA, WHY).\n"
        "3. PHRASE_COMPLETION: Words that complete a common phrase, compound word, or expression, often using blanks or prefix/suffix words (e.g., 'WORDS WITH \"FALL\"': BACK, OUT, DOWN, UP; '___ OF CARDS': DECK, HOUSE, PACK, SUIT).\n"
        "4. TRIVIA_ENCYCLOPEDIC: Knowledge-based lists, proper nouns, brands, pop culture references, names of teams, shows, characters, elements, or specialized trivia (e.g., 'NBA TEAMS': BUCKS, HEAT, JAZZ, NETS).\n"
        "5. MORPHOLOGY: Structural properties of the words themselves, such as starting/ending with certain letters, sharing prefixes/suffixes, letter counts, double letters, parts of speech (e.g., 'WORDS STARTING WITH COLORS': BROWNING, GREENERY, ORANGEADE, REDHEAD).\n\n"
        "You must output a JSON object containing a 'classifications' array. Each item in the array must have 'id' (integer matching the input) and 'relation_type' (one of the 5 uppercase strings above)."
    )

    user_prompt = (
        f"Classify the following groups of words:\n\n{batch_text}\n\n"
        "Respond with a valid JSON object matching the requested schema."
    )

    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.0,
        "response_format": {"type": "json_object"}
    }

    # Retry logic
    for attempt in range(3):
        try:
            response = requests.post(url, headers=headers, json=data, timeout=30)
            if response.status_code == 200:
                result = response.json()
                content = result['choices'][0]['message']['content']
                parsed = json.loads(content)
                
                # Build mapping of id -> relation_type
                label_map = {}
                for item in parsed.get("classifications", []):
                    label_map[item["id"]] = item["relation_type"].strip().upper()
                
                # Check if all IDs in batch are covered
                labels = []
                for item in batch:
                    rtype = label_map.get(item["id"])
                    if rtype not in RELATION_TYPES:
                        rtype = "SYNONYM"  # Fallback
                    labels.append(rtype)
                return labels
            else:
                print(f"API Error (HTTP {response.status_code}): {response.text}")
        except Exception as e:
            print(f"Request exception on attempt {attempt + 1}: {e}")
        
        time.sleep(2 ** attempt)

    raise RuntimeError("Failed to query DeepSeek API after 3 attempts.")

def main():
    parser = argparse.ArgumentParser(description="Label Connections categories using DeepSeek API.")
    parser.add_argument("--limit-batches", type=int, default=0, help="Limit number of batches to run (0 for no limit).")
    parser.add_argument("--batch-size", type=int, default=30, help="Batch size of groups per request.")
    args = parser.parse_args()

    env = load_env()
    api_key = env.get("DEEPSEEK_API_KEY")
    if not api_key or api_key == "your_api_key_here":
        print("Error: Please set DEEPSEEK_API_KEY in the .env file before running.")
        return

    data_path = "data/connections.json"
    cache_path = "data/llm_labels_cache.json"

    if not os.path.exists(data_path):
        print(f"Error: Dataset {data_path} not found.")
        return

    with open(data_path, "r") as f:
        puzzles = json.load(f)

    # Load existing cache
    if os.path.exists(cache_path):
        with open(cache_path, "r") as f:
            cache = json.load(f)
    else:
        cache = {}

    # Extract all unique categories to label
    unique_groups = {}
    for puzzle in puzzles:
        for answer in puzzle["answers"]:
            key = make_cache_key(answer["group"], answer["members"])
            if key not in cache:
                unique_groups[key] = {
                    "group": answer["group"],
                    "members": answer["members"]
                }

    print(f"Total unique groups in dataset: {len(unique_groups) + len(cache)}")
    print(f"Cached classifications: {len(cache)}")
    print(f"Remaining groups to label: {len(unique_groups)}")

    if len(unique_groups) > 0:
        # Convert unique groups dictionary to a list for batching
        to_label = [{"key": k, "group": v["group"], "members": v["members"]} for k, v in unique_groups.items()]
        
        batches_run = 0
        for i in range(0, len(to_label), args.batch_size):
            if args.limit_batches > 0 and batches_run >= args.limit_batches:
                print(f"Stopping after hitting the limit of {args.limit_batches} batch(es).")
                break

            batch_slice = to_label[i:i+args.batch_size]
            # Attach a temporary serial ID for tracking in LLM response
            batch_payload = []
            for idx, item in enumerate(batch_slice):
                batch_payload.append({
                    "id": idx,
                    "group": item["group"],
                    "members": item["members"]
                })

            print(f"Labeling batch {batches_run + 1}/{(len(to_label)-1)//args.batch_size + 1} ({len(batch_slice)} items)...")
            try:
                labels = get_deepseek_labels(batch_payload, api_key)
                for item, label in zip(batch_slice, labels):
                    cache[item["key"]] = label
                
                # Save cache after each successful batch
                with open(cache_path, "w") as f:
                    json.dump(cache, f, indent=4)
                
                batches_run += 1
                time.sleep(0.5)  # Brief rate-limit buffer
            except Exception as e:
                print(f"Error during labeling: {e}")
                print("Cache saved up to current progress. Fix the issue and resume.")
                return

    # Update the connections.json with labels from cache
    updated_count = 0
    for puzzle in puzzles:
        for answer in puzzle["answers"]:
            key = make_cache_key(answer["group"], answer["members"])
            if key in cache:
                answer["relation_type"] = cache[key]
                updated_count += 1

    with open(data_path, "w") as f:
        json.dump(puzzles, f, indent=4)

    print(f"\nLabeling completed!")
    print(f"Updated {updated_count} groups in {data_path}.")

    # Print distribution stats
    stats = {}
    for val in cache.values():
        stats[val] = stats.get(val, 0) + 1
    
    print("\nLLM Relation Type Distribution:")
    total = sum(stats.values())
    for k in RELATION_TYPES:
        v = stats.get(k, 0)
        print(f" - {k:<25}: {v:>5} ({v/total:.1%})")

if __name__ == "__main__":
    main()
