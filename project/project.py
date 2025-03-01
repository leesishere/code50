


from menu import main_menu
from menu import is_no
import user
import os, json
import random, time

def main():
    user_name = user.set_user()
    user.high_score()
    input()
    user_level = main_menu()
    guess_menu(user_level, user_name)

def get_score(s, guess_count=0):
    score = 0
    unique_letters = set()
    for i in range(len(s)):
        unique_letters.add(s[i])
    letter_count = len(unique_letters)
    if guess_count==0:
        letter_count
    if guess_count <= 20:
        score = 2 * letter_count
    if guess_count <= 15:
        score = 7 * letter_count
    if guess_count <= 10:
        score = 12 * letter_count
    return score


def guess_menu(user_level, user_name):
    word = select_word(user_level)
    guess_count = 0
    #word ='july'
    count = len(list(filter(lambda x: x != ' ', word)))
    letter = ''
    word_guess_display = '_ ' * count
    quess_letters = ''
    while True:
        os.system('clear')
        word_guess_screen = f"Playing level {user_level}   Total score: {user.get_user_score(user_name)}\n"
        word_guess_screen += f"Round(s): {guess_count} letter(s): {quess_letters}  \n\n"
        word_guess_screen += f"Word guess game: "
        word_guess_display = display_word(word,letter, word_guess_display)

        print(word_guess_screen + word_guess_display)
        if '_' not in word_guess_display:

            points = get_score(word,guess_count)
            user.add_score(user_name,points)
            if points > 20:
                print(f"Congratulations! You scored: {points}!")
                print(f"Your new total game score: {user.get_user_score(user_name)}.\n\n")
            elif points > 10:
                print(f"You have successfully scored: {points}!")
                print(f"Your new total game score: {user.get_user_score(user_name)}.\n\n")
            else:
                print(f"Your score was {points}. Try again.\n\n")

            time.sleep(2)
            print("Play again (y/n): ", end='')
            if is_no():
                exit()
            else:
                word = select_word(user_level)
                guess_count = 0
                #word ='july'
                count = len(list(filter(lambda x: x != ' ', word)))
                letter = ''
                word_guess_display = '_ ' * count
                quess_letters = ''
                os.system('clear')
                word_guess_screen = f"Playing level {user_level}   Total score: {user.get_user_score(user_name)}\n"
                word_guess_screen += f"Round(s): {guess_count} letter(s): {quess_letters}  \n\n"
                word_guess_screen += f"Word guess game: "
                word_guess_display = display_word(word,letter, word_guess_display)
                print(word_guess_screen + word_guess_display)
        print("Enter letter: ", end='')
        letter = input().lower()
        # if someone tries to guess the whole word. It will only cound as one guess :-)
        if len(letter) > 1:
            for i in range(len(letter) - 1):
                word_guess_display = display_word(word,letter[i], word_guess_display)
            letter = letter[-1]
        if letter not in quess_letters:
            quess_letters += letter + ' '
            guess_count += 1

def replace(s,replacement,index):
    return s[:index] + replacement + s[index+1:]

def display_word(word,guess='', display=''):
    word_length = len(word)
    range_obj=range(word_length)

    for index in range_obj:
        if word[index] == guess:
            display = replace(display,guess,index)

    return display

def select_word(user_level):
    file_name = f"word_level_{user_level}.json"
    space_word = ''
    data = load_data(file_name)
    select_word = random.randint(1, len(data["words"]))
    word = data['words'][select_word]['word']

    for ch in word:
        space_word += ch + ' '
    return space_word

def load_data(file_name):
    if os.path.isfile(file_name):
        with open(file_name, 'r') as json_file:
            return json.load(json_file)

if __name__ == "__main__":
    main()

