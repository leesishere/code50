
def main():



def convert_fraction(f):
    f = f.replace(" ", "")

    while True:
        try:
            numerator, denominator = f.split('/')
            return float(umerator/denominator)
        except ValueError:
            pass








if __name__ == "__main__":
    main()
