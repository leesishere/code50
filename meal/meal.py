######################
# Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00,
# and dinner between 18:00 and 19:00. Wouldn’t it be nice if you had a program that could tell you what to eat when?
######################


def main():
    time = input("What time is it? ").lower().strip()
    hour, min = convert(time)
    if hour in [7,8]:

    print(hour)
    print(min)
    #breakfast time
    #lunch time



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

