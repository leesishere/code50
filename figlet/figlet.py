import argparse

def main():
    parser = argparse.ArgumentParser(description='Process some arguments.')
    parser.add_argument('-f', '--font', type=str, help='Specify the font name')
    args = parser.parse_args()

    if args.font:
        print(f"Font specified: {args.font}")
    #else:
    #    ys.exit("Exiting the program due to an error.")




if __name__ == "__main__":
    main()
