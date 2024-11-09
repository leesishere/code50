import re

def main():
    [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

    # accept September 8, 1636 or 9/8/1636 and return 1636-9-8
    # Then output that same date in YYYY-MM-DD format.
    # If the user’s input is not a valid date in either format, prompt the user again.
    # Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.


    date = input("Date: ")

    # Define regex patterns for both date formats
    pattern1 = r'\b(\d{2})/(\d{2})/(\d{2})\b'  # Pattern for ##/##/##
    pattern2 = r'\b(\w+) (\d{1,2}), (\d{4})\b'  # Pattern for AAAA #, ####

    # Find all matches for both patterns
    dates1 = re.findall(pattern1, date)
    dates2 = re.findall(pattern2, date)

    # Print the results
    #Dates in format ##/##/##

    if dates1:
        print("Dates in format ##/##/##:", dates1)

    #Dates in format AAAA #, ####
    if dates2:
        # Find all matches
        matches = re.findall(pattern2, date)

        # Print the groups
        for match in matches:
            month, day, year = match
            print(f"Month: {month}, Day: {day}, Year: {year}")

        #print("Dates in format AAAA #, ####:", dates2)



if __name__ == "__main__":
    main()
