import re
import sys

def main():
    print(convert(input("Hours: ")))
    exit(0)

#  9:00 AM to 5:00 PM
#  9 AM to 5 PM
#  9:00 AM to 5 PM
#  9 AM to 5:00 PM


def convert(s):
    if " to " not in s:
        raise ValueError("Invalid time range format")

    # Continue with your conversion logic
    s = s.strip()
    pattern = r'^(1[0-2]|0?[1-9]):?([0-5][0-9])? ([AaPp][Mm])\s+[Tt][Oo]\s+(1[0-2]|0?[1-9]):?([0-5][0-9])? ([AaPp][Mm])$'

    match = re.search(pattern, s)

    try:
        if match:
            start_hour = match.group(1)
            start_minute = match.group(2) if match.group(2) else '00'
            start_period = match.group(3).upper()
            end_hour = match.group(4)
            end_minute = match.group(5) if match.group(5) else '00'
            end_period = match.group(6).upper()

            try:
                if not (0 <= int(start_hour) <= 12 and 0 <= int(start_minute) < 60):
                    raise ValueError("Invalid time range format")
                if not (0 <= int(end_hour) <= 12 and 0 <= int(end_minute) < 60):
                    raise ValueError("Invalid time range format")
            except ValueError:
                raise ValueError("Invalid time range format")

            if start_period == 'AM':
                if int(start_hour) == 12:
                    start_hour = '00'

            if start_period == 'PM':
                if int(start_hour) != 12:
                    start_hour = int(start_hour) + 12

            if end_period == 'AM':
                if int(end_hour) == 12:
                    end_hour = '00'

            if end_period == 'PM':
                if int(end_hour) != 12:
                    end_hour = int(end_hour) + 12

            start_time = f"{str(start_hour).zfill(2)}:{start_minute}"
            end_time = f"{str(end_hour).zfill(2)}:{end_minute}"

            return f"{start_time} to {end_time}"
        else:
            raise ValueError("Invalid time range format")
    except ValueError:
        raise ValueError("Invalid time range format")

if __name__ == "__main__":
    main()
