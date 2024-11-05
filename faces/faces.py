


unicode_dict = {
    "U+1F604": ":D",
    "U+1F605": ":')",
    "U+1F606": "XD",
    "U+1F609": ";)",
    "U+1F60A": ":)",
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
    split_list = s.split(" ")

    for value in split_list:
        # Check if the value exists and print the corresponding key
        for key, value in unicode_dict.items():
            if value == value_to_find:
                print(f"The key for value {value_to_find} is {key}.")
                break
        else:
            print(f"The value {value_to_find} is not found in the dictionary.")


    try:
        # One-liner to find the key for the given value
        key_for_value = next(key for key, value in unicode_dict.items() if value == last_element)
        return_message = ", ".join(split_list[:-1])
        for value_to_find in split_list:
            key_for_value = [key for key, value in unicode_dict.items() if value == value_to_find]
            print(f"|{key_for_value}|")

    except:
        print("Program only accepts the following emoations :)")
        list_all_options()
        return "\n"
    return return_message + " " + make_printable(key_for_value)

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
