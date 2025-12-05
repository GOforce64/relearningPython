def rotate(text, key):
    text = list(text)
    for index, char in enumerate(text):
        if (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122):
            isCapital = False
            if (ord(char) >= 65 and ord(char) <= 90):
                isCapital = True
            char = chr(ord(char) + key)
            if isCapital == True and ord(char) > 90:
                char = chr(ord(char) - 26)
            elif ord(char) > 122:
                char = chr(ord(char) - 26)
            text[index] = char
    text = ''.join(text)
    return text