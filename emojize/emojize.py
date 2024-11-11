import sys
sys.path.append('.')

from emoji import emoji_dict
emoji = emoji_dict


def main():
    while True:
        input_emoji = input("Input: ").lower().strip().split()

        print(input_emoji)
        exit()

        try:
            if len(message) == 2:
                print(f"Output: {message[0]} {emoji[message[1]]}")
                break
            else:
                print(f"Output: {emoji[message[0]]}")
                break
        except:
            pass



if __name__ == "__main__":
    main()
