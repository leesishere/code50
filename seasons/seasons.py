import sys
sys.path.append('/workspaces/21178063/seasons/')
import math
from num2words import num2words
from datetime import date


def main():
    print(age_in_minutes(input("Date of borth (YYYY-MM-DD):  ")))


def age_in_minutes(s='2000-01-01'):
    try:
        age = date.today() - date.fromisoformat(s)
        # Get the total minutes
        minutes = age.total_seconds() / 60
        return num2words(math.ceil(minutes))
    except ValueError:
        print("Invalid Date")

if __name__ == "__main__":
    main()
