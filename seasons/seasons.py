import sys
import os
import math
from datetime import date
import num2words
import inflect

p = inflect.engine()
# Corrected path appending:
sys.path.append(os.path.abspath('/workspaces/21178063/seasons'))

class Minutes:
    def __init__(self, birthday: str):
        self.birthday = birthday

    @property
    def today(self) -> date:
        #return date.fromisoformat('2000-01-01')
        return date.today()

    @property
    def birthday(self) -> date:
        return self._birthday

    @birthday.setter
    def birthday(self, s: str):
        try:
            self._birthday = date.fromisoformat(s)
        except ValueError:
            sys.exit("Invalid Date")

    def say_age_in_minutes(self):
        try:
            date_difference = date.__sub__(self.today, self.birthday)
            minutes = int(date_difference.total_seconds()/60)
            #age = self.today - self.birthday
            #minutes = age.total_seconds() / 60

            #words = num2words.num2words(math.ceil(minutes))
            #words_no_and = words.replace(" and", "")
            #return f"{words_no_and.capitalize()} minutes"

            print(f"{p.number_to_words(math.ceil(minutes), andword="").capitalize()} minutes")

        except ValueError:
            sys.exit("Invalid Date")

def print_say_age_in_minutes(birthday):
    mydate = Minutes(birthday)
    mydate.say_age_in_minutes()

def get_birthday():
    # expect (YYYY-MM-DD)
    return input("Date of Birth: ")

# ignoramus code
def main():
    print(get_minutes(input("Date of Birth: ")))

def get_minutes(date_input):
    today_date = date.today()

    try:
        year, month, day = str(date_input).split("-")
        birth_date = date(int(year), int(month), int(day))
        date_difference = today_date - birth_date
        #date_difference = date.__sub__(today_date, birth_date)
        seconds = int(date_difference.total_seconds()/60)
        words = p.number_to_words(seconds)
        words = words.capitalize()

        return f"{words.replace(" and "," ")} minutes"

    except ValueError:
        sys.exit("Invalid date")

# The cs50 check50 v3.3.11 does not like having this code in a class :-(
#def main():
#    birthday = get_birthday()
#    print_say_age_in_minutes(birthday)


if __name__ == "__main__":
    main()
