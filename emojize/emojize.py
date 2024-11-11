import sys
sys.path.append('.')

from emoji import emoji_dict
emoji = emoji_dict
print(emoji[':1st_place_medal:'])

def main():
    input_emoji = input("Input").lower().strip()



if __name__ == "__main__":
    main()
