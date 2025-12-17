def find(search_list, value):
    if search_list == []:
        raise ValueError("value not in array")
    highest_index = len(search_list) - 1
    lowest_index = 0
    midway_index = int((highest_index + lowest_index) / 2)
    while True:
        if search_list[midway_index] == value:
            return midway_index
            
        elif lowest_index == highest_index:
            raise ValueError("value not in array")
            
        elif value > search_list[midway_index]:
            lowest_index = midway_index + 1
            midway_index = int((highest_index + lowest_index) / 2)
            
        elif value < search_list[midway_index]:
            if midway_index == 0:
                raise ValueError("value not in array")
            highest_index = midway_index - 1
            midway_index = int((highest_index + lowest_index) / 2)
