import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):

    # the best site ever: https://regex101.com/
    pattern = r'\b[uU][mM]\b'
    matches = re.findall(pattern, s)

    return len(matches)

if __name__ == "__main__":
    main()
