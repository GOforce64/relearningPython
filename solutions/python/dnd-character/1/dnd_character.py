import random

class Character:
    def __init__(self):
        self.strength = dice_rolls()
        self.dexterity = dice_rolls()
        self.constitution = dice_rolls()
        self.intelligence = dice_rolls()
        self.wisdom = dice_rolls()
        self.charisma = dice_rolls()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        return self.hitpoints

def modifier(value):
    value = (value - 10) // 2
    return value

def dice_rolls():
    rolls = [None]*4
    lowest = 6
    lowest_index = 0
    for i in range(3):
        rolls[i] = random.randint(1,6)
        if rolls[i] < lowest:
            lowest = rolls[i]
            lowest_index = i
            
    total = 0
    lowest_deleted = False
    for i in range(3):
        if rolls[i] == lowest and lowest_deleted == False:
            lowest_deleted = True
        else:
            total = total + rolls[i]
    return total