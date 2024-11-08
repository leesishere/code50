
def main():
    camelCase = input("camelCase: ")
    snake_case = convert(camelCase)

def convert(camelCase):
    snake_case = ''
    for i in range(len(camelCase)):
        if camelCase[i].isupper()):
            snake_case = nake_case + '_' + camelCase[i].lower()
        else:
            snake_case = nake_case + camelCase[i]

if __name__ == "__main__":
    main()
