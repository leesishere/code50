import argparse
from pyfiglet import Figlet
import random
from pprint import pprint

class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        self.print_usage()
        custom_message = f"Invalid usage\n"
        self.exit(2, custom_message)

def main():
    parser = argparse.ArgumentParser(description='Process some arguments.')
    parser.add_argument('-f', '--font', type=str, help='Specify the font name')
    try:
        args = parser.parse_args()
    except:
        pass

    figlet = Figlet()
    requested_string = input("Input: ").lower().strip()

    if args.font:
        # Create a pyfiglet object with a specific font
        figlet.setFont(font=args.font)

        # Generate ASCII art
        ascii_art = figlet.renderText(requested_string)

        # Print the result
        print(ascii_art)
    else:
        font_list = figlet.getFonts()
        # Define the range
        start = 0
        end = len(font_list) - 1
        # Generate a random number
        random_index = random.randint(start, end)

        # Create a pyfiglet object with a specific font
        figlet.setFont(font=font_list[random_index])

        # Generate ASCII art
        ascii_art = figlet.renderText(requested_string)

        # Print the result
        print(ascii_art)

if __name__ == "__main__":
    main()
