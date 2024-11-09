
def main():
    grocery_list =[ ]

    while True:
        try:
            item = input().lower().title().strip()
            grocery_list.append(item)
        except EOFError:
            grocery_list = sorted(grocery_list)
            for item in grocery_list:
                count = sum(1 for x in grocery_list if item == x )
                print(f"{count} {item}")
            exit()
        except Exception:
            pass





if __name__ == "__main__":
    main()
