from random import randint
from structures.exceptions import StructureException
from structures.linked_list import LinkedList


def list_task(pokemon_count: int, pokemons: list) -> None:
    print("\n----------------------------------------")
    print("Tarefas de Lista:")

    pokemon_list = LinkedList()

    print("\n1 - Inserindo dados na lista...")
    for i in range(pokemon_count):
        pokemon_list.insert(i + 1, pokemons[i])
    print(pokemon_list)

    print("\n2 - Removendo o ultimo elemento da lista...")
    pokemon_list.remove(pokemon_count)  # remove o ultimo inserido
    print(pokemon_list)

    pokemon_list.insert(pokemon_count,
                           pokemons[pokemon_count-1])

    print("\n3 - Mostrando se a lista está vazia ou não...")
    print("lista ", "Vazia" if pokemon_list.is_empty() else "Não vazia")

    print("\n4 - Exibindo o tamanho da lista...")
    print("Tamanho da lista: ", pokemon_list.size)

    print("\n5 - Exibindo elemento da lista...")
    print(pokemon_list.element(randint(1, pokemon_count)))

    print("\n6 - Ordenando a lista pelo peso do Pokemon...")
    pokemon_list.order_by("weight")
    print(pokemon_list)

    try:
        print("\n7 - Buscando Pokemons pelo tipo grama...")
        results = pokemon_list.search_by("type", "grass")
        print("Resultados da busca: [", end="")
        results_len = len(results)
        for i in range(results_len):
            print(results[i], end=", " if i <
                  results_len - 1 else ']')
    except StructureException as e:
        print(e)

    # Search with error
    try:
        print("\n\n8 - Buscando Pokemons por um tipo inexistente...")
        results = pokemon_list.search_by("type", "carburador")
    except StructureException as e:
        print("Resultados da busca com falha:", e)

    print("\nFIM LISTA\n")
