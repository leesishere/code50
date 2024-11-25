import sys
import pytest
sys.path.append('/workspaces/21178063/bank')

from bank import value


def test_shorten():
    assert value("Jamey") == 0

def main():
    greeting = input("Greating: ").lower().strip()
    pay_up = value(greeting)

    if pay_up == 0:
        print("$0")
    elif pay_up == 20:
        print("$20")
    elif pay_up == 100:
        print("$100")

def value(greeting):
    if 'hello' == greeting[:5]:
        return 0
    elif 'h' == greeting[0]:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
