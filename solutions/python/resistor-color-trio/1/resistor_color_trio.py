color_codes = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

def label(colors):
    color_comb = 0
    exponent = 0
    for index, color in enumerate(color_codes):
        if color == colors[0]:
            color_comb = color_comb + index * 10
        if color == colors[1]:
            color_comb = color_comb + index
        if color == colors[2]:
            exponent = index

    color_comb = color_comb * 10 ** exponent 
    
    suffix = ""
    if (color_comb % (10**9)) == 0 and color_comb != 0:
        suffix = " gigaohms"
        color_comb = color_comb / 10**9
    elif (color_comb % (10**6)) == 0 and color_comb != 0:
        suffix = " megaohms"
        color_comb = color_comb / 10**6
    elif (color_comb % (10**3)) == 0 and color_comb != 0:
        suffix = " kiloohms"
        color_comb = color_comb / 10**3
    else:
        suffix = " ohms" 
    output = str(int(color_comb))
    output = output + suffix
    return output
