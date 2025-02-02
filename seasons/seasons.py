import sys
sys.path.append('/workspaces/21178063/seasons/')
import math
from num2words import num2words
from datetime import date


def main():
    print(age_in_minutes(input("Date of borth (YYYY-MM-DD):  ")))


def age_in_minutes(s):
    try:
        age = date.today() - date.fromisoformat(s)
        age = date.fromisoformat('2000-01-01') - date.fromisoformat(s)
    except:
        sys.exit("Invalid Date")
    # Get the total minutes
    minutes = age.total_seconds() / 60
        #29,092,320
    return num2words(math.ceil(minutes))


if __name__ == "__main__":
    main()
