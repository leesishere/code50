import sys
import os

def main():
    print(file_exists(file_path))

def check_arguments():
    if len(sys.argv) == 2:
        print("Too few command-line arguments")
        sys.exit()
    elif: len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit()
    else:
        return True

def file_exists(file_path):
    # Check if the file extension is .py
    if not py_extension(file_path):
        return False
    # Check if the file exists
    if os.path.isfile(file_path):
        return True
    else:
        return False

def py_extension(file_path):
    file_extension = os.path.splitext(file_path)[1]
    if file_extension == '.py':
        return True
    else:
        return False

if __name__ == "__main__":
      main()
      check_arguments()
