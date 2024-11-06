import re
######################
# Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00,
# and dinner between 18:00 and 19:00. Wouldn’t it be nice if you had a program that could tell you what to eat when?
######################


def main():
    time = input("What time is it? ").lower().strip()
    hour, min = convert(time)
    print("breakfast time") if hour == 7 or (hour == 8 and min == 00) else None
    print("lunch time") if hour == 12 or (hour == 13 and min == 00) else None
    print("dinner time") if hour == 18 or (hour == 19 and min == 00) else None

def am(s):
    # ante meridiem (am)
    ante = r'\b(a\.m\.|am)\b'
    return re.search(ante, s, re.IGNORECASE)

def pm(s):
    # post meridiem (pm)
    post = r'\b(p\.m\.|pm)\b'
    return re.search(post, s, re.IGNORECASE)


def convert(time):
    time_list = time.strip().split()
    # check if there is a . or : to find hour and minute...
    if len(time_list) > 1:
        if pm(time_list[-1]):

    exit()
    if ':' in time:
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
        #if type(float(time)) == type(1.0):
        #    hour, min = time.split('.')
        #    hour = int(hour)
        #    min = int(min) * 60
    return int(hour), int(min)

if __name__ == "__main__":
    main()

