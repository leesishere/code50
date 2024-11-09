
def main():
    while True:
        fract = input("Fraction: ")
        if type(fract) == type(1.0):
            percentage = fract * 100
            if percentage < 2:
                print_string = f"E"
            elif percentage > 89:
                print_string = f"F"
            else:
                print_string = f"{percentage}%"
            break
    print(f"{print_string}")

def convert_fraction(f):
    f = f.replace(" ", "")
    try:
        numerator, denominator = f.split('/')
        return float(umerator/denominator)
    except ValueError:
        pass








if __name__ == "__main__":
    main()
