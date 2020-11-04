import requests
from estruturas import dado


# Exemplo api
if __name__ == "__main__":
    pokemon = dado.Dado(requests.get(
        "https://pokeapi.co/api/v2/pokemon/1").json())
    print(pokemon.dado["name"])
