import csv
from tabulate import tabulate
import sys, os

def main():
    # csv checks
    if not check_arguments(sys.argv):
        if len(sys.argv) < 3:
            print("Too few command-line arguments")
            sys.exit(1)
        if len(sys.argv) > 3:
            print("Too many command-line arguments")
            sys.exit(1)
    else:
        if not jpg_extension(sys.argv[1]):
            print("Input and output have different extensions")
            sys.exit(1)
        if not jpg_extension(sys.argv[2]):
            print("Invalid output")
            sys.exit(1)


def check_arguments(params):
    if len(params) == 3:
        return True
    else:
        return False

def file_exists(file_path):
    # Check if the file exists
    if os.path.isfile(file_path):
        return True
    else:
        return False

def jpg_extension(file_path):
    file_extension = os.path.splitext(file_path)[1]
    if file_extension == '.jpg':
        return True
    else:
        return False

if __name__ == "__main__":
      main()
