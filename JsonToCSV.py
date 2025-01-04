import requests
import json
import csv

def fetch_pokemon_data(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/bulbasaur'
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    data = response.json()
    return data

def save_json_to_file(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def json_to_csv(json_filename, csv_filename):
    with open(json_filename, 'r') as json_file:
        data = json.load(json_file)
    
    # Flatten the JSON data
    flat_data = flatten_json(data)
    
    # Write to CSV
    with open(csv_filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(flat_data.keys())
        writer.writerow(flat_data.values())

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
    pokemon_name = 'bulbasaur'
    data = fetch_pokemon_data(pokemon_name)
    
    json_filename = f'{pokemon_name}.json'
    csv_filename = f'{pokemon_name}.csv'
    
    save_json_to_file(data, json_filename)
    json_to_csv(json_filename, csv_filename)
    
    print(f"Data saved to {json_filename} and converted to {csv_filename}")

if __name__ == "__main__":
    main()