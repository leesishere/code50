import sys
import os

def main(file_path):
    print(file_path)


    # Check if the file exists
   
    if os.path.isfile(file_path):
        print("File exists")
    else:
        print("File does not exist")



if __name__ == "__main__":
    main(sys.argv[1:])
