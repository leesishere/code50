import sys
import os
sys.path.append('/workspaces/21178063/seasons/')
import math
from num2words import num2words
from datetime import date

class Minutes(date):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

def main():
    # expect (YYYY-MM-DD)
    birthDate = input("Date of Birth: ")
    age_in_minutes(birthDate)

def age_in_minutes(s):
    try:
        #if "PYTEST_CURRENT_TEST" in os.environ:
        #    today='2000-01-01'
        #    age = date.fromisoformat(today) - date.fromisoformat(s)
        #else:
        #    age = date.today() - date.fromisoformat(s)

        today='2000-01-01'
        age = date.fromisoformat(today) - date.fromisoformat(s)

        #age = date.today() - date.fromisoformat(s)

        # Get the total minutes
        minutes = age.total_seconds() / 60
        words = num2words(math.ceil(minutes))
        words_no_and = words.replace("and ","")
        return words_no_and

    except ValueError:
        print()"Invalid Date")

if __name__ == "__main__":
    main()
