import random
def new_game():
    """this method makes three doors, with two being goats and one being a car. This returns an array where the index that returns True is the car"""
    car = random.randrange(3)
    doors = ["goat"]*3
    doors[car] = "car"
    return doors

def guess():
    return random.randrange(3)

def reveal_goat(game,guess):
    """This returns a door that was not your guess with a goat behind it"""
    doors = [0,1,2]
    random.shuffle(doors)
    for door in doors:
        if (game[door] == "goat" and door != guess):

            return door
