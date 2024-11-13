import random

def main():
    level = get_level()
    number_of_math_problems = 10
    count_wrong_answer = 0
    while number_of_math_problems > 0:
        first_digit = generate_integer(level)
        second_digit = generate_integer(level)
        answer = first_digit + second_digit
        print(f"{first_digit} + {second_digit} = ", end='')

        while True
            input_reponse = input().strip()
            if input_reponse == str(answer):
                number_of_math_problems -= 1
                break
            elif(count_wrong_answer > 3):
                print(f"{first_digit} + {second_digit} = {answer}")
                break
            else:
                print("EEE")
                count_wrong_answer += 1


def get_level():
    while not (input_level := input("Level: ").strip()).isdigit() or not (1 <= int(input_level) <= 3): pass
    return int(input_level)


def generate_integer(level):
    if level == 1:
        return int(random.randint(0, 9))
    if level == 2:
        return int(random.randint(10, 19))
    if level == 3:
        return int(random.randint(20, 29))

if __name__ == "__main__":
    main()
