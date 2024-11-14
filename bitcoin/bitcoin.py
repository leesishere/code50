import requests
import sys

from pprint import pprint

# Font names: http://www.figlet.org/fontdb.cgi

class CommandLineParser(sys):
    def __init__(self):
        super().__init__()

    def get_parm_count(self):
        return len(self.argv)


try:
    p = CommandLineParser()
    print(p.get_parm_count())

except requests.RequestException:
    pass
except:
    pass
