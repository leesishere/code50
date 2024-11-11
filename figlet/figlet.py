import argparse

def main():
    parser.add_argument('-f', '--font', type=str, help='Specify the font name')
    if args.font:
        print(f"Font specified: {args.font}")
    else:
        print("No font specified.")




if __name__ == "__main__":
    main()
