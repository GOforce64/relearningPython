def egg_count(display_value):
    binary = bin(display_value)
    binary_eggs = binary.replace("0b", "")
    total_eggs = 0
    for egg in binary_eggs:
        print(egg)
        if (int(egg) == 1):
            total_eggs = total_eggs + 1
    return total_eggs
