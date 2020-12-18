import time
import random

def print_pause(messages):
    if len(messages) == 0:
        return
    else:
        print(messages[0])
        #time.sleep(1)
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
    sword = False
    enter_query(sword)


def house():
    pass


def cave(sword):
    if sword:
        messages = ["You peer cautiously into the cave.",
                    "You've been here before,",
                    "and gotten all the good stuff.",
                    "It's just an empty cave now.",
                    "You walk back out to the field."]    
    else:
        messages = ["You peer cautiously into the cave.",
                    "It turns out to be only a very small cave.",
                    "Your eye catches a glint of metal behind a rock.",
                    "You have found the magical Sword of Ogoroth!",
                    "You discard your silly old dagger and take the sword with you.",
                    "You walk back out to the field."]

        sword = True

    print_pause(messages)
    enter_query(sword)


def field():
    pass


def fight():
    pass


def valid_response(number, sword):
    if number == '1':
        house()
    elif number == '2':
        cave(sword)
    else:
        print_pause(["(Please enter 1 or 2.)"])
        print_pause(["What would you like to do?"])
        valid_response(input(), sword)


def enter_query(sword):
    queries = ["Enter 1 to knock on the door of the house.",
    "Enter 2 to peer into the cave.",
    "What would you like to do?",
    "(Please enter 1 or 2.)"]

    print_pause(queries)

    valid_response(input(), sword)


intro()


