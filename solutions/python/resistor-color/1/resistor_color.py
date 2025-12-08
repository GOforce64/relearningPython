colour_codes = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white",]

def color_code(color):
    """Return the color code of the given colour

    :param color: string - the color to find the code for.
    :return: int - the code for the color given
    """
    
    for index, colour_code in enumerate(colour_codes):
        if colour_code == color:
            return index
    return -1

def colors():
    """Return color list

    :return: list - the color list
    """
    return colour_codes
