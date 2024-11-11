import sys
sys.path.append('.')

from emoji import emoji_dict
emoji = emoji_dict


def main():
    while True:
        input_emoji = input("Input: ").lower().strip()
        try:
            print(f"Output: {emoji[input_emoji]}")
            break
        except:
            pass



if __name__ == "__main__":
    main()
