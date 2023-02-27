from structures.linked_stack import LinkedStack


def stack_task(pokemon_count: int, pokemons: list) -> None:
    print("\n----------------------------------------")
    print("Tarefas de stack:")

    pokemon_stack = LinkedStack()

    print("\n1 - Inserindo dados na stack...")
    for i in range(pokemon_count):
        pokemon_stack.insert(pokemons[i])
        print(f'passo {i+1}:', pokemon_stack)

    print("\n2 - Removendo elemento da stack...")
    for i in range(pokemon_stack.size):
        print(f'Passo {i+1}:', pokemon_stack)
        pokemon_stack.remove()
    print(f'Passo {i+2}:', pokemon_stack)

    print("\n3 - Mostrando se a stack está vazia ou não...")
    print("stack ", "Vazia" if  pokemon_stack.is_empty() else "Não vazia")

    print("\nPreenchendo a stack novamente...")
    for i in range(pokemon_count):
        pokemon_stack.insert(pokemons[i])

    print("\n4 - Exibindo o tamanho da stack...")
    print("Tamanho da stack: ", pokemon_stack.size)

    print("\n5 - Exibindo elemento da stack...")
    print(pokemon_stack.element())

    print("\nFIM stack\n")
