color_codes = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

def value(colors):
    number = 0
    for index,color in enumerate(color_codes):
        if color == colors[0]:
            number = number + index * 10
        if color == colors[1]:
            number = number + index
    return number
