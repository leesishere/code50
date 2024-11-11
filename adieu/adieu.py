
def main():
    name_list = []
    try:
        while True:
            user_input = input("Name: ")
            name_list.append(user_input)
    except EOFError:
        print("Adieu, adieu, to ",end='')
        for name in name_list[1:-1]:
            print(name,end='')
        print()



if __name__ == "__main__":
    main()
