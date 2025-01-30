import re
import sys
from ipaddress import ip_address

# IP address
# ###.###.###.### But each # should be a number between 0 and 255,

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Define the pattern to match an IPv4 address
    pattern_IPv4 = r"\b^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\b(?!\.)"
    match = re.search(pattern_IPv4, ip)


    if match:
        # Get the number of groups
        num_groups = match.lastindex
        print("Number of groups:", num_groups)

        # Loop through the groups to validate 0-255
        for i in range(1, num_groups + 1):
            print(f"Group {i}: {match.group(i)}")
            if not (int(match.group(i)) >= 0 and int(match.group(i)) <= 255):
                return False
        return True

    else:
        # Does not match pattern of 127.0.0.1
        return False

'''
# To use the ipaddress package to validate if we have a IPv4
def validate(IP: str) -> str:
    try:
        ip = ip_address(IP)
        if ip.version == 4:
            return True
        else:
            return False
    except ValueError:
        return False
'''

if __name__ == "__main__":
    main()
