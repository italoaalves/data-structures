from random import randint
from os import system, name

from clients.pokeapi_client import fetch_pokemons

from tasks.list_task import list_task
from tasks.queue_task import queue_task
from tasks.stack_task import stack_task


if __name__ == "__main__":
    print("Este programa executa as tarefas que cumprem os requisitos do projeto.")

    while True:
        try:
            pokemon_count: int = int(
                input("Insira a quantidade de pokemons a lista: "))
            assert isinstance(pokemon_count,
                              int) and pokemon_count > 0
            break
        except AssertionError:
            print("Você precisa inserir um valor inteiro positivo.")
        except ValueError:
            print("Você precisa inserir um valor inteiro positivo.")

    system('cls' if name == 'nt' else 'clear')

    random_number = pokemon_count != 150
    list_task(pokemon_count, fetch_pokemons(
        pokemon_count, random_number))

    input("Enter para continuar")

    queue_task(6, fetch_pokemons(6, random_number=True))

    input("Enter para continuar")

    stack_task(6, fetch_pokemons(6, random_number=True))

    input("Enter para finalizar\n")
