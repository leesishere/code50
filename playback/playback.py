
def main():


def slow(s):
    # Split the string by spaces
    split_text = s.split(' ')

    # Replace ' ' with '...' in the list
    replaced_text = [word + '...' for word in split_text]

    # Join the list back into a string
    return '...'.join(replaced_text)


