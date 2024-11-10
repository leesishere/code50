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
    pattern1 = r'\b\s*(\d{1,2})\s*/\s*(\d{1,2})\s*/\s*(\d{4})\s*\b'  # Pattern for ##/##/####
    pattern2 = r'\b\s*(\w+)\s*(\d{1,2})\s*,\s*(\d{4})\s*\b'  # Pattern for AAAA #, ####

    # Find all matches for both patterns
    match1 = re.search(pattern1, date)
    match2 = re.search(pattern2, date)

    #Dates in format ##/##/##
    if match1 and not convert_date(match1, month_list):
        print(f"{convert_date(match1, month_list)}")

    #Dates in format Month_Name #, ####
    if match2 and not convert_date(match2, month_list):
        print(f"{convert_date(match2, month_list)}")

def convert_date(match,month_list):
        month = match.group(1)
        day = match.group(2)
        year = match.group(3)

        if day > 30:
            return False

        if not month.isdigit():
            month = month_list[month.title()] # assign month name to month number

        # create leading zero if needed
        month = str(month).zfill(2)
        day = str(day).zfill(2)

        # print YYYY-MM-DD format
        return f"{year}-{month}-{day}"


if __name__ == "__main__":
    main()


