


unicode_dict = {
    "U+1F604": ":D",
    "U+1F605": ":')",
    "U+1F606": "XD",
    "U+1F609": ";)",
    "U+1F642": ":)",
    "U+1F60B": ":P",
    "U+1F60E": "B)",
    "U+1F60D": "<3",
    "U+1F617": ":*",
    "U+1F618": ":*",
    "U+1F61A": ":*",
    "U+1F61C": ":P",
    "U+1F61D": ":P",
    "U+1F61E": ":(",
    "U+1F622": ":'( ",
    "U+1F623": ":(",
    "U+1F624": ">:(",
    "U+1F628": "D:",
    "U+1F629": ":(",
    "U+1F62A": "-_-",
    "U+1F62D": "T_T",
    "U+1F631": "D:",
    "U+1F632": ":O",
    "U+1F635": "@.@",
    "U+1F637": ":mask:"
}

def main():
    message = input()
    response = emoticons(message)
    print(response)

def emoticons(s):
    values_to_find = s.split(" ")
    return_message = ''

    # Iterate through the list of values and find the corresponding keys
    for value in values_to_find:
        key_for_value = next((key for key, val in unicode_dict.items() if val == value), None)
        if key_for_value is not None:
            return_message += " " + make_printable(key_for_value)
        else:
            return_message += " " + value
    return  return_message

def make_printable(u):
       # Remove the 'U+' prefix
        hex_string = u.replace('U+', '')
        # Convert the string to an integer
        unicode_int = int(hex_string, 16)
        # Get the Unicode character
        return chr(unicode_int)

def list_all_options():
    for code, description in unicode_dict.items():
        print(f"{make_printable(code)} {description}")

main()
