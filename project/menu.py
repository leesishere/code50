from time import sleep
import sys
from random import uniform
import os
import requests
import random

error_count = 0

def main_menu()->str:
    """
    Description
    ----------
    Displays the game levels from 1-5 and retrieves from the user their selection of difficulty in the game levels and returns the level selected.
    If the player enters qq, the game will print a farewell and ask the player if they would like to hear a programmer's joke before they exit the game.
    The game will end if the player clicks any key besides 1-5 more than 5 times.

    Parameters
    ----------
    main_menu(None) : str
    No parameters

    User input
    ----------
    User Level
    Enter key more than 5 will call fairwell()
    qq to exit game

    Returns
    -------
    User level 1-5 or exists game
    """
    global error_count
    menu_level()
    while True:
        user_level = input()
        try:
            if 0 < int(user_level) and int(user_level) < 6:
                break
            else:
                error_count += 1
                if error_count > 5:
                    print(f"\n{fairwell()}")
                    sys.exit()
                menu_level(False)
        except:
            if user_level == "" or str(user_level):
                if user_level.lower() == 'qq':
                    i_quite()
                error_count += 1
                menu_level(False)
            if error_count > 5:
                print(f"\n{fairwell()}")
                sys.exit()
    return user_level

def i_quite()->None:
    """

    Description
    ----------
    This function takes no params, calls fairwell() with an option to call get_joke() before exiting the program.

    Parameters
    ----------
    i_quite(None) : None
    No parameters

    User input
    ----------
    How about a joke before you go (y/n)

    Returns
    -------
    None
    """
    os.system('clear')
    print(f"\n{fairwell()}")
    print("How about a joke before you go (y/n): ", end='')
    if is_no():
        sys.exit()
    joke = get_joke()
    print( f"\n{joke['setup']}")
    processing()
    print(f"\n{joke['punchline']}\n\n")
    sys.exit()

def is_no()->bool:
    """
    Description
    ----------
    This function takes no params and validate user input entered y or n and exit program after 5 or more failed attempts.

    Parameters
    ----------
    i_quite(None) : True/False
    No parameters

    User input
    ----------
    How about a joke before you go (y/n)

    Returns
    -------
    True for n
    False for y

    """
    global error_count
    while True:
        user_input = input()
        if user_input.lower() in 'n':
            return True
        if user_input.lower() in 'y':
            return False
        error_count += 1
        if error_count > 5:
            print(f"\n{fairwell()}")
            sys.exit()

def fairwell()->str:
    """
    Description
    ----------
    This function takes no params and returns a fairwell phrase at random.

    Parameters
    ----------
    fairwell(None) : str
    No parameters

    User input
    ----------
    None

    Returns
    -------
    fairwell phrase as string

    """
    sentences = [
        "I understand your decision, and I respect it.",
        "Thank you for being part of our team, your efforts were always appreciated.",
        "I'm sorry to see you go, but I wish you all the best in your future endeavors.",
        "If you ever decide to come back, we'll welcome you with open arms.",
        "It's important to take care of yourself, and I support your choice.",
        "I appreciate all the good times we had together in the game.",
        "Feel free to stay in touch; you're always a friend.",
        "Quitting can be tough, but sometimes it's the right decision.",
        "Your presence will be missed, but your well-being matters more.",
        "If you need anything, don't hesitate to reach out.",
        "'Frankly, my dear, I don't give a damn.' - Gone with the Wind",
        "Goodbye! Take care and see you soon!",
        "Farewell! Wishing you all the best.",
        "See you later! Stay safe and have a great day.",
        "Take care! Until next time.",
        "Goodbye for now! Keep in touch.",
        "Farewell, my friend! Until we meet again.",
        "See you around! Have a wonderful time.",
        "Catch you later! Don't be a stranger.",
        "Catch you on the flip side! Don't do anything I wouldn't do.",
        "Goodbye! May your Wi-Fi always be strong.",
        "See you later, alligator! After a while, crocodile!",
        "I'm outta here! You just got lucky.",
        "Hasta la vista, baby! (This is my best Terminator voice)",
        "Toodles! Try not to miss me too much.",
        "Bye! Don't forget to feed the cat (even if you don't have one)."
    ]
    return random.choice(sentences)


def processing()->str:
    """
    Description
    ----------
    This function takes no params and prints a progress chart.

    Parameters
    ----------
    processing(None) : str
    No parameters

    User input
    ----------
    None

    Returns
    -------
    prints a progress chart:
    [*                   ] 5%
    [***                 ] 15%
    [*****               ] 25%
    [******              ] 30%
    [********            ] 40%
    [**********          ] 50%
    [************        ] 60%
    [**************      ] 70%
    [****************    ] 80%
    [******************* ] 95%
    [********************] 100%

    """
    for i in range(21):
        sys.stdout.write('\r')
        # the exact output you're looking for:
        sys.stdout.write("[%-20s] %d%%" % ('*'*i, 5*i))
        sys.stdout.flush()
        sleep(0.25)

def get_joke()->str:
    """
    Description
    ----------
    This function takes no params, performs api to https://official-joke-api.appspot.com/jokes/programming/random and returns a programming joke as string

    Parameters
    ----------
    get_joke(None): str
    No parameters

    User input
    ----------
    None

    Returns
    -------
    returns a programming joke as string

    """

    url = "https://official-joke-api.appspot.com/jokes/programming/random"

    # Send a GET request to the API
    response = requests.get(url)
    #time.sleep(10)  # Sleep for 5 seconds
   # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data[0]
    else:
        return None

def menu_level(typer=True)->None:
    """
    Description
    ----------
    This function takes True/False to determine whether the user-level menu is displayed on the screen in typewriter mode.

    Parameters
    ----------
    menu_level(bool): None

    User input
    ----------
    Select leve 1-5

    Returns
    -------
    None

    """

    os.system('clear')
    indent = " " * 4
    if typer == True:
        print(f"{indent} Welcome to The Guessing Word Game.\n\n")
        sleep(1)
    os.system('clear')
    menu =  "\n"
    menu += indent + "Please select the game level 1-5\n"
    menu += indent + "------------------------------\n"
    menu += indent + "1  Easier Than Easy\n"
    menu += indent + "2  Easy\n"
    menu += indent + "3  Normal \n"
    menu += indent + "4  Hard\n"
    menu += indent + "5  Difficult\n"
    menu += indent + "------------------------------\n"
    menu += indent + "Please select your level (1-5): "
    # Easy / Beginner / Novice.
    # Normal / Medium / Standard / Average / Intermediate.
    # Hard / Expert / Difficult.

    if typer:
        type_writer(menu)
    else:
        print(menu, end='', flush=True)

def type_writer(line)->None:
    """
    Description
    ----------
    This function takes string and memics a typewriter mode

    Parameters
    ----------
    type_writer(str): None

    User input
    ----------
    None

    Returns
    -------
    None

    """
    for x in line:
        print(x, end='')
        sys.stdout.flush()
        #sleep(0.1)
        sleep(uniform(0, 0.1))


if __name__ == "__main__":
    main_menu()




