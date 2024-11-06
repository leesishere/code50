x, y, z = input("Expression: ").split(' ')


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

