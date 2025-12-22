SPECIAL_CASES = ("IV", "IX", "XL", "XC", "CD", "CM")
LETTERS = ("I", "V", "X", "L", "C", "D", "M")

def roman(number):
    output = ""
    while number > 0:
        if number >= 1000:
            number = number - 1000
            output = output + LETTERS[6]
            
        elif number >= 500:
            if number >= 900:
                number = number - 900
                output = output + SPECIAL_CASES[5]
            else:
                number = number - 500
                output = output + LETTERS[5]
                
        elif number >= 100:
            if number >= 400:
                number = number - 400
                output = output + SPECIAL_CASES[4]
            else:
                number = number - 100
                output = output + LETTERS[4]
                
        elif number >= 50:
            if number >= 90:
                number = number - 90
                output = output + SPECIAL_CASES[3]
            else:
                number = number - 50
                output = output + LETTERS[3]
                
        elif number >= 10:
            if number >= 40:
                number = number - 40
                output = output + SPECIAL_CASES[2]
            else:
                number = number - 10
                output = output + LETTERS[2]
            
        elif number >= 5:
            if number == 9:
                number = number - 9
                output = output + SPECIAL_CASES[1]
            else:
                number = number - 5
                output = output + LETTERS[1]

        else:
            if number == 4:
                number = number - 4
                output = output + SPECIAL_CASES[0]
            else:
                number = number - 1
                output = output + LETTERS[0]
    return output

