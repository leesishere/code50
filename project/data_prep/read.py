
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
    j_data = json.load(file)



# Example searches
#print(word('accursed', word_dict)['meanings'][0]['definitions'][0]['definition'])
#print(word('the', word_dict)['meanings'][0]['definitions'][0]['definition'])
#print(word('the', word_dict)['letter_count'])
#print(word('the', word_dict)['syllable_count'])

# Words with three or four syllables with a letter count between 12 and 15.
data = {"words": []}

for word in j_data:  # Level 4
    if (word['letter_count'] >= 12 and word['letter_count'] <= 15) and (word['syllable_count'] == 3 or word['syllable_count'] == 4):
        word_entry = {
            "word": f"{word['word']}",  # Change this to your dynamic word (e.g., f"word_{i}" or custom logic)
            "level": 4  # Dynamically set the level
        }
        data["words"].append(word_entry)  # Append the new entry to the "words" list

with open('word_level_4.json', 'w') as file:
    json.dump(data, file, indent=4)

# Words with 1 syllables with a letter count less than 5.
data = {"words": []}

for word in j_data:  # Level 1
    if (word['letter_count'] < 5) and (word['syllable_count'] == 1):
        word_entry = {
            "word": f"{word['word']}",  # Change this to your dynamic word (e.g., f"word_{i}" or custom logic)
            "level": 1  # Dynamically set the level
        }
        data["words"].append(word_entry)  # Append the new entry to the "words" list

with open('word_level_1.json', 'w') as file:
    json.dump(data, file, indent=4)
