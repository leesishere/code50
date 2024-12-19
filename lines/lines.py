import sys
import os
import re
'''
This program counts all python code by:
    1. removing the blank lines
    2. removing # comments lines
    3. remvong DocString lines such as this one

'''
def main():
    file_path = check_arguments(sys.argv)
    if py_file_exists(file_path):
        count_code_lines(file_path)

def count_code_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read the entire content of the file
            content = file.read()
            print(f"{len(content.split("\n"))}")

            results = remove_blank_lines(remove_hash_comments(content))
            print(f"{len(results.split("\n"))}")


    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")



def remove_blank_lines(text):
    # Split the string into lines, filter out blank lines, and join the remaining lines
    return "\n".join([line for line in text.splitlines() if line.strip()])


def remove_hash_comments(text):
    # Define the pattern to match lines with whitespace followed by #
    pattern = r'^\s+#.*$'

    # Use re.sub() to remove matching lines
    result = re.sub(pattern, '', text, flags=re.MULTILINE)

    # Optionally, strip leading/trailing whitespace
    result = result.strip()

    return result

def check_arguments(params):
    if len(params) == 1:
        print("Too few command-line arguments")
        sys.exit(1)
    if len(params) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        return params[1]

def py_file_exists(file_path):
    # Check if the file extension is .py
    if not py_extension(file_path):
        print("Not a Python file")
        sys.exit(1)
    # Check if the file exists
    if os.path.isfile(file_path):
        return True
    else:
        print("File does not exist")
        sys.exit(1)

def py_extension(file_path):
    file_extension = os.path.splitext(file_path)[1]
    if file_extension == '.py':
        return True
    else:
        return False

if __name__ == "__main__":
      main()

