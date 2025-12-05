def is_isogram(string):
    """
    Function takes in a word string and determines if it is an isogram.
    
    param: string - the word to be checked.
    return: boolean - if it is an isogram.
    """
    string = string.lower()
    checkedChars = []
    for char in string:
        if char.isalpha() and char in checkedChars:
            return False
        if char.isalpha():
            checkedChars.append(char)
    return True
    # We add every alphabetic character to a list and check every new character with the list.