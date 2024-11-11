import argparse
from pyfiglet import Figlet
import random
from pprint import pprint

class ArgPaser:
    def __init__(self, param_one, param_two):
        self.param_one = param_one
        self.param_two = param_two

    def display_info(self,arg):
        return arg in self.param_one


# Example usage
parser = ArgPaser('-f', '--font')

parser.display_info()
exit()

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
