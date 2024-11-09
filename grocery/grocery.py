
def main():
    grocery_list =[ ]

    while True:
        try:
            item = input().lower().title().strip()
            grocery_list.append(item)
        except EOFError:
            print()
            grocery_list = sorted(grocery_list)
            previous = ''
            for item in grocery_list:
                count = sum(1 for x in grocery_list if item == x )
                if previous.upper() != item.upper():
                    print(f"{count} {item.upper()}")

                previous = item.upper()
            exit()
        except Exception:
            pass





if __name__ == "__main__":
    main()
