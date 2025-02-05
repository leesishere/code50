from datetime import date, timedelta
import inflect
import sys

p = inflect.engine()

def main():
    #response = input("Date of Birth: ")
    #if ':' in response:
    #    birthday, today = response.split(':')
    #    year, month, day = str(today).split("-")
    #    today = date(int(year), int(month), int(day))
    #    print(get_minutes(birthday, today))

    #else:
    #    print(get_minutes(response))
    print(get_minutes(input("Date of Birth: ")))


def get_minutes(date_input):
#def get_minutes(date_input, today_date=date.today()):
    today_date=date.today()
    try:
        year, month, day = str(date_input).split("-")
        birth_date = date(int(year), int(month), int(day))
        date_difference = date.__sub__(today_date, birth_date)
        seconds = int(date_difference.total_seconds()/60)
        in_words = p.number_to_words(seconds)
        in_words = in_words.capitalize()

        return f"{in_words.replace(" and "," ")} minutes"

    except ValueError:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()

