def proverb(*input_list, qualifier = None):
    if not input_list:
        return []
    if qualifier != None:
        qualifier = " " + qualifier + " "
    else:
        qualifier = " "
    output_list = []
    for index in range(len(input_list)-1):
        first_item, second_item = input_list[index], input_list[index + 1]
        output_list.append(f"For want of a {input_list[index]} the {input_list[index + 1]} was lost.")
    output_list.append(f"And all for the want of a{qualifier}{input_list[0]}.")
    return output_list
