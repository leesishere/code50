x, y, z = input("Expression: ").split(' ')


def classify_math(x,y,z):
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

