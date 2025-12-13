color_codes = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
tolerances_colors = ["grey", "violet", "blue", "green", "brown", "red", "gold", "silver"]
tolerances = ["0.05%", "0.1%", "0.25%", "0.5%", "1%", "2%", "5%", "10%"]

def resistor_label(colors):
    color_comb = 0
    exponent = 0
    if len(colors) == 4:
        for index, color in enumerate(color_codes):
            if color == colors[0]:
                color_comb = color_comb + index * 10
            if color == colors[1]:
                color_comb = color_comb + index
            if color == colors[2]:
                exponent = index
    elif len(colors) == 5:   
        for index, color in enumerate(color_codes):
            if color == colors[0]:
                color_comb = color_comb + index * 100
            if color == colors[1]:
                color_comb = color_comb + index * 10
            if color == colors[2]:
                color_comb = color_comb + index
            if color == colors[3]:
                exponent = index
    else:
        return "0 ohms"
    color_comb = color_comb * 10 ** exponent 
    
    suffix = ""
    if exponent >= 7 and color_comb != 0:
        suffix = " gigaohms"
        color_comb = color_comb / 10**9
    elif exponent >= 4 and color_comb != 0:
        suffix = " megaohms"
        color_comb = color_comb / 10**6
    elif exponent >= 1 and color_comb != 0:
        suffix = " kiloohms"
        color_comb = color_comb / 10**3
        if color_comb < 1:
            color_comb = color_comb * 10**3
            suffix = " ohms" 
    else:
        suffix = " ohms" 
    color_comb = round(float(color_comb),2)
    if color_comb.is_integer():
        output = str(int(color_comb))
    else:
        output = str(color_comb)
    
    tolerance = " ±"
    for index, color in enumerate(tolerances_colors):
        if color == colors[-1]:
            tolerance = tolerance + tolerances[index]
        
    output = output + suffix + tolerance
    return output
