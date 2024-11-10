import json
import requests

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=50&term=weezer"
)

artist = response.json()

for result in artist["results"]:
    print(result["trackName"])


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
