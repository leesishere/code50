from pyfiglet import Figlet
import random
import sys
from pprint import pprint


class ArgParser:
    def __init__(self, flag, argv):
        self.flag_list = flag.split(',')
        self.font = self.get_font_name(argv)
        self.font_list = figlet.getFonts()

    def get_font_name(self, argv):
        if len(argv) == 3: # file_name[0] -flag[1] font_name[2]
            return argv[2]
        else:
            return None

    def get_random_font(self):
        end = len(self.font_list) - 1
        # Generate a random number
        random_index = random.randint(0, end)
        return self.font_list[random_index]

    def is_flag_present(self, argument):
        return argument in self.flag_list

    def is_font_type_present(self):
        return True if self.font else False

    def is_font_type_in_Figlet(self):
        return self.font in self.font_list


def main():
    parser = ArgParser('-f,--font', sys.argv)
    figlet = Figlet()
    requested_string = input("Input: ").lower().strip()

    if (parser.is_flag_present('-f') or parser.is_flag_present('--font')) and (parser.is_font_type_present() and parser.is_font_type_in_Figlet()):
        # Create a pyfiglet object with a specific font
        figlet.setFont(font=parser.get_font_name())

        # Generate ASCII art
        ascii_art = figlet.renderText(requested_string)

        # Print the result
        print(ascii_art)

    exit()


    figlet = Figlet()
    requested_string = input("Input: ").lower().strip()


if __name__ == "__main__":
    main()
