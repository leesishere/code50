import sys
import os
from datetime import date

# Corrected path appending:
sys.path.append(os.path.abspath('/workspaces/21178063/seasons'))

import sys
import os
from datetime import date

# Corrected path appending:
sys.path.append(os.path.abspath('..'))

class Minutes:
    def __init__(self, birthday: str):
        self.birthday = date.fromisoformat(birthday)

    @property
    def today(self) -> date:
        return date.today()

    @property
    def birthday(self) -> date:
        return self._birthday

    @birthday.setter
    def birthday(self, s: str):
        try:
            # Corrected usage of date.fromisoformat()
            if not isinstance(s, str):  # Input must be a string
                raise TypeError("Invalid input. Please provide an ISO-formatted date.")
            self._birthday = date.fromisoformat(s)
        except ValueError as e:
            print(f"Invalid Date (Error): {e}")

    def say_age_in_minutes(birthday: str):
        try:
            # Corrected usage of date
            today = date.today()

            age = today - date.fromisoformat(birthday)

            minutes = age.total_seconds() / 60

            words = num2words(math.ceil(minutes))
            words_no_and = words.replace(" and", "")

            return words_no_and
        except ValueError as e:
            print(f"Invalid Date (Error): {e}")

def main():
    # expect (YYYY-MM-DD)
    birthday = input("Date of Birth: ")

    mydate = Minutes(birthday)

if __name__ == "__main__":
    main()
