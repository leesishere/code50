import requests

def save_response_to_text(url, filename='.txt'):
    # Make the web request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Save the response text to a file
        with open(filename, 'w') as file:
            file.write(response.text)
        print(f'Response saved to {filename}')
    else:
        print(f'Failed to retrieve data. Status code: {response.status_code}')

# Define the API endpoint
url = "https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words_alpha.txt"
save_response_to_text(url)
