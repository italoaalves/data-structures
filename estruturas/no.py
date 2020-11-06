class Node:
    def __init__(self, dado=None) -> None:
        self.__dado: object = dado
        self.__prox = None

    @property
    def dado(self) -> object:
        return self.__dado

    @property
    def prox(self) -> object:
        return self.__prox

    @dado.setter
    def dado(self, novoDado) -> None:
        self.__dado = novoDado

    @prox.setter
    def prox(self, novoProx) -> None:
        self.__prox = novoProx

    def __str__(self) -> str:
        return str(self.__dado)
