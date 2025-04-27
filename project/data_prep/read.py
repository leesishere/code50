
import json

def load_word_dictionary(filename):
    with open(filename, 'r') as file:
        word_list = json.load(file)
    return {entry['word']: entry for entry in word_list}

def word(word, word_dict):
    return word_dict.get(word, 'Word not found in the dictionary.')

# Usage
filename = '../word_dict.json'

word_dict = load_word_dictionary(filename)

# Example searches
#print(word('accursed', word_dict)['meanings'][0]['definitions'][0]['definition'])
#print(word('the', word_dict)['meanings'][0]['definitions'][0]['definition'])
print(word('the', word_dict)['letter_count'])
print(word('the', word_dict)['syllable_count'])

