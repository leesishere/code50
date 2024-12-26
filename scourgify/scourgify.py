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
        if not csv_extension(sys.argv[2]):
            print("Not a CSV file")
            sys.exit(1)

    # Define the CSV file path
    csv_in_file_path = sys.argv[1]
    csv_out_file_path = sys.argv[2]

    # Read the CSV file into a list of dictionaries
    data = []
    try:
        with open(csv_in_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                last_name, first_name = row['name'].split(",")
                row = {'first': first_name,'last': last_name,'house' : row['house'] }
                #print(f"{first_name} {last_name}")
                data.append(row)
        fieldnames = ["first", "last", "house"]
        # Write the list of dictionaries to another CSV file
        with open(csv_out_file_path, 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    except FileNotFoundError:
        print(f"The file {csv_file_path} does not exist.")
        sys.exit(1)
        data = []
'''
    # Use tabulate to format the data into a table
    if data:
        # New field names (must match the number of existing field names)
        fieldnames = ["first", "last", "house"]
        table = tabulate(data, headers="keys", tablefmt="grid")
        # print("Formatted Table:")
        print(table)
    else:
        print("No data to display.")
        sys.exit(1)
'''

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

def csv_extension(file_path):
    file_extension = os.path.splitext(file_path)[1]
    if file_extension == '.csv':
        return True
    else:
        return False

if __name__ == "__main__":
      main()
