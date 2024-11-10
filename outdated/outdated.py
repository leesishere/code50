import re

def main():
    month_list = {
            "January":1,
            "February":2,
            "March":3,
            "April":4,
            "May":5,
            "June":6,
            "July":7,
            "August":8,
            "September":9,
            "October":10,
            "November":11,
            "December":12
    }

    # accept September 8, 1636 or 9/8/1636 and return 1636-9-8
    # Then output that same date in YYYY-MM-DD format.
    # If the user’s input is not a valid date in either format, prompt the user again.
    # Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.

    date = input("Date: ").strip()

    # Define regex patterns for both date formats
    pattern1 = r'\b(\d{1,2})/(\d{1,2})/(\d{4})\b'  # Pattern for ##/##/####
    pattern2 = r'\b(\w+) (\d{1,2}), (\d{4})\b'  # Pattern for AAAA #, ####

    pattern = r'\b(\d{1,2})/(\d{1,2})/(\d{4})\b|\b(\w+) (\d{1,2}), (\d{4})\b'  # Pattern for ##/##/####

    match = re.search(pattern, date)
    if match:
        month = match.group(1)
        day = match.group(2)
        year = match.group(3)
        # assign month name to month number

        print(month)
        exit()
        if not month.isdigit():
            month = month_list[month.title()]
        month = str(month).zfill(2)
        day = str(day).zfill(2)
        print(f"{year}-{month}-{day}")
'''
    # Find all matches for both patterns
    match1 = re.search(pattern1, date)
    match2 = re.search(pattern2, date)

    #Dates in format ##/##/##
    if match1:
        month = match1.group(1)
        day = match1.group(2)
        year = match1.group(3)
        # print YYYY-MM-DD format
        if len(str(month).zfill(2)) == 2:
            month = '0' + str(month)
        if len(str(day).zfill(2)) == 2:
            day = '0' + str(day)
        print(f"{year}-{month}-{day}")

    #Dates in format Month_Name #, ####
    if match2:
        month = match2.group(1)
        day = match2.group(2)
        year = match2.group(3)
        # assign month name to month number
        month = month_list[month.title()]
        month = str(month).zfill(2)
        day = str(day).zfill(2)
        print(f"{year}-{month}-{day}")
'''


if __name__ == "__main__":
    main()


