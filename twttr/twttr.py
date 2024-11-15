# When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels,
# much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts
# the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
# whether inputted in uppercase or lowercase.

# list of vowels
vowels = ['A', 'E', 'I', 'O', 'U']

def main():
    s = input("Input: ")
    print("output: ", end="")
    for c in s:
        if c.upper() not in vowels:
            print(c, end="")
    print()

def shorten(word):
    ...
    
if __name__ == "__main__":
    main()
