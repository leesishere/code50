import json
import requests

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=50&term=weezer"
)

artist = response.json()

for result in artist["results"]:
    print(result["trackName"])

my_list = [
    1,
    2,
    3,
    4,
    5,
    6,
]
result = some_function_that_takes_arguments(
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
)


def cow(s):
    my_cow = r"""
  ___________
 | All Done! |
  ===========
           \
            \
              ^__^
              (oo)\_______
              (__)\       )\/\
                  ||----w |
                  ||     ||)
"""
    print(my_cow)


cow("Hello World")
