import requests
import json
import sqlite3
import csv

def fetch_pokemon_data(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/bulbasaur'
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    data = response.json()
    return data

def save_json_to_db(data, db_filename):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    
    # Flatten the JSON data
    flat_data = flatten_json(data)
    
    # Split data into chunks to avoid too many columns error
    chunk_size = 1000  # Adjust chunk size if necessary
    flat_data_items = list(flat_data.items())
    for i in range(0, len(flat_data_items), chunk_size):
        chunk = dict(flat_data_items[i:i + chunk_size])
        table_name = f'pokemon_{i // chunk_size}'
        
        # Create table
        columns = ', '.join(f'"{key}" TEXT' for key in chunk.keys())
        cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({columns})')
        
        # Insert data
        placeholders = ', '.join('?' for _ in chunk.values())
        cursor.execute(f'INSERT INTO {table_name} VALUES ({placeholders})', list(chunk.values()))
    
    conn.commit()
    conn.close()

def db_to_csv(db_filename, csv_filename):
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    
    with open(csv_filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        # Write headers and data for each table
        for table_name in cursor.execute("SELECT name FROM sqlite_master WHERE type='table'"):
            table_name = table_name[0]
            cursor.execute(f'SELECT * FROM {table_name}')
            rows = cursor.fetchall()
            
            # Write headers
            writer.writerow([description[0] for description in cursor.description])
            
            # Write data
            writer.writerows(rows)
    
    conn.close()

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
    
    db_filename = f'{pokemon_name}.db'
    csv_filename = f'{pokemon_name}.csv'
    
    save_json_to_db(data, db_filename)
    db_to_csv(db_filename, csv_filename)
    
    print(f"Data saved to {db_filename} and converted to {csv_filename}")

if __name__ == "__main__":
    main()