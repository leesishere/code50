def main():
    greating = input("Greating: ").lower().strip()


def value(greeting):
    if 'hello' == greating[:5]:
        return 0
    elif 'h' == greating[0]:
        return 20
    else:
        print("$100")
        return 100


if __name__ == "__main__":
    main()
