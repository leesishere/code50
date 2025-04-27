
import json


#def load_word_dictionary(filename):
#    with open(filename, 'r') as file:
#        word_list = json.load(file)
#    return {entry['word']: entry for entry in word_list}

#def word(word, word_dict):
#    return word_dict.get(word, 'Word not found in the dictionary.')

# word_dict = load_word_dictionary(filename)

filename = '../word_dict.json'
# Load the JSON data from the file
with open(filename, 'r') as file:
    data = json.load(file)



# Example searches
#print(word('accursed', word_dict)['meanings'][0]['definitions'][0]['definition'])
#print(word('the', word_dict)['meanings'][0]['definitions'][0]['definition'])
#print(word('the', word_dict)['letter_count'])
#print(word('the', word_dict)['syllable_count'])

# Words with three or four syllables with a letter count between 12 and 15.

for word in data:
    if (word['letter_count'] >= 12 and word['letter_count'] <= 15) and (word['syllable_count'] == 3 or word['syllable_count'] == 4):
        print(f"{word['word']} {word['letter_count']} {word['syllable_count']}")
