import argparse
import pyfiglet

from pyfiglet import Figlet
f = Figlet(font='slant')
print f.renderText('text to render')

def main():
    parser = argparse.ArgumentParser(description='Process some arguments.')
    parser.add_argument('-f', '--font', type=str, help='Specify the font name')
    args = parser.parse_args()

    if args.font:
        requested_string = input("Input: ").lower()

        # Create a pyfiglet object with a specific font
        figlet = pyfiglet.Figlet(font=args.font)

        # Generate ASCII art
        ascii_art = figlet.renderText(requested_string )

        # Print the result
        print(ascii_art)


if __name__ == "__main__":
    main()
