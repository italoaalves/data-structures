from es import imprime_estrutura
from estruturas.fila import FilaEncadeada


def tarefas_fila(quantidade_pokemons: int, pokemons: list) -> None:
    """Script que executa as tarefas
    que cumprem os requisitos do projeto
    para fila encadeada
    """
    fila_pokemons: FilaEncadeada = FilaEncadeada()

    # Inserção fila
    for i in range(6):
        fila_pokemons.inserir(pokemons[i])

    imprime_estrutura(fila_pokemons)

    # Remoção da fila
    fila_pokemons.remover()
    imprime_estrutura(fila_pokemons)

    # Vazio
    vazia: bool = fila_pokemons.vazia()
    print("Fila", "Vazia" if vazia else "Não vazia")

    # Tamanho
    tamanho: int = fila_pokemons.tamanho()
    print("Tamanho da fila: ", tamanho)

    # Mostrar elemento
    elemento: object = fila_pokemons.elemento()
    print(elemento)
