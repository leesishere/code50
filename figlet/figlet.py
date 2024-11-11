import argparse
import pyfiglet


def main():
    parser = argparse.ArgumentParser(description='Process some arguments.')
    parser.add_argument('-f', '--font', type=str, help='Specify the font name')
    args = parser.parse_args()

    if args.font:
        requested_string = input("Input: ").lower()
        print(f"Font specified: {args.font}")

        # Create a pyfiglet object with a specific font
        figlet = pyfiglet.Figlet(font='slant')

        # Generate ASCII art
        ascii_art = figlet.renderText('Hello World')

        # Print the result
        print(ascii_art)


if __name__ == "__main__":
    main()
