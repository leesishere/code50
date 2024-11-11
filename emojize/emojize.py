import re
import sys
sys.path.append('.')

from emoji import emoji_dict
emoji = emoji_dict
pattern_colon = r':\w+:'

def main():
    while True:
        input_message = input("Input: ").strip().split()
        message = ''
        for input_command_line in input_message:
            colon_words = re.findall(pattern_colon, input_command_line)
            if colon_words:
                print(f"index = {input_command_line.find(colon_words[0])}")
                print(f"{input_command_line} {colon_words[0]}")

            else:
                print(input_command_line)
            '''
            if input_command_line[0] == ':' and input_command_line[-1] == ':':
               input_command_line = input_command_line.lower()
               message += emoji[input_command_line] + ' '
            else:
                message +=  input_command_line + ' '
            '''

        if message:
            print(message)
            break

if __name__ == "__main__":
    main()
