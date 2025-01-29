import re
import sys
from ipaddress import ip_address

# IP address
# ###.###.###.### But each # should be a number between 0 and 255,

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):



def validIP(IP: str) -> str:
    try:
        ip = ip_address(IP)
        return "IPv4" if ip.version == 4 else "IPv6"
    except ValueError:
        return "Invalid"


if __name__ == "__main__":
    main()
