import sys
import os
from datetime import date

# Corrected path appending:
sys.path.append(os.path.abspath('/workspaces/21178063/seasons'))

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
            self._birthday = date.fromisoformat(s)
        except ValueError as e:
            print(f"Invalid Date (Error): {e}")

def main():
    # expect (YYYY-MM-DD)
    birthday = input("Date of Birth: ")

    mydate = Minutes(birthday)

if __name__ == "__main__":
    main()
