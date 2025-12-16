def commands(binary_str):
    actions = []
    if int(binary_str[-1]) == 1:
        actions.append("wink")
    if int(binary_str[-2]) == 1:
        actions.append("double blink")
    if int(binary_str[-3]) == 1:
        actions.append("close your eyes")
    if int(binary_str[-4]) == 1:
        actions.append("jump")
    if int(binary_str[-5]) == 1:
        actions.reverse()
    return actions
