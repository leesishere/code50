
def main:
    grocery_list =[ ]

    while True:
        try:
            item = input().lower().title().strip()
            grocery_list.append(item)
        except EOFError:
            
            exit()
        except Exception:
            pass





if __name__ == "__main__":
    main()
