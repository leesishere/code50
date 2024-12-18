
def main():
    while True:
        fract = input("Fraction: ")
        fract = convert(fract)
        if type(fract) == type(1.0):
            percentage = gauge(percentage)


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
    retrun print_string
    
def convert(f):
    f = f.replace(" ", "")
    try:
        numerator, denominator = f.split('/')
        numerator = int(numerator)
        denominator = int(denominator)
        # force error if numarator is more than denominator
        if numerator > denominator:
            denominator = 0
            # round(denominator , 2)
        return round(float(numerator/denominator),2)
    except ValueError:
        pass
    except ZeroDivisionError:
        pass


if __name__ == "__main__":
    main()
