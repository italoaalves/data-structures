import asyncio
import aiohttp
from random import randint
from estruturas.pokemon import Pokemon


url_base: str = "https://pokeapi.co/api/v2/pokemon/"


async def captura_pokemon(id: int, lista: list) -> None:
    async with aiohttp.ClientSession() as sessao:
        async with sessao.get(f'{url_base}{id}') as resposta:
            pokemon_dict: dict = await resposta.json()

            nome: str = pokemon_dict["name"]
            altura: float = pokemon_dict["height"]
            peso: float = pokemon_dict["weight"]
            tipo: str = pokemon_dict["types"][0]["type"]["name"]

            pokemon = Pokemon(id, nome, altura, peso, tipo)
            lista.append(pokemon)


def captura_pokemons(quantidade: int = 1, aleatorio: bool = False) -> list:
    """ Busca na api a quantidade de Pokemons passada como parametro e
    retorna uma lista
    """
    pokemons: list = []
    loop: object = asyncio.get_event_loop()

    print("\nBuscando pokemons, aguarde...")

    if quantidade < 890:
        loop.run_until_complete(
            asyncio.gather(
                *(captura_pokemon(randint(1, 890) if aleatorio else i+1, pokemons) for i in range(quantidade))
            )
        )
    elif aleatorio:
        loop.run_until_complete(
            asyncio.gather(
                *(captura_pokemon(randint(1, 890) if aleatorio else i+1, pokemons) for i in range(890))
            )
        )

        pokemons.extend([pokemons[randint(0, 889)]
                         for i in range(quantidade-890)])
    else:
        raise Exception("Só existem 890 pokemons.")

    return pokemons
