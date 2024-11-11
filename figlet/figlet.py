from pyfiglet import Figlet
import random
import sys
from pprint import pprint


class ArgParser:
    def __init__(self, flag, argv):
        self.flag_list = flag.split(',')
        self.font = get_font_name(argv)
        self.font_list = figlet.getFonts()

    def get_font_name(self, argv):
        if len(argv) == 3: # file_name[0] -flag[1] font_name[2]
            return argv[2]
        else:
            return None

    def is_flag_present(self, argument):
        return argument in self.flag_list

    def is_font_type_present(self):
        return True if self.font else False

    def is_font_type_in_Figlet(self):


        return True if self.font else False

# Example usage
parser = ArgParser('-f,--font', sys.argv)
print(parser.is_flag_present('-f'))  # Output: True
print(parser.is_flag_present('--font'))  # Output: True
print(parser.is_flag_present('--other'))  # Output: False
print(parser.is_font_type_present())  # Output: True/False


#print(sys.argv[1])
#print(sys.argv[2])

exit()

def main():
    # Access individual arguments
    parser.display_info(sys.argv[1])
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
