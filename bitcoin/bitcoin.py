import requests
import sys
from pprint import pprint
import requests

class CommandLineBitcoinParser:
    def __init__(self):
        try:
            self.argv = sys.argv[1:]
            self.exit = sys.exit
        except:
            self.exit()

    def get_parm_count(self):
        if len(self.argv) < 1:
            self.exit("Missing Command-line argument")
        return len(self.argv)

    def get_parm_list(self):
        if len(self.argv) < 1:
            self.exit("Missing Command-line argument")
        return [l for l in self.argv]

    def get_param_float(self):
        result = any(type(p) == type(1.0) for p in self.argv)
        if result:
            return True
        else:
            return False
    def convert_argv(self):
        if self.get_parm_count():
            for l in self.argv:
                if self.is_float(l):
                    l = float(l)
                else:
                    self.exit("Command-line argument is not a number")
            return l

    def is_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def exit(self, error_message):
        return self.exit(error_message)
def main():

    p = CommandLineBitcoinParser()

    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        formatted_amount = "${:,.2f}".format(amount)
        bitcoin_price = float(data['bpi']['USD']['rate'].replace(',',''))
        print(f"{bitcoin_price * p.convert_argv()}")

    else:
        print("Failed to retrieve data from the API")

if __name__ == "__main__":
    main()

