# Adieu, adieu, to Liesl and Friedrich

def main():
    name_list = []
    try:
        while True:
            user_input = input("Name: ").strip()
            name_list.append(user_input)

    except EOFError:
        if name_list[-1] != '':
            print()

        # make sure the user entered a name not a space or blank
        name_list = [name for name in name_list if name]
        print("Adieu, adieu, to ",end='')
        if len(name_list) == 1:
            print(name_list[-1])
        elif len(name_list) == 2:
            print(f"{name_list[0]} and {name_list[1]}")
        elif len(name_list) > 2:
            for name in name_list[0:-1]:
                print(name + ", ", end='')
            print("and", name_list[-1])


if __name__ == "__main__":
    main()
