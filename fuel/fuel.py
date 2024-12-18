
def main():
    while True:
        fract = input("Fraction: ")
        fract = convert(fract)
        print(fract)
        if type(fract) == type(1.0):
            percentage = gauge(fract)
            if is_percentage(percentage) or ('E' in percentage or 'F' in percentage):
                print_string = percentage
                break
    print(f"{print_string}")

def gauge(percentage):
    percentage = percentage * 100
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
    try:
        numerator = is_int(numerator)
        denominator = is_int(denominator)
    except ValueError as e:
        print(e) # Output

    return round(float(numerator/denominator),2)



def is_int(s):
    if not s.isdigit():
        print("howdy")
        raise ValueError(f"Cannot convert '{s}' to an integer")
    return int(s)

def is_percentage(s):
    # Check if the string ends with '%'
    if s.endswith('%'):
        # Remove the '%' sign and check if the remaining part is a digit
        number_part = s[:-1]
        return number_part.replace('.', '', 1).isdigit()
    return False


if __name__ == "__main__":
    main()
