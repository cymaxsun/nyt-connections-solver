import json
import os

def classify_group_refined(group_name: str, members: list) -> str:
    group_lower = group_name.lower().strip()
    
    # 1. PHRASE_COMPLETION
    if "___" in group_lower or " _ " in group_lower or "blank" in group_lower:
        return "PHRASE_COMPLETION"
    
    phrase_keywords = [
        "words after", "words before", "followed by", "preceded by", 
        "word after", "word before", "can follow", "can precede", 
        "preceded", "followed", "words that can follow", "words that can precede"
    ]
    if any(k in group_lower for k in phrase_keywords):
        return "PHRASE_COMPLETION"

    # 2. WORDPLAY
    wordplay_keywords = [
        "anagram", "palindrome", "homophone", "sounds like", "spelling", 
        "pronounced", "spoonerism", "pun", "rhymes with", "rhyming", 
        "wordplay", "pig latin", "inside", "inserted", "letter swap", 
        "added letter", "letter sounds", "words that sound like", 
        "homophones of", "sound like", "spelled backward", "backwards", 
        "backward", "swapped", "rearranged", "hidden in", "spelling of", 
        "pronunciation", "sound alike", "homophonic", "minus", "removed", 
        "dropped", "subtracted", "added", "substitution", 
        "changed", "homographs", "homographic", "same sound"
    ]
    if any(k in group_lower for k in wordplay_keywords):
        # Exclude plain synonym groups like "replacement" or "changed"
        if group_lower not in ["replacement", "substitution", "changed"]:
            return "WORDPLAY"
    
    clean_members = [m.strip().upper() for m in members]
    if len(clean_members) >= 3 and all(w == w[::-1] for w in clean_members if len(w) > 1):
        return "WORDPLAY"

    # 3. MORPHOLOGY
    morph_keywords = [
        "prefix", "suffix", "starts with", "ends with", "beginning with",
        "ending in", "prefixed by", "suffixed by", "starting with", "ending with",
        "first letter", "last letter", "middle letter", "letter count", "syllable",
        "double letter", "consonant", "vowel", "parts of speech", "compound", 
        "shares prefix", "shares suffix"
    ]
    if any(k in group_lower for k in morph_keywords):
        return "MORPHOLOGY"
        
    # Shared prefix/suffix check of length >= 3
    if len(clean_members) >= 3:
        # check shared prefix
        common_prefix = os.path.commonprefix(clean_members)
        if len(common_prefix) >= 3:
            return "MORPHOLOGY"
        # check shared suffix
        reversed_members = [w[::-1] for w in clean_members]
        common_suffix = os.path.commonprefix(reversed_members)[::-1]
        if len(common_suffix) >= 3:
            return "MORPHOLOGY"

    # 4. TRIVIA_ENCYCLOPEDIC
    # Removed generic words like "state" or "capital" which cause false positives (e.g. "FLUSTERED STATE")
    # Added specific state/capital keywords instead.
    trivia_keywords = [
        "teams", "brands", "characters", "shows", "movies", "songs", "actors",
        "musicals", "magazines", "countries", "cities", "places", "franchises",
        "companies", "members of", "winners", "awards", "history", "presidents",
        "games", "logos", "symbols", "landmarks", "nobel", "olympics",
        "zodiac", "constellations", "currencies", "elements", "album", "band",
        "singer", "artist", "author", "book", "play", "novel", "poet", "deities",
        "gods", "mythology", "constellation", "currency", "island", 
        "monopoly", "simpsons", "disney", "nba", "nfl", "mlb", "nhl",
        "tv show", "television", "radio", "newspaper", "website", "app", "game"
    ]
    
    state_keywords = ["us state", "u.s. state", "states bordering", "states of", "southern state", "western state", "state names"]
    capital_keywords = ["capitals", "capital of", "capital cities", "world capitals"]
    
    is_trivia = any(k in group_lower for k in trivia_keywords)
    is_state_trivia = any(k in group_lower for k in state_keywords)
    is_capital_trivia = any(k in group_lower for k in capital_keywords)
    
    if is_trivia or is_state_trivia or is_capital_trivia:
        return "TRIVIA_ENCYCLOPEDIC"

    # 5. SYNONYM (default)
    return "SYNONYM"

def main():
    data_path = "data/connections.json"
    if not os.path.exists(data_path):
        print(f"Error: Dataset {data_path} not found.")
        return
        
    with open(data_path, "r") as f:
        data = json.load(f)
        
    changes = []
    corrected_data = []
    
    for puzzle in data:
        new_answers = []
        for answer in puzzle["answers"]:
            old_type = answer.get("relation_type", "SYNONYM")
            new_type = classify_group_refined(answer["group"], answer["members"])
            
            if old_type != new_type:
                changes.append((answer["group"], answer["members"], old_type, new_type))
                
            new_ans = {
                "level": answer["level"],
                "group": answer["group"],
                "relation_type": new_type,
                "members": answer["members"]
            }
            new_answers.append(new_ans)
            
        new_puzzle = {
            "id": puzzle["id"],
            "date": puzzle.get("date", ""),
            "answers": new_answers
        }
        corrected_data.append(new_puzzle)
        
    print(f"Total label corrections made: {len(changes)}")
    if len(changes) > 0:
        print("\nSample Label Corrections:")
        for group, members, old, new in changes[:30]:
            print(f" - Group: {group:<40} | Old: {old:<20} -> New: {new}")
            
    # Save the updated json in-place
    with open(data_path, "w") as f:
        json.dump(corrected_data, f, indent=4)
    print(f"\nSuccessfully updated {data_path} in-place with corrected 'relation_type' fields.")

if __name__ == "__main__":
    main()
