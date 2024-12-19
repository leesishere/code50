import sys
import os

def main():
    file_path = check_arguments(sys.argv)
    print(file_exists(file_path))


def check_arguments(params):
    print(params)
    if len(params) == 2:
        print("Too few command-line arguments")
        sys.exit()
    if len(params) > 3:
        print("Too many command-line arguments")
        sys.exit()
    else:
        return params[1]

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

