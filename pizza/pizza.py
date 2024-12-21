def main():

    if csv_file(sys.argv):




def csv_file(argv):
    if len(params) == 1:
        print("Too few command-line arguments")
        sys.exit(1)
    if len(params) > 2:
        print("Too many command-line arguments")
        sys.exit(1)

   if not check_arguments(argv):
        sys.exit(1)
    else:
        #check passed file exists and is csv file
        if not file_exists(arg[1]):
            sys.exit(1)
        if not csv_extension(arg[1]):
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
