def main():
    x, y, z = input("Expression: ").split(' ')
    print(math_it(float(x),y,float(z)))

def math_it(x,y,z) -> float:

    match y:
        case '+':
            return x + z
        case '-':
            return x - z
        case '*':
            return x * z
        case '/':
            if z != 0:
                return x / z
        case _:
            return "Other number"

main()
