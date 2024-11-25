def main():
    greating = input("Greating: ").lower().strip()
    if 'hello' == greating[:5]:
        print("$0")
    elif 'h' == greating[0]:
        print("$20")
    else:
        print("$100")

def value(greeting):
    ...


if __name__ == "__main__":
    main()
