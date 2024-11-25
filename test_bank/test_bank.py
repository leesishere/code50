def main():
    greating = input("Greating: ").lower().strip()
    pay_up = value(greeting)

    if pay_up == 0:
        print("$0")
    elif pay_up == 20:
        print("$20")
    elif pay_up == 100:
        print("$100")

def value(greeting):
    if 'hello' == greating[:5]:
        return 0
    elif 'h' == greating[0]:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
