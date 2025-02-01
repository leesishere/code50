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
    pattern = r'^(\d{1,2}[:|])\s([AM|PM])\s+to\s+(.+)([AM|PM])$'

    #pattern = r'http(?:s):\/\/(?:www\.)?youtube\.com\/(?:embed/)?'
    match = re.search(pattern, s)
    print(match.group(1))


if __name__ == "__main__":
    main()
