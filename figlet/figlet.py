import argparse
from pyfiglet import Figlet


def main():
    parser = argparse.ArgumentParser(description='Process some arguments.')
    parser.add_argument('-f', '--font', type=str, help='Specify the font name')
    args = parser.parse_args()
    figlet = Figlet()

    if args.font:
        requested_string = input("Input: ").lower()

        # Create a pyfiglet object with a specific font
        figlet.setFont(font=args.font)

        # Generate ASCII art
        ascii_art = figlet.renderText(requested_string)

        # Print the result
        print(ascii_art)
    else:
        font_list = figlet.getFonts()
        print(font_list)


if __name__ == "__main__":
    main()
