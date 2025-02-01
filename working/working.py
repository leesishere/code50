import re
import sys


def main():
    print(convert(input("Hours: ")))


#  9:00 AM to 5:00 PM
#  9 AM to 5 PM
#  9:00 AM to 5 PM
#  9 AM to 5:00 PM

def convert(s):
    s = s.strip()
    pattern = r'^(1[0-2]|0?[1-9]):?([0-5][0-9])? ?([AaPp][Mm])\s+[Tt][Oo]\s+(1[0-2]|0?[1-9]):?([0-5][0-9])? ?([AaPp][Mm])$'
    pattern = r'(1[0-2]|0?[1-9]):?([0-5][0-9])? ?([AaPp][Mm])\s[Tt][Oo]\s(1[0-2]|0?[1-9]):?([0-5][0-9])? ?([AaPp][Mm])'

    #pattern = r'http(?:s):\/\/(?:www\.)?youtube\.com\/(?:embed/)?'
    match = re.search(pattern, s)

    try:
        firstHour = match.group(1)
        firstMinute = match.group(2)
        firstMeridieme = match.group(3)
        secondHour = match.group(4)
        secondMinute = match.group(5)
        secondMeridieme = match.group(6)
        print(f"{firstHour} \n {firstMinute} \n{firstMeridieme}")
        print(f"{secondHour} {secondMinute} {secondMeridieme}")
    except:
        pass

if value < 0:
    raise ValueError("The value cannot be negative.")



if __name__ == "__main__":
    main()
