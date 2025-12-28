def rows(letter):
    if letter == "A":
        return ["A"]
        
    diamond = []
    original_difference = ord(letter) - ord("A")
    difference = original_difference
    char_to_add = "A"
    reverse_flag = False
    middle_index = -1
    
    while difference >= 0 and difference <= original_difference:
        string_to_add = ""
        for i in range(difference):
            string_to_add = string_to_add + " "
        string_to_add = string_to_add + char_to_add

        if difference != original_difference:
            for i in range(middle_index):
                string_to_add = string_to_add + " "
            string_to_add = string_to_add + char_to_add
            
        for i in range(difference):
            string_to_add = string_to_add + " "
            
        diamond.append(string_to_add)
        
        if difference == 0:
            reverse_flag = True
            
        if reverse_flag:
            difference = difference + 1
            middle_index = middle_index - 2
            char_to_add = chr(ord(char_to_add) - 1)
        else:
            difference = difference - 1
            middle_index = middle_index + 2
            char_to_add = chr(ord(char_to_add) + 1)
    return diamond
        
        
