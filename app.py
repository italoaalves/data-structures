import requests
from estruturas.pokemon import Pokemon


def captura_pokemons(quantidade: int = 1) -> list:
    """ Busca na api a quantidade de Pokemons passada como parametro e
    retorna uma lista
    """
    pokemons: list = []

    for i in range(quantidade):
        pokemon_dict: dict = requests.get(
            f'https://pokeapi.co/api/v2/pokemon/{i+1}').json()

        nome: str = pokemon_dict["name"]
        altura: float = pokemon_dict["height"]
        peso: float = pokemon_dict["weight"]
        tipo: str = pokemon_dict["types"][0]["type"]["name"]

        pokemon = Pokemon(i+1, nome, altura, peso, tipo)
        pokemons.append(pokemon)

    return pokemons


if __name__ == "__main__":
    pokemons: list = captura_pokemons()

    print(pokemons[0].nome, pokemons[0].tipo)
