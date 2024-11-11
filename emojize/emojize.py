import re
import sys
sys.path.append('.')

from emoji import emoji_dict
emoji = emoji_dict


def main():
    while True:
        input_emoji = input("Input: ").lower().strip()
        pattern = r'\b(\w*) (:\w*:)\b'
        match = re.search(pattern, input_emoji)

        try:
            message = match.group(1)
            input_emoji = match.group(2)
            print(message)
            if message:
                print(f"Output: {message} {emoji[input_emoji]}")
            else:
                print(f"Output: {emoji[input_emoji]}")
            break
        except:
            pass



if __name__ == "__main__":
    main()
