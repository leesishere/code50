from pyfiglet import Figlet
import random
import sys
from pprint import pprint


class ArgParser(Figlet):
    def __init__(self, flag, argv):
        super().__init__()

        self.flag_list = flag.split(',')
        self.font = self.set_font_name(argv)
        self.font_list = self.getFonts()
        self.argv = argv
        print(self.is_comandline_correct())
        if not self.is_comandline_correct():
            sys.exit("Invalid usage")


    def set_font_name(self, argv):
        if len(argv) == 3: # file_name[0] -flag[1] font_name[2]
            return argv[2]
        else:
            return None

    def get_font_name(self):
        return self.font

    def get_random_font(self):
        end = len(self.font_list) - 1
        # Generate a random number
        random_index = random.randint(0, end)
        return self.font_list[random_index]

    def is_flag_present(self):
        return self.argv[1] in self.flag_list

    def is_font_type_present(self):
        return True if self.font else False

    def is_font_type_in_Figlet(self):
        return self.font in self.font_list

    def is_comandline_correct(self):
        print(f"is_comandline_correct == {len(self.argv) == 3} and {not (self.is_flag_present() or self.is_font_type_in_Figlet())}")
        print(f"is_comandline_correct == {self.is_flag_present()} or {self.is_font_type_in_Figlet()}")
        if len(self.argv) == 2 and not self.is_flag_present():
            return False
        elif(len(self.argv) == 3 and not (self.is_flag_present() or self.is_font_type_in_Figlet())):
            return False
        else:
            return True


def main():
    parser = ArgParser('-f,--font', sys.argv)



    requested_string = input("Input: ").strip()

    if parser.is_flag_present() and (parser.is_font_type_present() and parser.is_font_type_in_Figlet()):
        # Create a pyfiglet object with a specific font
        parser.setFont(font=parser.get_font_name())

        # Generate ASCII art
        ascii_art = parser.renderText(requested_string)

        # Print the result
        print(f"Output:\n{ascii_art}")

if __name__ == "__main__":
   main()
