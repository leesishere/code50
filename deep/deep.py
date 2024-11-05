###################
# In deep.py, implement a program that prompts the user for the answer to the
# Great Question of Life, the Universe and Everything,
# outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
###################

answer = ["42","forty-two","forty two"]

input_answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

if input_answer in answer:
    print("Yes")
else:
    print("No")
