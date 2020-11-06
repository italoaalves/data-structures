from estruturas.pilha import PilhaEncadeada


def tarefas_pilha(quantidade_pokemons: int, pokemons: list) -> None:
    """Script que executa as tarefas
    que cumprem os requisitos do projeto
    para pilha encadeada
    """

    print("\n----------------------------------------")
    print("Tarefas de Pilha:")

    pilha_pokemons: PilhaEncadeada = PilhaEncadeada()

    # Inserção pilha
    print("\n1 - Inserindo dados na pilha...")
    for i in range(6):
        pilha_pokemons.inserir(pokemons[i])
        print(f'passo {i+1}:', pilha_pokemons)

    # Remoção da pilha
    print("\n2 - Removendo elemento da pilha...")
    for i in range(pilha_pokemons.tamanho):
        print(f'Passo {i+1}:', pilha_pokemons)
        pilha_pokemons.remover()
    print(f'Passo {i+2}:', pilha_pokemons)

    # Vazio
    print("\n3 - Mostrando se a pilha está vazia ou não...")
    vazia: bool = pilha_pokemons.vazia()
    print("Pilha ", "Vazia" if vazia else "Não vazia")

    # Reinserindo elementos
    print("\nPreenchendo a pilha novamente...")
    for i in range(6):
        pilha_pokemons.inserir(pokemons[i])

    # Tamanho
    print("\n4 - Exibindo o tamanho da pilha...")
    tamanho: int = pilha_pokemons.tamanho
    print("Tamanho da pilha: ", tamanho)

    # Mostrar elemento
    print("\n5 - Exibindo elemento da pilha...")
    elemento: object = pilha_pokemons.elemento()
    print(elemento)

    print("\nFIM PILHA\n")
