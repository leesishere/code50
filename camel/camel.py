
def main():
    camelCase = input("camelCase: ")

    snake_case = convert(camelCase)
    print(snake_case)

def convert(camelCase):
    snake_case = ''
    camelCase[0] = camelCase.lower() if camelCase[0].isupper() else camelCase[0]
    for i in range(len(camelCase)):
        #print(camelCase[i].isupper(), end='')
        if camelCase[i].isupper():
            snake_case = snake_case + '_' + camelCase[i].lower()
            #print(snake_case)
        else:
            snake_case = snake_case + camelCase[i]
    return snake_case

if __name__ == "__main__":
    main()
