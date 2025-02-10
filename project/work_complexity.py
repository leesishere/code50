import requests
import json
import os

# Define the global count variable
count = 0

def get_word(word):
    # Define the API endpoint
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    # Send a GET request to the API
    response = requests.get(url)
   # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data[0]
    else:
        return None

def get_howtosay(data):
        try:
            audio = data['phonetics'][0]['audio']
        except:
            audio = False
        return audio

def count_letters(word):
    return len(word)

def count_syllables(word):
    vowels = "aeiou"
    syllable_count = 0
    previous_char_was_vowel = False
    for char in word:
        if char in vowels:
            if not previous_char_was_vowel:
                syllable_count += 1
            previous_char_was_vowel = True
        else:
            previous_char_was_vowel = False
    return syllable_count

def is_phonetically_complex(word):
    # Check for phonetic complexity (e.g., silent letters, unusual phonemes)
    complex_patterns = ['kn', 'ph', 'gh', 'ch', 'tion', 'sion', 'ough']
    for pattern in complex_patterns:
        if pattern in word:
            return True
    return False

def has_morphological_complexity(word):
    # Check for prefixes and suffixes (e.g., un-, re-, -able, -ment)
    prefixes = ['un', 're', 'pre', 'dis', 'mis', 'non']
    suffixes = ['able', 'ment', 'ness', 'tion', 'sion', 'ive']
    for prefix in prefixes:
        if word.startswith(prefix):
            return True
    for suffix in suffixes:
        if word.endswith(suffix):
            return True
    return False

def analyze_word_complexity(word, how_to_say):
    complexities = {
        'word': word,
        'how_to_say': how_to_say,
        'letter_count': count_letters(word),
        'syllable_count': count_syllables(word),
        'phonetic_complexity': is_phonetically_complex(word),
        'morphological_complexity': has_morphological_complexity(word)
    }
    return complexities


def open_and_parse_file(filename,out_filename, cnt):
    global count
    word_complexities = {}
    start_json(out_filename)
    with open(filename, 'r') as rfile:
        lines = rfile.readlines()
        for word in lines:
            word_record = get_word(word.strip())
            how_to_say = get_howtosay(word_record)
            if how_to_say:
                word_complexities.update(analyze_word_complexity(word.strip(),how_to_say))
                append_to_json(word_complexities,out_filename)
                if count > cnt:
                    end_json(out_filename)
                    exit()
                else:
                    count += 1
    end_json(out_filename)

def append_to_json(record, filename):
    with open(filename, 'a') as file:
        json.dump(record, file)
        file.write(',\n')  # Ensure each record is on a new line

    print(f"Record added: {record}")

def start_json(filename):
    with open(filename, 'w') as file:
        file.write('[\n')  # Ensure each record is on a new line
def end_json(filename):
    remove_last_comma(filename)
    with open(filename, 'a') as file:
        file.write('\n]')  # Ensure each record is on a new line

def remove_last_comma(filename):
    with open(filename, "r+") as file:
        content = file.read()
        file.seek(0)
        file.write(content[:-1])
        file.truncate()



open_and_parse_file('word.txt','word_dict.json',5)



