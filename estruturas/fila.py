from estruturas.excecoes import EstruturaException
from estruturas.no import Node


class FilaEncadeada:
    def __init__(self) -> None:
        self.__head: object = None
        self.__tamanho: int = 0

    @property
    def head(self) -> object:
        return self.__head

    @head.setter
    def head(self, novoHead: object = None) -> None:
        self.__head = novoHead

    @property
    def tamanho(self) -> int:
        return self.__tamanho

    def vazia(self) -> bool:
        if self.__tamanho == 0:
            return True

    def inserir(self, dado) -> None:
        cursor: object = self.__head

        if self.vazia():
            no = Node(dado)
            self.__head = no
            no.prox = None
            self.__tamanho += 1
        else:
            while cursor != None:
                ultimo_elem = cursor
                cursor = cursor.prox
            no = Node(dado)
            no.prox = ultimo_elem.prox
            ultimo_elem.prox = no
            self.__tamanho += 1

    def remover(self) -> None:
        if self.vazia():
            raise EstruturaException('A fila está vazia')
        self.__head = self.__head.prox
        self.__tamanho -= 1

    def elemento(self) -> object:
        if(self.vazia()):
            raise EstruturaException('A fila está vazia')
        return self.__head.dado

    def __str__(self) -> str:
        saida: str = 'Fila: ['
        cursor: object = self.__head

        while cursor != None:
            saida += f'{str(cursor.dado)}'
            cursor = cursor.prox

            if cursor != None:
                saida += ', '

        saida += ']'
        return saida
