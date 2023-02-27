import asyncio
import aiohttp
from random import randint
from structures.pokemon import Pokemon


url_base: str = "https://pokeapi.co/api/v2/pokemon/"


async def fetch_pokemon(id: int, pokemon_list: list) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{url_base}{id}') as response:
            pokemon_dict: dict = await response.json()

            pokemon = Pokemon(
                id,
                pokemon_dict["name"],
                pokemon_dict["height"],
                pokemon_dict["weight"],
                pokemon_dict["types"][0]["type"]["name"]
            )
            pokemon_list.append(pokemon)


def fetch_pokemons(count: int = 1, random_number: bool = False) -> list:
    pokemons: list = []
    loop: object = asyncio.get_event_loop()
    possible_count: int = count if count <= 890 else 890

    print("\nBuscando pokemons, aguarde...")

    loop.run_until_complete(
        asyncio.gather(
            *(fetch_pokemon(randint(1, 890) if random_number else i+1, pokemons) for i in range(possible_count))
        )
    )

    if random_number and count > 890:
        pokemons.extend([
            pokemons[randint(0, 889)] for i in range(count - 890)
        ])
    elif count > 890 and not random_number:
        raise Exception("Só existem 890 pokemons.")

    return pokemons
