import requests
import json

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
    return keys  # This should be outside the elif block

def fetch_pokemon_data(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    data = response.json()
    return data

def main():
    pokemon_name = input("Enter the name of the Pokémon: ").strip().lower()
    try:
        data = fetch_pokemon_data(pokemon_name)
        all_keys = get_all_keys(data)
        print(f"\nAvailable Field Titles for {pokemon_name.capitalize()}:")
        for key in sorted(all_keys):
            print(key)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

if __name__ == "__main__":
    main()