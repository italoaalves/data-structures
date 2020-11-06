from random import randint

from es.pokeapi import captura_pokemons

from tarefas.lista import tarefas_lista
from tarefas.fila import tarefas_fila
from tarefas.pilha import tarefas_pilha


if __name__ == "__main__":
    print("Este programa executa as tarefas que cumprem os requisitos do projeto.")

    while True:
        try:
            quantidade_pokemons: int = int(
                input("Insira a quantidade de pokemons para trabalhar: "))
            assert isinstance(quantidade_pokemons,
                              int) and quantidade_pokemons > 0
            break
        except AssertionError:
            print("Você precisa inserir um valor inteiro positivo.")

    pokemons: list = captura_pokemons(quantidade_pokemons)
    pokemons_batalha: list = []

    tarefas_lista(quantidade_pokemons, pokemons)

    for i in range(6):
        pokemons_batalha.append(pokemons[randint(1, quantidade_pokemons - 1)])

    input("Enter para continuar")

    tarefas_fila(6, pokemons_batalha)

    input("Enter para continuar")

    tarefas_pilha(6, pokemons_batalha)

    input("Enter para finalizar")
