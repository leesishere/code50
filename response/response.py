import sys
sys.path.append('/workspaces/21178063/response')
import validators

def main():
    if validators.email(input("What's your e-mail address? ")):
        print('Valid')
    else:
        print('Invalid')

if __name__ == "__main__":
    main()
