from random import randint

from estruturas.excecoes import EstruturaException
from estruturas.lista import ListaEncadeada


def tarefas_lista(quantidade_pokemons: int, pokemons: list) -> None:
    """Script que executa as tarefas
    que cumprem os requisitos do projeto
    para lista encadeada
    """
    print("\n----------------------------------------")
    print("Tarefas de Lista:")

    lista_pokemons: ListaEncadeada = ListaEncadeada()

    # Lista
    # Inserção
    print("\n1 - Inserindo dados na lista...")
    for i in range(quantidade_pokemons):
        lista_pokemons.inserir(i + 1, pokemons[i])
    print(lista_pokemons)

    # Remoção
    print("\n2 - Removendo o ultimo elemento da lista...")
    lista_pokemons.remover(quantidade_pokemons)  # remove o ultimo inserido
    print(lista_pokemons)

    # Vazio
    print("\n3 - Mostrando se a lista está vazia ou não...")
    vazia: bool = lista_pokemons.vazia()
    print("lista ", "Vazia" if vazia else "Não vazia")

    # Tamanho
    print("\n4 - Exibindo o tamanho da lista...")
    tamanho: int = lista_pokemons.tamanho
    print("Tamanho da lista: ", tamanho)

    # Mostrar elemento
    print("\n5 - Exibindo elemento da lista...")
    elemento: object = lista_pokemons.elemento(randint(1, quantidade_pokemons))
    print(elemento)

    # Ordenar lista
    print("\n6 - Ordenando a lista pelo peso do Pokemon...")
    lista_pokemons.ordenar_por("peso")
    print(lista_pokemons)

    # Busca
    try:
        print("\n7 - Buscando Pokemons pelo tipo grama...")
        resultados: list = lista_pokemons.busca_por("tipo", "grass")
        print("Resultados da busca: [", end="")
        for resultado in resultados:
            print(resultado, ", ", end="")
        print("]")
    except EstruturaException as ee:
        print(ee)

    # Busca com falha
    try:
        print("\n8 - Buscando Pokemons por um tipo inexistente...")
        resultados: list = lista_pokemons.busca_por("tipo", "carburador")
    except EstruturaException as ee:
        print("Resultados da busca com falha:", ee)

    print("FIM LISTA\n")
