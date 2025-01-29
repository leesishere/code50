import re
import sys
from ipaddress import ip_address

# IP address
# ###.###.###.### But each # should be a number between 0 and 255,

def main():
    print(validate(input("IPv4 Address: ")))


def validate(IP: str) -> str:
    try:
        ip = ip_address(IP)
        if ip.version == 4:
            return True
        else:
            return False
    except ValueError:
        return "Invalid"


if __name__ == "__main__":
    main()
