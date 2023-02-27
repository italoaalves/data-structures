from structures.linked_queue import LinkedQueue


def queue_task(pokemon_count: int, pokemons: list) -> None:
    print("\n----------------------------------------")
    print("Tarefas de Fila:")

    pokemon_queue = LinkedQueue()

    print("\n1 - Inserindo dados na fila...")
    for i in range(pokemon_count):
        pokemon_queue.insert(pokemons[i])
        print(f'Passo {i+1}', pokemon_queue)

    print("\n2 - Removendo elementos da fila...")
    for i in range(pokemon_queue.size):
        print(f'Passo {i+1}', pokemon_queue)
        pokemon_queue.remove()
    print(f'Passo {i+2}', pokemon_queue)

    print("\n3 - Mostrando se a fila está vazia ou não...")
    print("Fila", "Vazia" if pokemon_queue.is_empty() else "Não vazia")

    print("\nPreenchendo a fila novamente...")
    for i in range(pokemon_count):
        pokemon_queue.insert(pokemons[i])

    print("\n4 - Exibindo o tamanho da fila...")
    print("Tamanho da fila: ", pokemon_queue.size)

    print("\n5 - Exibindo elemento da fila...")
    print(pokemon_queue.element())

    print("\nFIM FILA\n")
