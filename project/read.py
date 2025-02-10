
def load_dict_from_txt(filename):
    with open(filename, 'r') as file:
        data = file.read().strip()
        # Convert string representation of dictionary to actual dictionary
        word_dict = eval(data)
    return word_dict


def search_word(word, word_dict):
    return word_dict.get(word, 'Word not found in the dictionary.')

# Usage
filename = 'word_dict.json'
word_dict = load_dict_from_txt(filename)

# Example searches
print(search_word('alibi', word_dict))
print(search_word('able', word_dict))
print(search_word('Ache', word_dict))  # This word is not in the dictionary
