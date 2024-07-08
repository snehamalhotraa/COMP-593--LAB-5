'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_info() function
    # Use breakpoints to view returned dictionary
    
    poke_info = get_pokemon_info("Rockruff")
    if poke_info:
        print(poke_info)
    else:
        print("Failed to fetch Pokemon information.")
    return

def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # TODO: Clean the Pokemon name parameter
    
    pokemon_name = str(pokemon_name).strip().lower()

    # TODO: Build a clean URL and use it to send a GET request

    url = f'{POKE_API_URL}{pokemon_name}'

    # TODO: If the GET request was successful, convert the JSON-formatted message body text to a dictionary and return it

    # TODO: If the GET request failed, print the error reason and return None

    try:
        response = requests.get(url)
        # If the GET request was successful, convert the JSON-formatted message body text to a dictionary and return it
        if response.status_code == 200:
            return response.json()
        else:
           
            print(f'Error: Not able to get data for {pokemon_name}. HTTP Status code: {response.status_code}')
            return None
        
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        return None

if __name__ == '__main__':
    main()