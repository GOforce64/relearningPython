def translate(word):
    words = word.split()
    vowels = ['a','e','i','o','u','y']
    xryt = ["xr", "yt"]

    sentence = ""
    for text in words:
        if (text[0] in vowels and text[0] != 'y') or (text[:2] in xryt):
            sentence = sentence + text + "ay"
        
        elif (text[1] not in vowels and text[2] not in vowels):
            temp = text[:3]
            sentence = sentence + text.lstrip(temp) + temp + "ay"
            
        elif (text[1] not in vowels):
            temp = text[:2]
            if text[1:3] == "qu":
                temp = text[:3]
            sentence = sentence + text.lstrip(temp) + temp + "ay"
        elif (text[0] not in vowels or text[0] == 'y'):
            temp = text[:1]
            if text[:2] == "qu":
                temp = text[:2]
            sentence = sentence + text.lstrip(temp) + temp + "ay"
        sentence = sentence + " "
    sentence = sentence.strip()
    return sentence
