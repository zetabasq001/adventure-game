import time
import random

def print_pause(messages):
    if len(messages) == 0:
        return
    else:
        print(messages[0])
        time.sleep(2)
    print_pause(messages[1:])


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

    print_pause(messages)


def house():
    pass


def cave():
    pass


def valid_response(number):
    if number == '1':
        house()
    elif number == '2':
        cave()
    else:
        print_pause("(Please enter 1 or 2.)")
        print_pause("What would you like to do?")
        valid_response(input())


def enter_query():
    queries = ["Enter 1 to knock on the door of the house.",
    "Enter 2 to peer into the cave.",
    "What would you like to do?",
    "(Please enter 1 or 2.)"]

    print_pause(queries)

    valid_response(input())


enter_query()


