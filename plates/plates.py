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

    if count_numbers(s) > 0:
        plate_list = order_of_things(s)
        # Numbers cannot be used in the middle of a plate; they must come at the end.
        # For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
        # CS50P2

        # Numbers in the middle of plate
        if count_numbers(s[-1]) == 0:
            return False
        number_cnt = 0
        for i in plate_list:
            if count_numbers(i):
                number_cnt += 1
        if number_cnt > 1:
            return False

        #The first number used cannot be a ‘0’.”
        for num in plate_list:
            if count_numbers(num):
                if num[0] == '0':
                    return False

    # “No periods, spaces, or punctuation marks are allowed.”
    # Define patterns for characters and numbers
    if only_letter_or_number(s):
        return False

    return True

def only_letter_or_number(s):
    # Regular expression pattern to match any lowercase letters
    pattern = re.compile(r'[a-zA-Z]+|\d+')

    # List to hold strings without leters or numbers
    none_valid_chat = [s for s in strings if not pattern.search(s)]
    print count(none_valid_chat)

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
