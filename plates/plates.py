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

    # number start with 1 alphebetic charecters
    if count_letters(s[:2]) != 2:
        return False

    # nust not be longer that 6 charectors
    if len(s) > 6:
        return False

    # “No periods, spaces, or punctuation marks are allowed.”
    # Define patterns for characters and numbers
    if not only_letter_or_number(s):
        return False

    # CS50 class name is incorrectly entered
    #if len(s) == 4:
    #     if s[:2].upper() == 'CS':
    #         if s[2:] != '50':
    #             return False

    if count_numbers(s) > 0:
        #plate_list = order_of_things(s)
        # Numbers cannot be used in the middle of a plate; they must come at the end.
        # For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
        # CS50P2


        # The vharter can't start with a number
        if count_numbers(s[0]):
            return False

        # number must not be in the middle
        # Regular expression pattern to find numbers
        pattern = re.compile(r'\d+') # Find all matches
        numbers = pattern.findall(s)
        if len(numbers) > 1: # Numbers are seperate by alpebetic char via are in the middle
            return False
        elif len(numbers[0]) > 1:  # more than 1 number foud
            if numbers[0][0] == '0': # numbers must not start with zeros
                return False
            else:
                if numbers[0] == '0': # One number and must not start with zeros
                    return False

        # number must be at the end of plate string
        if count_letters(s[-1]) > 0:
            return False
    '''
    # not begining alphabetical
    plate_string = order_of_things(s)
    letters_count = count_letters(s)
    alpha = ['A','B','C','D','E','F']
    if plate_string[:letters_count] == alpha[:letters_count]:
        return False
    '''

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
    pattern = re.compile(f'[a-zA-Z0-9]')
    return re.findall(pattern, s)

if __name__ == "__main__":
    main()
