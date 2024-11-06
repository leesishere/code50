######################
# Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00,
# and dinner between 18:00 and 19:00. Wouldn’t it be nice if you had a program that could tell you what to eat when?
######################


def main():
    time = input("What time is it? ").lower().strip()
    hour, min = convert(time)
    print("breakfast time") if hour == 7 or (hour == 8 and min == 00)
    print("lunch time") if hour == 12 or (hour == 13 and min == 00)
    print("dinner time") if hour == 18 or (hour == 19 and min == 00)


def convert(time):
    hour, min = time.split(':')
    if 'a.m.' in min:
        min = min.replace('a.m.', '').strip()
        min = int(min)
        hour = int(hour)
        if hour > 12:
            hour -= 12
    if 'p.m.' in min:
        min = min.replace('p.m.', '').strip()
        min = int(min)
        hour = int(hour) + 12
    return hour, min

if __name__ == "__main__":
    main()

