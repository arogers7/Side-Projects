import random
from helper import *

run_times = 100000

wins = {"change":0,"maintain":0}

for i in range(run_times):
    change_guess(new_game(),guess())
    maintain_guess(new_game(),guess())


def maintain_guess(game,guess):
    """This is the version where you do not switch from your original guess """
    #we don't bother revealing a goat here because no matter what, you are staying with your first choice
    if(game[guess] == "car"):
        wins["maintain"] += 1

def change_guess(game,guess):
    """This is the version where you switch your guess after the goat is revealed"""
    goat = reveal_goat(game,guess)
    for i in range(3):
        if (i != guess and i != goat):
            new_guess = i

    newguesses[new_guess] += 1
    if (game[new_guess] == "car"):
        wins["change"] += 1




print("maintain:",wins["maintain"]/run_times,"\nchange",wins["change"]/run_times)
print(newguesses)
