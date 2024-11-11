import random


def main():


def get_level():
    while not (input_level := input("Level: ").strip()).isdigit() or not (1 <= int(input_level) <= 3): pass
    return input_level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    if level == 2:
        return random.randint(10, 19)
    if level == 3:
        return random.randint(20, 29)

if __name__ == "__main__":
    main()
