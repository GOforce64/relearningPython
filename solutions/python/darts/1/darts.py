def score(x, y):
    if (x**2 + y**2) <= 1**2:
        return 10
    if (x**2 + y**2) <= 5**2:
        return 5
    if (x**2 + y**2) <= 10**2:
        return 1
    return 0
