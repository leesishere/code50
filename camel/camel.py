
def main():
    camelCase = input("camelCase: ")
    snake_case = convert(camelCase)

def convert(camelCase):
    for i in range(len(camelCase)):
        print(camelCase[i].isupper())

if __name__ == "__main__":
    main()
