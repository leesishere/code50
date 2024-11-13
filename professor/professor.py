import random

def main():
    level = get_level()
    number_of_math_problems = 0
    count_wrong_answer = 0
    while number_of_math_problems < 10:
        first_digit = generate_integer(level)
        second_digit = generate_integer(level)
        answer = first_digit + second_digit
        print(f"{first_digit} + {second_digit} = ", end='')

        while True:
            input_reponse = input().strip()
            print(f"{input_reponse}")
            if input_reponse == str(answer):
                number_of_math_problems += 1
                count_wrong_answer = 0
                break
            elif(count_wrong_answer > 1):
                print(f"{first_digit} + {second_digit} = {answer}")
                break
            else:
                print("EEE")
                print(f"{first_digit} + {second_digit} = ", end='')
                count_wrong_answer += 1


def get_level():
    while not (input_level := input("Level: ").strip()).isdigit() or not (1 <= int(input_level) <= 3): pass
    return int(input_level)


def generate_integer(level):
    if level == 1:
        return int(random.randint(0, 9))
    if level == 2:
        return int(random.randint(10, 99))
    if level == 3:
        return int(random.randint(100, 999))

if __name__ == "__main__":
    main()
