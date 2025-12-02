def convert(number):
    hasSound = False
    outputstring = ""
    if (number % 3) == 0:
        outputstring = outputstring + "Pling"
        hasSound = True
    if (number % 5) == 0:
        outputstring = outputstring + "Plang"
        hasSound = True
    if (number % 7) == 0:
        outputstring = outputstring + "Plong"
        hasSound = True
    if hasSound == False:
        outputstring = str(number)
    return outputstring