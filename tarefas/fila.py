from estruturas.fila import FilaEncadeada


def tarefas_fila(quantidade_pokemons: int, pokemons: list) -> None:
    """Script que executa as tarefas
    que cumprem os requisitos do projeto
    para fila encadeada
    """

    print("\n----------------------------------------")
    print("Tarefas de Fila:")

    fila_pokemons: FilaEncadeada = FilaEncadeada()

    # Inserção fila
    print("\n1 - Inserindo dados na fila...")
    for i in range(6):
        fila_pokemons.inserir(pokemons[i])
        print(f'Passo {i+1}', fila_pokemons)

    # Remoção da fila
    print("\n2 - Removendo elementos da fila...")
    for i in range(fila_pokemons.tamanho):
        print(f'Passo {i+1}', fila_pokemons)
        fila_pokemons.remover()
    print(f'Passo {i+2}', fila_pokemons)

    # Vazio
    print("\n3 - Mostrando se a fila está vazia ou não...")
    vazia: bool = fila_pokemons.vazia()
    print("Fila", "Vazia" if vazia else "Não vazia")

    # Preenchendo a fila novamente
    print("\nPreenchendo a fila novamente...")
    for i in range(6):
        fila_pokemons.inserir(pokemons[i])

    # Tamanho
    print("\n4 - Exibindo o tamanho da fila...")
    tamanho: int = fila_pokemons.tamanho
    print("Tamanho da fila: ", tamanho)

    # Mostrar elemento
    print("\n5 - Exibindo elemento da fila...")
    elemento: object = fila_pokemons.elemento()
    print(elemento)

    print("FIM FILA\n")
