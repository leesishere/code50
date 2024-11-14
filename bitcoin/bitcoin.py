import requests
import sys
from pprint import pprint

class CommandLineParser:
    def __init__(self):
        try:
            self.argv = sys.argv[1:]
        except:
            sys.exit

    def get_parm_count(self):
        return len(self.argv)

    def get_parm_list(self):
        return [l for l in self.argv]

    def get_param_float():
        result = any(type(p) == type(1.0) for p in self.argv)
        if result:
            return True
        else:
            return False

try:
    p = CommandLineParser()
    #print(p.get_parm_count())
    #print(p.get_parm_list())
    print(f"{p.get_param_float()}")

except requests.RequestException:
    pass
except:
    pass
