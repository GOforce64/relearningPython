def is_valid(isbn):
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
