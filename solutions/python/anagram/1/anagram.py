def find_anagrams(word, candidates):
    word = word.lower()
    sorted_word = sorted(word)
    anagrams = []
    
    for candidate in candidates:
        candidate_lower = candidate.lower()

        if candidate_lower == word:
            continue
            
        if sorted(candidate_lower) == sorted_word:
            anagrams.append(candidate)
    return anagrams

        
