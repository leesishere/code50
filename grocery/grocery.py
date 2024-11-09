
def main:
    grocery_list =[ ]

    while True:
        try:
            item = input().lower().title().strip()
            
        except EOFError:
            # needed to add the final total to get the test script to pass the code :-(
            print(f"${total:.2f}")
            exit()
        except Exception:
            pass





if __name__ == "__main__":
    main()
