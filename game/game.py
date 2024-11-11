import random

# Prompts the user for a level,
# If the user does not input a positive integer, the program should prompt again.
# Randomly generates an integer between 1 and inclusive, using the random module.
# Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
# If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
# If the guess is larger than that integer, the program should output Too large! and prompt the user again.
# If the guess is the same as that integer, the program should output Just right! and exit.

def main():

    while not (input_level := input("Level: ").strip()).isdigit(): pass
    print(input_level)
    random_integer = random.randint(2, input_level)
    Too small!
    Too large!
    Just right!
    guess = input("Guess: ")

if __name__ == "__main__":
    main()
