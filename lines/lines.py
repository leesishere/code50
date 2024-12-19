import sys
import os
import re

def main():
    file_path = check_arguments(sys.argv)
    if py_file_exists(file_path):
        count_code_lines(file_path)

def count_code_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read the entire content of the file
            content = file.read()
            print("File content:")
            #print(content)
            line_count = content.split("\n")
            print(len(line_count))
            print("*" * 10)
            results_count = remove_hash_comments(content).split("\n")
            print(len(results_count))

    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")

def remove_hash_comments_blank_lines(text):
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

