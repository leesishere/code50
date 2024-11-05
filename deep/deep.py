###################
# In deep.py, implement a program that prompts the user for the answer to the
# Great Question of Life, the Universe and Everything,
# outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
###################


def main():
    input_answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ").lower().strip()
    print(answer(input_answer))


def answer(r):
    match r:
        case "42" | "forty-two" | "forty two":
            return "Yes"
        case _:
            return "No"

def answer_two(a):
    answer = ["42","forty-two","forty two"]
    if a in answer:
        print("Yes")
    else:
        print("No")

main()
