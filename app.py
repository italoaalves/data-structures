from random import randint
from os import system, name

from es.pokeapi import captura_pokemons

from tarefas.lista import tarefas_lista
from tarefas.fila import tarefas_fila
from tarefas.pilha import tarefas_pilha


if __name__ == "__main__":
    print("Este programa executa as tarefas que cumprem os requisitos do projeto.")

    while True:
        try:
            quantidade_pokemons: int = int(
                input("Insira a quantidade de pokemons a lista: "))
            assert isinstance(quantidade_pokemons,
                              int) and quantidade_pokemons > 0
            break
        except AssertionError:
            print("Você precisa inserir um valor inteiro positivo.")
        except ValueError:
            print("Você precisa inserir um valor inteiro positivo.")

    system('cls' if name == 'nt' else 'clear')

    aleatorio = quantidade_pokemons != 150
    tarefas_lista(quantidade_pokemons, captura_pokemons(
        quantidade_pokemons, aleatorio))

    input("Enter para continuar")

    tarefas_fila(6, captura_pokemons(6, aleatorio=True))

    input("Enter para continuar")

    tarefas_pilha(6, captura_pokemons(6, aleatorio=True))

    input("Enter para finalizar\n")
