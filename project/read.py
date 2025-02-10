
import json

def load_word_dictionary(filename):
    with open(filename, 'r') as file:
        word_list = json.load(file)
    return {entry['word']: entry for entry in word_list}

def word(word, word_dict):
    return word_dict.get(word, 'Word not found in the dictionary.')

# Usage
filename = 'word_dict.json'
word_dict = load_word_dictionary(filename)

# Example searches
thisword = word('abstain', word_dict)

print(thisword['word'])
print(word('accepts', word_dict)['how_to_say'])
print(word('administer', word_dict)['letter_count'])  # This word is not in the dictionary
