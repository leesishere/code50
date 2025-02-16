import requests
import json
import time
import prettyjson

# Define the global count variable
interval = 250

def get_word(word):
    # Define the API endpoint
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    time.sleep(5)
    # Send a GET request to the API
    response = requests.get(url)
    #time.sleep(10)  # Sleep for 5 seconds
   # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data[0]
    else:
        return None

def get_audio(data):
    try:
        audio = data['phonetics'][1]['audio']
    except:
        audio = False
    return audio

def get_text(data):
    try:
        text = data['phonetics'][1]['text']
    except:
        text = False
    return text

def get_meaning(data):
    try:
        meanings = data['meanings']
    except:
        meanings = False
    return meanings

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

def analyze_word_complexity(word, word_record):
    complexities = {
        'word': word,
        'audio': get_audio(word_record),
        'text': get_text(word_record),
        'meanings':get_meaning(word_record),
        'letter_count': count_letters(word),
        'syllable_count': count_syllables(word),
        'phonetic_complexity': is_phonetically_complex(word),
        'morphological_complexity': has_morphological_complexity(word)
    }
    return complexities


def open_and_parse_file(filename,out_filename, start_word=None):
    global interval
    word_count = 0
    word_complexities = {}
    found_word = False
    if start_word is None:
        start_json(out_filename)
        found_word = True

    with open(filename, 'r') as rfile:
        lines = rfile.readlines()
        for word in lines:
            word = word.strip()
            if word == start_word:
                found_word = True
                continue
            if not found_word:
                continue
            print(f"{word}")
            word_count += 1
            word_record = get_word(word.strip())
            #if get_audio(word_record):
            #    word_complexities.update(analyze_word_complexity(word.strip(),word_record))
            #    append_to_json(word_complexities,out_filename)
            #    if word_count > interval:
            #        # pause 10 minutes
            #        time.sleep(600)
            #        interval += 250
            word_complexities.update(analyze_word_complexity(word.strip(),word_record))
            append_to_json(word_complexities,out_filename)
            if word_count > interval:
                # pause 10 minutes
                time.sleep(600)
                interval += 250
    end_json(out_filename)



def append_to_json(record, filename):
    with open(filename, 'a') as file:
        json.dump(record, file)
        file.write(',\n')  # Ensure each record is on a new line

    #print(f"Record added: {record}")

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
        # Find the position of the last comma
        last_comma_index = content.rfind(',')
        if last_comma_index != -1:
            # Remove the last comma
            content = content[:last_comma_index] + content[last_comma_index + 1:]
            # Write the modified content back to the file
            file.seek(0)
            file.write(content)
            file.truncate()

def format_json_file(filename, indent=4):
    with open(filename, "r") as file:
        # Load the content of the file
        content = json.load(file)

    with open(filename, "w") as file:
        # Write the formatted JSON content with specified indentation
        json.dump(content, file, indent=indent, separators=(", ", ": "))


out_filename = "word_dict_new.json"
open_and_parse_file('google-10000-english-no-swears.txt',out_filename, 'studio')

format_json_file(out_filename, indent=4)
