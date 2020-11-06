from random import randint
from estruturas.excecoes import EstruturaException
from es import imprime_estrutura
from estruturas.lista import ListaEncadeada


def tarefas_lista(quantidade_pokemons: int, pokemons: list) -> None:
    """Script que executa as tarefas
    que cumprem os requisitos do projeto
    para lista encadeada
    """

    lista_pokemons: ListaEncadeada = ListaEncadeada()

    # Lista
    # Inserção
    for i in range(quantidade_pokemons):
        lista_pokemons.inserir(i + 1, pokemons[i])

    imprime_estrutura(lista_pokemons)

    # Remoção
    lista_pokemons.remover(quantidade_pokemons)  # remove o ultimo inserido
    imprime_estrutura(lista_pokemons)

    # Vazio
    vazia: bool = lista_pokemons.vazia()
    print("lista ", "Vazia" if vazia else "Não vazia")

    # Tamanho
    tamanho: int = lista_pokemons.tamanho()
    print("Tamanho da lista: ", tamanho)

    # Mostrar elemento
    elemento: object = lista_pokemons.elemento(randint(1, quantidade_pokemons))
    print(elemento)

    # Ordenar lista
    lista_pokemons.ordena_por("peso")
    imprime_estrutura(lista_pokemons)

    # Busca
    try:
        resultados: list = lista_pokemons.busca_por("tipo", "grass")
        print("Resultados da busca: [", end="")
        for resultado in resultados:
            print(resultado, ", ", end="")
        print("]")
    except EstruturaException as ee:
        print(ee)

    # Busca com falha
    try:
        resultados: list = lista_pokemons.busca_por("tipo", "carburador")
        print("Resultados da busca: [", end="")
        for resultado in resultados:
            print(resultado + ", ", end="")
        print("]")
    except EstruturaException as ee:
        print("Resultados da busca com falha:", ee)
