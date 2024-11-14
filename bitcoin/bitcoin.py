import requests
import sys
from pprint import pprint


class CommandLineParser:
    def __init__(self):
        self.argv = sys.argv[1:]

    def get_parm_count(self):
        return len(self.argv)

    def get_parm_list(self):
        return [l for l in self.argv]
    

try:
    p = CommandLineParser()
    print(p.get_parm_count())
    print(p.get_parm_list())

except requests.RequestException:
    pass
except:
    pass
