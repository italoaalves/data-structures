from random import randint

from es.pokeapi import captura_pokemons

from tarefas.lista import tarefas_lista
from tarefas.fila import tarefas_fila
from tarefas.pilha import tarefas_pilha


if __name__ == "__main__":
    quantidade_pokemons: int = 15
    pokemons: list = captura_pokemons(quantidade_pokemons)
    pokemons_batalha: list = []

    tarefas_lista(quantidade_pokemons, pokemons)

    for i in range(6):
        pokemons_batalha.append(pokemons[randint(1, quantidade_pokemons - 1)])

    tarefas_fila(6, pokemons_batalha)
    tarefas_pilha(6, pokemons_batalha)
