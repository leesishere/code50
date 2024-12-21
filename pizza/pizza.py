def main():
    file_path = check_arguments(sys.argv)
    if not file_exists(file_path):
        sys.exit(1)


def check_arguments(params):
    if len(params) == 1:
        print("Too few command-line arguments")
        sys.exit(1)
    if len(params) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        return params[1]

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
