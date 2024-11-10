import json
import requests

text = requests.get('https://itunes.apple.com/search?entity=song&limit=1&term=weazer')
print(text.json)

