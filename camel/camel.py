
def main():
    camelCase = input("camelCase: ")
    snake_case = convert(camelCase)

def convert(camelCase):
    snake_case = ''
    for i in range(len(camelCase)):
        if camelCase[i].isupper():
            snake_case = snake_case + '_' + camelCase[i].lower()
        else:
            snake_case = snake_case + camelCase[i]
    return snake_case

if __name__ == "__main__":
    main()
