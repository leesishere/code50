def main():
    x, y, z = input("Expression: ").split(' ')
    print(math_it(int(x),y,int(z)))

def math_it(x,y,z) -> float:
    match y:
        case '+':
            return x + z
        case '-':
            return x - z
        case '*':
            return x * z
        case '/':
            return x / z
        case _:
            return "Other number"

main()
