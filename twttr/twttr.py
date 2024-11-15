# When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels,
# much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts
# the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
# whether inputted in uppercase or lowercase.

# list of vowels
vowels = ['A', 'E', 'I', 'O', 'U']

def main():
    word = input("Input: ")
    print(f"output: {shorten(word)}")


def shorten(word):
    no_vowels_workd = ''
    for c in word:
        if c.upper() not in vowels:
            no_vowels_workd += c
    return no_vowels_workd

if __name__ == "__main__":
    main()
