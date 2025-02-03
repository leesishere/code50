import sys
import os
sys.path.append('/workspaces/21178063/seasons/')
import math
from num2words import num2words
from datetime import date

# ignoramus

class Minutes(date, num2words):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.birthday = birthday
class Minutes:
    def __init__(self, year, month, day, birthday):
        self.date = date(year, month, day)
        self.birthday
        
    def __str__(self):
        age = cls.today() - self.birthday
        # Get the total minutes
        minutes = age.total_seconds() / 60
        words = num2words(math.ceil(minutes))
        words_no_and = words.replace("and ","")
        return words_no_and

    @classmethod
    def minutes(self):
        date.fromisoformat(today) - self._birthday
        return cls.today()

    @property
    def birthday():
        return self._birthday

    @birthday.setter
    def birthday(s):
        try:
            self._birthday = cls.fromisoformat(s)
        except ValueError:
            print("Invalid Date")

def main():
    # expect (YYYY-MM-DD)
    birthday = input("Date of Birth: ")

    mydate = Minutes(birthday)
    print(mydate.today())

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
        print("Invalid Date")

if __name__ == "__main__":
    main()
