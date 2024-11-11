import re
import sys
sys.path.append('.')

from emoji import emoji_dict
emoji = emoji_dict


def main():
    while True:
        input_message = input("Input: ").strip().split()
        message = ''
        for input_command_line in input_message:
            
            if input_command_line[0] == ':' and input_command_line[-1] == ':':
               input_command_line = input_command_line.lower()
               message += emoji[input_command_line] + ' '
            else:
                message +=  input_command_line + ' '

        if message:
            print(message)
            break

if __name__ == "__main__":
    main()
