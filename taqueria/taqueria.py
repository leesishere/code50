def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    total = 0.0

    while True:
        try:
            item = input("Item : ").lower().title()
            print(f"{item} = {menu[item]}")
            total += menu[item]
            print(f"Title : {total}")
        except EOFError:
            print()
            exit()
        except Exception:
            pass









if __name__ == "__main__":
    main()
