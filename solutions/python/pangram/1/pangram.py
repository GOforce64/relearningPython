def is_pangram(sentence):
    phraze = list("thequickbrownfoxjumpsoverthelazydog")
    checked_characters = []
    unique_character_count = 0
    for character in sentence:
        character = character.lower()
        if (character in phraze) and (character not in checked_characters):
            unique_character_count = unique_character_count + 1
            checked_characters.append(character)
    if unique_character_count == 26:
        return True
    else:
        return False
            
