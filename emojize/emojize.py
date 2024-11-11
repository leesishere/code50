import re
import sys
sys.path.append('.')

from emoji import emoji_dict
emoji = emoji_dict
pattern_colon = r':\w+:'

def main():
    # :CANdy: or ?:tHumbsUp: ?
    while True:
        input_message = input("Input: ").strip()
        colon_words = re.findall(pattern_colon, input_message)
        for find_text in colon_words:
            emoji_text = find_text.lower()
            input_message = input_message.replace(find_text, emoji[emoji_text])
        print(input_message)

'''
def main():
    while True:
        input_message = input("Input: ").strip().split()
        message = ''
        for input_command_line in input_message:
            colon_words = re.findall(pattern_colon, input_command_line)
            if colon_words:
                punctuation = input_command_line.replace(colon_words[0],'')
                message += f" {emoji[colon_words[0]]}{punctuation}"
            else:
                message += " " + input_command_line
        if message:
            print(f"output: {message}")
            break
'''



if __name__ == "__main__":
    main()
