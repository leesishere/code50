#############################
# In a file called bank.py, implement a program that prompts the user for a greeting.
# If the greeting starts with “hello”, output $0.
# If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100.
# Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
#############################

def main():
    greeting = input("Greating: ").lower().strip()
    pay_up = value(greeting)

    if pay_up == 0:
        print("$0")
    elif pay_up == 20:
        print("$20")
    elif pay_up == 100:
        print("$100")

def value(greeting):
    if 'hello' == greeting[:5]:
        return 0
    elif 'h' == greeting[0]:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
