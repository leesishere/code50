import argparse
from pyfiglet import Figlet
import random
from pprint import pprint


def main():
    # Access individual arguments
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]

    # Check if the correct number of arguments is provided
    if len(sys.argv) < 3:
        print("Usage: script.py <arg1> <arg2>")
        sys.exit(1)



    # Print the arguments
    print(f"Argument 1: {arg1}")
    print(f"Argument 2: {arg2}")

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
