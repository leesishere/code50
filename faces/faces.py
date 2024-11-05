


unicode_dict = {
    "U+1F600": ":D",
    "U+1F603": ":D",
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
    # Example usage
    for code, description in unicode_dict.items():
        smilley = chr(code)
        print(f"{smilley} {description}")

    # Convert Unicode code point to a character
    unicode_char = chr(0x1F637)
    print(unicode_char)  # Output: 😷


def emoticons(s):
    find_emotions = s.plit(' ')
    [x for x in find_emotions if x == ':)' ]
   # slit space and then Join the list back into a string...
    return '...'.join(s.split(' '))

main()
