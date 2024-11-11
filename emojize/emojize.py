import re
import sys
sys.path.append('.')

from emoji import emoji_dict
emoji = emoji_dict
pattern_colon = r':\w+:'

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
def main():
    while True:
        input_message = input("Input: ").strip().split()
        

if __name__ == "__main__":
    main()
