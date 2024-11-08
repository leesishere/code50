# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”

# “No periods, spaces, or punctuation marks are allowed.”
import re


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # “All vanity plates must start with at least two letters.”
    # “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”#
    if count_letters(s[:2]) != 2 or len(s) > 6:
        return False
    if count_numbers:
        plate_list = order_of_things(s)
        # Numbers cannot be used in the middle of a plate; they must come at the end.
        if count_letters(plate_list[0]) and count_letters(plate_list[-1]):
            return False
        #The first number used cannot be a ‘0’.”
        [num for num in plate_list if num in numbers]

def count_letters(s):
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return sum(1 for char in s if char.upper() in alphabet)

def count_numbers(s):
    numbers = list('0123456789')
    return sum(1 for num in s if num in numbers)

def order_of_things(s):
    # Define the pattern to split by digits and non-digits
    pattern = r'[a-zA-Z]+|\d+'
    return re.findall(pattern, s)

if __name__ == "__main__":
    main()
