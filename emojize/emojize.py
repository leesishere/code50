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
            colon_words = re.search(pattern_colon, input_command_line)
            print(f"{input_command_line} {colon_words}")

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
