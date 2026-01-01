def sum_of_multiples(limit, multiples):
    set_of_points = set()
    for number in multiples:
        set_to_add = []
        multiple = number
        
        while multiple < limit and multiple != 0:
            set_to_add.append(multiple)
            multiple = multiple + number
        set_of_points = set_of_points | set(set_to_add)
    return sum(set_of_points)
