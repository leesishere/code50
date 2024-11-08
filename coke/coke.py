# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins
# in these denominations: 25 cents, 10 cents, and 5 cents.
#
# Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
# Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
import re

text = "abc123def456ghi789..."


def main():
    amount = 50
    while amount > 0:
        try:
            coin = input("Insert Coin: ")
            coin = int(coin)
        except:
            # Define the pattern to split by digits and non-digits
            #pattern = r'(\d+|\D+)'
            #parts = re.findall(pattern, coin)
            #amount -= int(parts[0])
            #print(f"Amount Due: {amount}{parts[1]}")
            continue
        amount -= coin
        if amount > 0:
            print(f"Amount Due: {amount}")

    print("Change Owed:", abs(amount))


if __name__ == "__main__":
    main()
