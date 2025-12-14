def square_root(number):
    counter = 1
    while True:
        sqrt = counter * counter
        if number == sqrt:
            return counter
        else:
            counter = counter + 1
        if counter >= number:
            break
