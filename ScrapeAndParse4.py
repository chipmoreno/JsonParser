import requests
import json

# URL for the API
url = 'https://pokeapi.co/api/v2/pokemon/bulbasaur'

# Send GET request to the API
response = requests.get(url)

# Parse JSON data from the response
data = response.json()

# Function to extract all keys from JSON
def get_all_keys(obj, keys=None):
    if keys is None:
        keys = set()  # Initialize an empty set if no keys are passed
    if isinstance(obj, dict):
        for key, value in obj.items():
            keys.add(key)  # Add the current key
            keys.update(get_all_keys(value))  # Recursively add nested keys
    elif isinstance(obj, list):
        for item in obj:
            keys.update(get_all_keys(item))  # Recursively process list items
    return keys

# Call the function with the parsed JSON data
all_keys = get_all_keys(data)

# Print the field titles
print("Available Field Titles:")
for key in (sorted(all_keys)):
    print (key)
