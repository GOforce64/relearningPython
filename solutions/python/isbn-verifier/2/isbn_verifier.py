def is_valid(isbn):
    """
    Given a string the program should check if the provided string is a valid ISBN-10. Putting this into place
    requires some thinking aboutpreprocessing/parsing of the string prior to calculating the check digit for the ISBN.
    The program should be able to verify ISBN-10 both with and without separating dashes.
    hese may be communicated with or without hyphens, and can be checked for their validity by the following formula:
    (d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) mod 11 == 0
    If the result is 0, then it is a valid ISBN-10, otherwise it is invalid.
    """
    isbn = isbn.replace('-','')
    print(isbn)
    if len(isbn) != 10:
        return False
    isbnList = list(isbn)
    count = 10
    total = 0
    for digit in isbnList:
        if digit == 'X' and count != 1:
            return False
        if digit == 'X':
            total = total + 10
        else:
            intValue = ord(digit) - ord('0')
            total = total + count * intValue
            count = count - 1
    if total % 11 == 0:
        return True
    return False
