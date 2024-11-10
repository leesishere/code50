import json
import requests

response = requests.get('https://itunes.apple.com/search?entity=song&limit=1&term=weezer')
print(json.dumps(response.json(), indent=4))

