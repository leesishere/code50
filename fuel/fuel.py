
def main():
    while True:
        fract = input("Fraction: ")
        fract = convert_fraction(fract)
        if type(fract) == type(1.0):
            percentage = fract * 100
            if percentage < 2:
                print_string = f"E"
            elif percentage > 89:
                print_string = f"F"
            else:
                percentage = int(percentage)
                print_string = f"{percentage}%"
            break
    print(f"{print_string}")

def convert_fraction(f):
    f = f.replace(" ", "")
    try:
        numerator, denominator = f.split('/')
        numerator = int(numerator)
        denominator = int(denominator)
        # force error if numarator is more than denominator
        if numerator > denominator:
            denominator = 0
        return float(numerator/denominator)
    except ValueError:
        pass
    except ZeroDivisionError:
        pass


if __name__ == "__main__":
    main()
