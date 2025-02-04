from datetime import date, timedelta
import inflect
import sys

p = inflect.engine()

def main():
    print(get_minutes(input("Date of Birth: ")))

def get_minutes(date_input):
    today_date = date.today()

    try:
        year, month, day = str(date_input).split("-")
        birth_date = date(int(year), int(month), int(day))
        date_difference = date.__sub__(today_date, birth_date)
        seconds = int(date_difference.total_seconds()/60)
        words = p.number_to_words(seconds)
        words = words.capitalize()

        return f"{words.replace(" and "," ")} minutes"

    except ValueError:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()
