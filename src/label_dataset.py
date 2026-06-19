import json
import os
import re

def classify_group(group_name: str, members: list) -> str:
    group_lower = group_name.lower().strip()
    
    # 1. PHRASE_COMPLETION
    # Standard blank fills, or phrases starting/ending with words
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
    # Active letter manipulation, anagrams, homophones, phonetic similarity, spelling subtraction/addition
    wordplay_keywords = [
        "anagram", "palindrome", "homophone", "sounds like", "spelling", 
        "pronounced", "spoonerism", "pun", "rhymes with", "rhyming", 
        "wordplay", "pig latin", "inside", "inserted", "letter swap", 
        "added letter", "letter sounds", "words that sound like", 
        "homophones of", "sound like", "spelled backward", "backwards", 
        "backward", "swapped", "rearranged", "hidden in", "spelling of", 
        "pronunciation", "sound alike", "homophonic", "minus", "removed", 
        "dropped", "subtracted", "added", "replacement", "substitution", 
        "changed", "homographs", "homographic"
    ]
    if any(k in group_lower for k in wordplay_keywords):
        return "WORDPLAY"
    
    # Palindrome member check
    clean_members = [m.strip().upper() for m in members]
    if len(clean_members) >= 3 and all(w == w[::-1] for w in clean_members if len(w) > 1):
        return "WORDPLAY"

    # 3. MORPHOLOGY
    # Structural properties of the words themselves (prefixes, suffixes, double letters, etc.)
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
    # Proper nouns, brands, pop culture lists, specific trivia domains
    trivia_keywords = [
        "teams", "brands", "characters", "shows", "movies", "songs", "actors",
        "musicals", "magazines", "countries", "cities", "places", "franchises",
        "companies", "members of", "winners", "awards", "history", "presidents",
        "games", "logos", "symbols", "landmarks", "capitals", "nobel", "olympics",
        "zodiac", "constellations", "currencies", "elements", "album", "band",
        "singer", "artist", "author", "book", "play", "novel", "poet", "deities",
        "gods", "mythology", "constellation", "currency", "island", "state",
        "capital", "monopoly", "simpsons", "disney", "nba", "nfl", "mlb", "nhl",
        "tv show", "television", "radio", "newspaper", "website", "app", "game"
    ]
    if any(k in group_lower for k in trivia_keywords):
        return "TRIVIA_ENCYCLOPEDIC"

    # 5. SYNONYM (default)
    # Semantic similarity or synonyms
    return "SYNONYM"

def main():
    data_path = "data/connections.json"
    if not os.path.exists(data_path):
        print(f"Error: Dataset {data_path} not found.")
        return
        
    with open(data_path, "r") as f:
        data = json.load(f)
        
    stats = {
        "SYNONYM": 0,
        "WORDPLAY": 0,
        "PHRASE_COMPLETION": 0,
        "TRIVIA_ENCYCLOPEDIC": 0,
        "MORPHOLOGY": 0
    }
    
    labeled_data = []
    sample_outputs = []
    
    for puzzle in data:
        new_answers = []
        for answer in puzzle["answers"]:
            rel_type = classify_group(answer["group"], answer["members"])
            stats[rel_type] += 1
            
            new_ans = {
                "level": answer["level"],
                "group": answer["group"],
                "relation_type": rel_type,
                "members": answer["members"]
            }
            new_answers.append(new_ans)
            
            if len(sample_outputs) < 30:
                sample_outputs.append((answer["group"], answer["members"], rel_type))
                
        new_puzzle = {
            "id": puzzle["id"],
            "date": puzzle.get("date", ""),
            "answers": new_answers
        }
        labeled_data.append(new_puzzle)
        
    print("Trial Run / Classification Sample (using 5 Archetypes):")
    for group, members, rtype in sample_outputs:
        print(f" - Group: {group:<40} | Members: {str(members):<40} -> Type: {rtype}")
        
    print("\nClassification Statistics:")
    total = sum(stats.values())
    for k in ["SYNONYM", "WORDPLAY", "PHRASE_COMPLETION", "TRIVIA_ENCYCLOPEDIC", "MORPHOLOGY"]:
        v = stats[k]
        print(f" - {k:<25}: {v:>5} ({v/total:.1%})")
    print(f"Total labeled groups: {total}")
    
    # Save the updated json in-place
    with open(data_path, "w") as f:
        json.dump(labeled_data, f, indent=4)
    print(f"\nSuccessfully updated {data_path} in-place with 'relation_type' fields.")

if __name__ == "__main__":
    main()
