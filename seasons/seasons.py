import sys
sys.path.append('/workspaces/21178063/seasons/')
from datetime import date


def main():
    print(age_in_minutes(input("Date of borth (YYYY-MM-DD):  ")))


def age_in_minutes(s):
    age = date.today() - date.fromisoformat(s)
    # Get the total minutes
    minutes = age.total_seconds() / 60
    return minutes


if __name__ == "__main__":
    main()
