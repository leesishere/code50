import json
import requests

response = requests.get('https://itunes.apple.com/search?entity=song&limit=50&term=weezer')
artist = response.json()

for result in artist['results']:
    print(result["trackName"])
