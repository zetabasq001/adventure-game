import time
import random

def print_pause(message):
    print(message)
    time.sleep(2)


def intro():
    villains = ["deadly dragon", "wicked witch", "sinister sorcerer"]
    villain = random.choice(villains)

    messages = ["You find yourself standing in an open field, ",
    "filled with grass and yellow wildflowers. ", 
    f"Rumor has it that a {villain} is somewhere around here, ",
    "and has been terrifying the nearby village."]

    for message in messages:
        print_pause(message)

intro()