import argparse
from pyfiglet import Figlet
import random
from pprint import pprint

def main():
    parser = argparse.ArgumentParser(description='Process some arguments.')
    parser.add_argument('-f', '--font', type=str, help='Specify the font name')
    args = parser.parse_args()
    figlet = Figlet()

    if args.font:
        requested_string = input("Input: ").lower()

        # Create a pyfiglet object with a specific font
        #print(args.font)
        figlet.setFont(font=args.font)

        # Generate ASCII art
        ascii_art = figlet.renderText(requested_string)

        # Print the result
        print(ascii_art)
    else:
        font_list = figlet.getFonts()
        # Define the range
        start = 0
        end = len(font_list)
        pprint(font_list)
        print(end)

        # 'runyc' 'fbr_stri'
        # Generate a random number
        random_number = random.randint(start, end)


if __name__ == "__main__":
    main()
