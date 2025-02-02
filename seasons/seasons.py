import sys
sys.path.append('/workspaces/21178063/seasons/')
from datetime import date


def main():
    print(age_in_minutes(input("Date of borth (YYYY-MM-DD):  ")))


def age_in_minutes(s):
 return date.fromisoformat(s)
 #return date.today()

# Calculate the difference
difference = date2 - date1

# Get the total minutes
minutes = difference.total_seconds() / 60

print(f"Minutes between dates: {minutes}")

if __name__ == "__main__":
    main()
