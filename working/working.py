import re
import sys


def main():
    print(convert(input("Hours: ")))


#  9:00 AM to 5:00 PM
#  9 AM to 5 PM
#  9:00 AM to 5 PM
#  9 AM to 5:00 PM

def convert(s):
    s = s.split()
    pattern = r'^(.+)[AM|PM]\sto\s'

    #pattern = r'http(?:s):\/\/(?:www\.)?youtube\.com\/(?:embed/)?'
    match = re.search(pattern, s)

if __name__ == "__main__":
    main()
