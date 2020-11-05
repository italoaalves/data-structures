class Node:
    def __init__(self, dado=None):
        self.__dado = dado
        self.__prox = None

    @property
    def dado(self):
        return self.__dado

    @property
    def prox(self):
        return self.__prox

    @dado.setter
    def dado(self, novoDado):
        self.__dado = novoDado

    @prox.setter
    def prox(self, novoProx):
        self.__prox = novoProx

    def __str__(self):
        return str(self.__dado)
