
def main():


def slow(s):
    # Split the string by spaces
    split_text = s.split(' ')

    # Replace ' ' with '...' in the list
    replaced_text = [word.replace('CS50', 'CS50x') for word in split_text]

    # Join the list back into a string
    result = ' '.join(replaced_text)

# Original string
text = "Hello, welcome to CS50. CS50 is great!"



print(result)

