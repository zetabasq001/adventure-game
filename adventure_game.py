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
    enter_query(sword, villain)

def ending():
    pass

def house(sword, villain):

    messages = ["You approach the door of the house.",
                "You are about to knock when the door opens"
                f"and out steps a {villain}.",
                f"Eep! This is the {villain}'s house!",
                f"The {villain} attacks you!"]
    print_pause(messages)

    if not sword:
        messages = ["You feel a bit under-prepared for this,",
                "what with only having a tiny dagger."]
        print_pause(messages)

    print_pause(["Would you like to (1) fight or (2) run away?"])
    valid_response(input() + '2', sword, villain)


def cave(sword, villain):

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
                    "You discard your silly old dagger",
                    "and take the sword with you.",
                    "You walk back out to the field."]

        sword = True

    print_pause(messages)
    enter_query(sword, villain)


def field(sword, villain):

    messages = ["You run back into the field.",
                "Luckily, you don't seem to have been followed."]

    print_pause(messages)
    enter_query(sword, villain)


def fight(sword, villain):

    if not sword:
        messages = ["You do your best...",
                    f"but your dagger is no match for the {villain}.",
                    "You have been defeated!"]
        print_pause(messages)   
    else:
        messages = [f"As the {villain} moves to attack, you unsheath your new sword.",
                    "The Sword of Ogoroth shines brightly in your hand",
                    "as you brace yourself for the attack.",
                    f"But the {villain} takes one look at your shiny new toy and runs away!",
                    f"You have rid the town of the {villain}.",
                    "You are victorious!"]
        print_pause(messages)

    ending()


def valid_response(number, sword, villain):
    if number == '1':
        house(sword, villain)
    elif number == '2':
        cave(sword, villain)
    elif number == '12':
        fight(sword, villain)
    elif number == '22':
        field(sword, villain)
    else:
        print_pause(["(Please enter 1 or 2.)"])
        print_pause(["What would you like to do?"])
        valid_response(input(), sword, villain)


def enter_query(sword, villain):
    queries = ["\nEnter 1 to knock on the door of the house.",
    "Enter 2 to peer into the cave.",
    "What would you like to do?",
    "(Please enter 1 or 2.)"]

    print_pause(queries)

    valid_response(input(), sword, villain)


intro()


