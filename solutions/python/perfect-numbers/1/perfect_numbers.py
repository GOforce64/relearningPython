def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    total = 0
    divisor = 1
    while (divisor <= number/2):
        if (number % divisor) == 0:
            total = total + divisor
        divisor += 1
    if total == number:
        return "perfect"
    elif total > number:
        return "abundant"
    else:
        return "deficient"
