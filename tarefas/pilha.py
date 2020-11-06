from es import imprime_estrutura
from estruturas.pilha import PilhaEncadeada


def tarefas_pilha(quantidade_pokemons: int, pokemons: list) -> None:
    """Script que executa as tarefas
    que cumprem os requisitos do projeto
    para pilha encadeada
    """
    pilha_pokemons: PilhaEncadeada = PilhaEncadeada()

    # Inserção pilha
    for i in range(6):
        pilha_pokemons.inserir(pokemons[i])

        # Remoção da pilha
    pilha_pokemons.remover()
    imprime_estrutura(pilha_pokemons)

    # Vazio
    vazia: bool = pilha_pokemons.vazia()
    print("Pilha ", "Vazia" if vazia else "Não vazia")

    # Tamanho
    tamanho: int = pilha_pokemons.tamanho()
    print("Tamanho da pilha: ", tamanho)

    # Mostrar elemento
    elemento: object = pilha_pokemons.elemento()
    print(elemento)
