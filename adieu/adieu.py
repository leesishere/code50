
def main():
    name_list = []
    try:
        while True:
            user_input = input("Name: ").strip()
            if not user_input:
                raise EOFError()
            name_list.append(user_input)
    except EOFError:
        # make sure the user entered a name not a space or blank
        name_list = [name for name in name_list if name]
        print()
        print("Adieu, adieu, to ",end='')
        for name in name_list[0:-1]:
            print(name + ", ", end='')
        if len(name_list) > 1:
            print("and", name_list[-1])
        else:
            print(name_list[-1])


if __name__ == "__main__":
    main()
