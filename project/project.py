import requests

def get_howtosay(word)
    # Define the API endpoint
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        data = data[0]
        return data['phonetics'][0]['audio'])

    else:
        return None





