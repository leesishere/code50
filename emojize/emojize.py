import sys
sys.path.append('.')

from emoji import emoji_dict
emoji = emoji_dict

def main():
    if isinstance(emoji, set):
        print("It's a set!")
        print(emoji[':1st_place_medal:'])



if __name__ == "__main__":
    main()
