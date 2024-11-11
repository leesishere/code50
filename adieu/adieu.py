
def main():
    name_list = []
    try:
        while True:
            user_input = input("Name: ")
            name_list.append(user_input)
    except EOFError:
        print("Adieu, adieu, to ",end='')
        for name in name_list[0:-1]:
            print(name + ", ", end='')
        if len(name_list) > 1:
            print("and", name_list[-1])
        else:
            print(name_list[-1])


if __name__ == "__main__":
    main()
