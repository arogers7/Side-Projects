from helper import *
import random

def new_game():
    """this method makes three doors, with two being goats and one being a car. This returns an array where the index that returns True is the car"""
    car = random.randrange(3)
    doors = ["goat"]*3
    doors[car] = "car"
    return doors

def guess():
    """Guesses a random door"""
    return random.randrange(3)

def reveal_goat(game,guess):
    """This returns a door that was not your guess with a goat behind it"""
    doors = [0,1,2]
    random.shuffle(doors)
    for door in doors:
        if (game[door] == "goat" and door != guess):
            return door

def maintain_guess(game,guess):
    """This is the version where you do not switch from your original guess """
    #we don't bother revealing a goat here because no matter what, you are staying with your first choice
    if(game[guess] == "car"):
        return 1
    else:
        return 0

def change_guess(game,guess):
    """This is the version where you switch your guess after the goat is revealed"""
    goat = reveal_goat(game,guess)
    for i in range(3):
        if (i != guess and i != goat):
            new_guess = i
    if (game[new_guess] == "car"):
        return 1
    else:
        return 0


if __name__ == '__main__':
    run_times = 100000
    #these variables keep track of the number of times that the "changer" or "switcher" contestant wins their game
    change_wins,switch_wins = 0,0

    for i in range(run_times):
        #if each instantiation of a game is a win (the door reveals a car), a win is added to the contestants win count
        change_wins += change_guess(new_game(),guess())
        switch_wins += maintain_guess(new_game(),guess())

    print('The contestant who chose to remain with their choice won',change_wins/run_times*100,'% of their games\nThe user who changed their response won',switch_wins/run_times*100,'% of their games. This shows that the contestant who changes their answer is twice as likely to win their game, as predicted.')
