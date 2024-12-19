import sys
import os

def main(file_path):
    print(file_exists(file_path))



def file_exists(file_path):
    # Check if the file exists
    if os.path.isfile(file_path):
        return True
    else:
        return False


if __name__ == "__main__":
    main(sys.argv[1])
