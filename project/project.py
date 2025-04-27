from menu import main_menu, is_no, i_quite, fairwell
import user
import os, json
import random, time
import sys

error_count = 0


def main()->None:
    """
    Description
    ----------
    Retrieves username (player).
    If this is the player's first time playing the game, their username will be added to the user_scores.json file to keep track of their scores.
    The username (players) high scoreboard will be displayed on the screen.
    The level menu will be displayed to the player to select which level they would like to play the game in
    The game will start with selecting a random work to guess from either level 1-5 game level

    Parameters
    ----------
    main(None) : None

    User input
    ----------
    Any key to continue

    Returns
    -------
    None
    """
    user_name = user.set_user()
    user.high_score()
    input()
    user_level = main_menu()
    guess_menu(user_level, user_name)


def get_score(s, guess_count=0)->int:
    """
    Description
    ----------
    This function retrieves the word used in the game and the number of times the player took to guess it. Unique letters in the word are total and will be used to calculate the game score.
    With zero guesses or tries, the score will be the number of unique letters in the word
    10 or fewer guesses or tries, the score is 12 times the unique letters in the word
    15 or fewer guesses or tries, the score is 7 times the unique letters in the word
    20 or fewer guesses or tries, the score is 2 times the unique letters in the word
    More than 20 tries, the player receives a zero score:-(

    Parameters
    ----------
    get_score(str,int) : int

    User input
    ----------
    None

    Returns
    -------
    int as the score
    """

    score = 0
    unique_letters = set()
    for i in range(len(s)):
        unique_letters.add(s[i])
    letter_count = len(unique_letters)
    if guess_count <= 20:
        score = 2 * letter_count
    if guess_count <= 15:
        score = 7 * letter_count
    if guess_count <= 10:
        score = 12 * letter_count
    if guess_count == 0:
        score = letter_count
    return score


def guess_menu(user_level, user_name)->None:
    """
    Description
    ----------
    Creates the game display to play the game. Retrieves a random word from the level JSON file and shows the current username's (player) score.
    The display will show the number of letters for the word as underscores (_).
    For example, if the word is July, the gameplay screen will show _ _ _ _, and with a guess of j, the screen will show j _ _ _ and so on.

    Parameters
    ----------
    guess_menu(int,str) : int

    User input
    ----------
    str as letter guessed or (y/n) to continue or not to continue gameplay.

    Returns
    -------
    none
    """
    word = select_word(user_level)
    guess_count = 0
    # word ='july'
    count = len(list(filter(lambda x: x != " ", word)))
    letter = ""
    word_guess_display = "_ " * count
    quess_letters = ""
    while True:
        os.system("clear")
        word_guess_screen = f"Playing level {user_level}   Total score: {user.get_user_score(user_name)}\n"
        word_guess_screen += f"Round(s): {guess_count} letter(s): {quess_letters}  \n\n"
        word_guess_screen += f"Word guess game: "
        word_guess_display = display_word(word, letter, word_guess_display)

        print(word_guess_screen + word_guess_display)
        if "_" not in word_guess_display:

            points = get_score(word, guess_count)
            user.add_score(user_name, points)
            if points > 20:
                print(f"Congratulations! You scored: {points}!")
                print(
                    f"Your new total game score: {user.get_user_score(user_name)}.\n\n"
                )
            elif points > 10:
                print(f"You have successfully scored: {points}!")
                print(
                    f"Your new total game score: {user.get_user_score(user_name)}.\n\n"
                )
            else:
                print(f"Your score was {points}. Try again.\n\n")

            time.sleep(2)
            print("Play again (y/n): ", end="")
            if is_no():
                exit()
            else:
                word = select_word(user_level)
                guess_count = 0
                # word ='july'
                count = len(list(filter(lambda x: x != " ", word)))
                letter = ""
                word_guess_display = "_ " * count
                quess_letters = ""
                os.system("clear")
                word_guess_screen = f"Playing level {user_level}   Total score: {user.get_user_score(user_name)}\n"
                word_guess_screen += (
                    f"Round(s): {guess_count} letter(s): {quess_letters}  \n\n"
                )
                word_guess_screen += f"Word guess game: "
                word_guess_display = display_word(word, letter, word_guess_display)
                print(word_guess_screen + word_guess_display)
        print("Enter letter: ", end="")
        letter = input().lower()
        global error_count
        if letter == "":
            error_count += 1
        if letter.lower() == "qq":
            i_quite()
        if error_count > 5:
            print(f"\n{fairwell()}")
            sys.exit()

        # The Cheater
        if letter == "qwerty":
            letter = word
        if ((len(letter) * 2) > len(word)) and letter != word:
            guess_count += len(letter)
            print(f"*** {user_name}, cheater alert warning! ***")
            print("The round penalty will be implemented.")
            time.sleep(5)
            next
        # if someone tries to guess the whole word. It will only cound as one guess :-)
        if (len(letter) * 2) == len(word) or letter == word:
            for i in range(len(letter) - 1):
                word_guess_display = display_word(word, letter[i], word_guess_display)
            letter = letter[-1]
        elif letter not in quess_letters:
            # sorting letters and spaces
            # help see letters already picked in the list
            quess_letters += letter
            quess_letters = quess_letters.strip()
            quess_letters = " ".join(sorted(quess_letters))
            quess_letters = quess_letters.lstrip()
            guess_count += 1


def replace(s, replacement, index)->str:
    """
    Description
    ----------
    This function replaces the correct guessed letter of the underscores (_) location.
    For example, if the word is July and the current display is '_ _ _ _', this function will take in the display, '_ _ _ _'', replace the letter, such as j, the index location of j is in the word and return 'j _ _ _ '.

    Parameters
    ----------
    replace(str,str,int) : str

    User input
    ----------
    None

    Returns
    -------
    str

    """
    return s[:index] + replacement + s[index + 1 :]


def display_word(word, guess="", display="")->str:
    """
    Description
    ----------
    This function receives the word, guessed letter, and current display and loops through each letter of the word to determine if the guessed letter is in the word.
    If the guessed letter is in the word, this function will call the replace function to replace the _ in the display variable with the guessed letter.

    Parameters
    ----------
    display_word(str, str,str)->str

    User input
    ----------
    None

    Returns
    -------
    str
    """
    word_length = len(word)
    range_obj = range(word_length)

    for index in range_obj:
        if word[index] == guess:
            display = replace(display, guess, index)

    return display


def select_word(user_level)->str:
    """
    Description
    ----------
    This function receives the game level, loads the word JSON file with the appropriate level, and selects and returns a word at random to be played in the game.

    Parameters
    ----------
    select_word(str) : str

    User input
    ----------
    None

    Returns
    -------
    str

    """
    file_name = f"word_level_{user_level}.json"
    space_word = ""
    data = load_data(file_name)
    select_word = random.randint(1, len(data["words"]))
    word = data["words"][select_word]["word"]

    for ch in word:
        space_word += ch + " "
    return space_word


def load_data(file_name):
    """
    Description
    ----------
    This function is a generic JSON file retriever. It validates that the JSON file exists, loads it into memory, and returns the data set in JSON file format.

    Parameters
    ----------
    load_data(str) : json

    User input
    ----------
    None

    Returns
    -------
    json
    """
    if os.path.isfile(file_name):
        with open(file_name, "r") as json_file:
            return json.load(json_file)

if __name__ == "__main__":
    main()
