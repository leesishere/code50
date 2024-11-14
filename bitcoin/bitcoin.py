import requests
import sys
from pprint import pprint

class CommandLineParser:
    def __init__(self):
        try:
            self.argv = sys.argv[1:]
            self.exit = sys.exit
        except:
            self.exit()

    def get_parm_count(self):
        return len(self.argv)

    def get_parm_list(self):
        return [l for l in self.argv]

    def get_param_float(self):
        result = any(type(p) == type(1.0) for p in self.argv)
        if result:
            return True
        else:
            return False
    def convert_argv():
        try:
            for l in self.argv:
                i - float(i)
        except:
            self.exit()
        return i
    def exit():
        return self.exit('101')

p = CommandLineParser()
print(p.get_parm_count())
print(p.get_parm_list())
print(p.convert_argv())



'''
if not p.get_param_float():
    p.exit("Complete failure!")
else:
    print("Oh, well!")
'''
#except requests.RequestException:
#    pass
#except:
#    pass
