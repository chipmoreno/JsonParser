import requests
import json
import csv

def fetch_pokemon_data(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    data = response.json()
    return data

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

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

def main():
    pokemon_names = input("Enter the names of the Pokémon (separated by commas): ").strip().lower().split(',')
    all_data = []
    all_keys = set()
    
    for pokemon_name in pokemon_names:
        pokemon_name = pokemon_name.strip()
        try:
            data = fetch_pokemon_data(pokemon_name)
            all_data.append(data)
            all_keys.update(get_all_keys(data))
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred for {pokemon_name}: {http_err}")
        except Exception as err:
            print(f"Other error occurred for {pokemon_name}: {err}")
    
    print("\nAvailable Field Titles:")
    for key in sorted(all_keys):
        print(key)
    
    selected_fields = input("\nEnter the field titles to include in the output (separated by commas) or type 'all' to include all fields: ").strip().lower()
    if selected_fields != "all":
        selected_fields = [field.strip() for field in selected_fields.split(',')]
    
    csv_filename = 'pokemon_data.csv'
    
    with open(csv_filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        # Write headers
        if selected_fields == "all":
            headers = sorted(all_keys)
        else:
            headers = selected_fields
        writer.writerow(headers)
        
        # Write data
        for data in all_data:
            flat_data = flatten_json(data)
            row = [flat_data.get(field, '') for field in headers]
            writer.writerow(row)
    
    print(f"Data saved to {csv_filename}")

if __name__ == "__main__":
    main()