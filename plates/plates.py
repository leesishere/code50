# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”#
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6:
        return False
    [x for x in l if type(x) == type(0)]




letters = r'[a-zA-Z]'
pattern = r'\d+'

result = ''.join(letters_only)


# Define the pattern to split by digits and non-digits
pattern = r'(\d+|\D+)'
parts = re.findall(pattern, text)

if __name__ == "__main__":
    main()
