def main():
    x, y, z = input("Expression: ").strip().split(' ')
    print(math_it(float(x),y,float(z)))

def math_it(x,y,z) -> float:

    match y:
        case '+':
            return round(x + z, 1)
        case '-':
            return round(x - z, 1)
        case '*':
            return round(x * z,1)
        case '/':
            if z != 0:
                return round(x / z,1)
        case _:
            return "Other number"

main()
