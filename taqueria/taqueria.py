import keyboard

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
    print(menu)
    # Register the hotkey for macOS ('cmd' for Command key, 'd' for D key)
    keyboard.add_hotkey('cmd+d', on_command_d)

    # Block the program to keep it running and listen for events
    keyboard.wait()


def on_command_d():
    print("Command-D keys were pressed.")







if __name__ == "__main__":
    main()
