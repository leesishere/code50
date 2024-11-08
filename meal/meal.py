import re
######################
# Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00,
# and dinner between 18:00 and 19:00. Wouldn’t it be nice if you had a program that could tell you what to eat when?
######################


def main():
    time = input("What time is it? ").lower().strip()
    if am(time) or pm(time):
        time = extra_challenge(time)
    else:
        time = convert(time)
        
    print("breakfast time") if time >= 7 and time <= 8 else None
    print("lunch time") if time >= 12 and time <= 13  else None
    print("dinner time") if time >= 18 and time <= 19  else None


def am(s):
    # ante meridiem (am)
    ante = r'(a\.m\.|am)'
    return re.search(ante, s, re.IGNORECASE)

def pm(s):
    # post meridiem (pm)
    post = r'(p\.m\.|pm)'
    return re.search(post, s, re.IGNORECASE)

def convert(time):
    hour, min = time.split(':')
    min = int(min)/60
    time = int(hour) + min
    return time

 #:## a.m. ##:## a.m.
def extra_challenge(time):
    time, am_pm = time.split()
    time = convert(time)
    if pm(am_pm):
        if time < 12:
            time *= 12
    return time

if __name__ == "__main__":
    main()

