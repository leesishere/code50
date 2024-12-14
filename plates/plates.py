import re
import sys


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
        sys.exit(0)
    else:
        print("Invalid")
        sys.exit(1)


def is_valid(s):
    # “All vanity plates must start with at least two letters.”
    # “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”

    count_letters(s[:2])
    if len(s) < 2 or len(s) > 6:
        return False

    # “No periods, spaces, or punctuation marks are allowed.”
    # Define patterns for characters and numbers
    if not only_letter_or_number(s):
        return False

    if count_numbers(s) > 0:
        #plate_list = order_of_things(s)
        # Numbers cannot be used in the middle of a plate; they must come at the end.
        # For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
        # CS50P2

        # The first number used cannot be a ‘0’.”
        if s[0] == '0':
            return False

        # The first number used cannot be a ‘0’.” or start with a number
        if count_numbers(s[0]):
            return False

        # Numbers in the middle of plate

        # Regular expression pattern to find numbers
        pattern = re.compile(r'\d+') # Find all matches
        numbers = pattern.findall(s)
        if len(numbers) > 1:
            return False

        # number must not be in the middle
        if count_letters(s[-1]) > 0:
            return False


    return True

def only_letter_or_number(s):
    # Regular expression pattern to match any non-alphabetic, non-numeric character
    pattern = re.compile(r'[^a-zA-Z0-9]')

    # Find all matches
    matches = pattern.findall(s)
    if len(matches) == 0:
        return True
    else:
        return False

def count_letters(s):
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return sum(1 for char in s if char.upper() in alphabet)

def count_numbers(s):
    numbers = list('0123456789')
    return sum(1 for num in s if num in numbers)

def order_of_things(s):
    # Define the pattern to split by digits and non-digits
    #pattern = r'[a-zA-Z]+|\d+'
    pattern = f'[a-zA-Z0-9]'
    return re.findall(pattern, s)

if __name__ == "__main__":
    main()
