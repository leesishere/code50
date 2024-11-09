
def main:


    while True:
        try:
            item = input().lower().title().strip()
            total += menu[item]
            print(f"Total: ${total:.2f}")
        except EOFError:
            # needed to add the final total to get the test script to pass the code :-(
            print(f"${total:.2f}")
            exit()
        except Exception:
            pass





if __name__ == "__main__":
    main()
