import random


def main():
    

def get_level():
    while not (input_level := input("Level: ").strip()).isdigit() or not (1 <= int(input_level) <= 3): pass
    return input_level



def generate_integer(level):
    ...


if __name__ == "__main__":
    main()
