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
        if not csv_extension(sys.argv[1]):
            print("Not a CSV file")
            sys.exit(1)

    # Define the CSV file path
    csv_file_path = sys.argv[1]

    # Read the CSV file into a list of dictionaries
    data = []
    try:
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"The file {csv_file_path} does not exist.")
        sys.exit(1)
        data = []

    # Use tabulate to format the data into a table
    if data:
        table = tabulate(data, headers="keys", tablefmt="grid")
        # print("Formatted Table:")
        print(table)
    else:
        print("No data to display.")
        sys.exit(1)


def check_arguments(params):
    if len(params) == 2:
        return True
    else:
        return False

def file_exists(file_path):
    # Check if the file exists
    if os.path.isfile(file_path):
        return True
    else:
        return False

def csv_extension(file_path):
    file_extension = os.path.splitext(file_path)[1]
    if file_extension == '.csv':
        return True
    else:
        return False

if __name__ == "__main__":
      main()
