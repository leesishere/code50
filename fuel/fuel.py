
def main():
    while True:
        fract = input("Fraction: ")
        if not convert(fract):
            continue
        else:
            fract = convert(fract)

        #if type(fract) == type(1.0):
        if type(fract) == type(1):
            percentage = gauge_(fract)
            if is_percentage(percentage) or ('E' in percentage or 'F' in percentage):
                print_string = percentage
                break
    if print_string:
        print(f"{print_string}")

def gauge(percentage):
    if percentage < 2:
        print_string = f"E"
    elif percentage > 89:
        print_string = f"F"
    else:
        percentage = int(percentage)
        print_string = f"{percentage}%"
    return print_string

def gauge_(percentage):
    if percentage < 2:
        print_string = f"E"
    elif percentage > 89:
        print_string = f"F"
    else:
        percentage = int(percentage)
        print_string = f"{percentage}%"
    return print_string


def convert(f):
    f = f.replace(" ", "")

    numerator, denominator = f.split('/')

    if is_int(numerator) and is_int(denominator):
        numerator = int(numerator)
        denominator = int(denominator)
    else:
        raise ValueError

    print(divide_(numerator, denominator))
    return divide_(numerator, denominator)


def is_percentage(s):
    # Check if the string ends with '%'
    if s.endswith('%'):
        # Remove the '%' sign and check if the remaining part is a digit
        number_part = s[:-1]
        return number_part.replace('.', '', 1).isdigit()
    return False

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return round(float(a/b),2)

def divide_(a, b):
    if b == 0:
        raise ZeroDivisionError
    return int(round(float(a/b),2) * 100)

def is_int(num):
    try:
        num = int(num)
    except:
        pass

    if type(num) == type(1):
        return True
    else:
        return False

if __name__ == "__main__":
    main()
