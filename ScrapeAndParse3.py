import requests

pokemon_names = ['bulbasaur', 'ivysaur', 'venusaur', 'charmander', 'charmeleon', 
                 'charizard', 'squirtle', 'wartortle', 'blastoise', 'caterpie']

for pokemon in pokemon_names: 
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    response = requests.get(url)
    response = requests.get(url)
    data = response.json()
    print("Name:", data.get('name'))
    print("Base Experience:", data.get('base_experience'))
    print("Height:", data.get('height'))
    print("Weight:", data.get('weight'))
    
    
    
    #print("Moves:")
    #for move in data.get('moves', []):
        #print(f"  {move['move']['name']}")



