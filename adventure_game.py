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
    "and has been terrifying the nearby village.", 
    "In front of you is a house.",
    "To your right is a dark cave.",
    "In your hand you hold your trusty (but not very effective) dagger."]

    for message in messages:
        print_pause(message)


def enter_query():
    queries = ["Enter 1 to knock on the door of the house.",
    "Enter 2 to peer into the cave.",
    "What would you like to do?",
    "(Please enter 1 or 2.)"]

    number = ''
    for query in queries:
        print_pause(query)
    number = input()




