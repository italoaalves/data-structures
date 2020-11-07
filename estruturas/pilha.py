from estruturas.excecoes import EstruturaException
from estruturas.no import Node


class PilhaEncadeada:
    def __init__(self):
        self.__head: object = None
        self.__tamanho: int = 0

    @property
    def head(self) -> object:
        return self.__head

    @head.setter
    def head(self, novoNo: object) -> None:
        self.__head = novoNo

    @property
    def tamanho(self) -> int:
        return self.__tamanho

    def vazia(self) -> bool:
        if self.__tamanho == 0:
            return True

    def inserir(self, dado: object) -> None:
        no: object = Node(dado)

        if self.vazia():
            self.__head = no
            no.prox = None
            self.__tamanho += 1
        else:
            no.prox = self.__head
            self.__head = no
            self.__tamanho += 1

    def remover(self) -> None:
        if self.vazia():
            raise EstruturaException('A fila está vazia')
        self.__head = self.__head.prox
        self.__tamanho -= 1

    def elemento(self) -> object:
        if(self.vazia()):
            raise EstruturaException('A pilha está vazia')
        return self.__head.dado

    def __str__(self) -> str:
        saida: str = 'Pilha: ['
        cursor: object = self.__head

        while cursor != None:
            saida += f'{str(cursor.dado)}'
            cursor = cursor.prox

            if cursor != None:
                saida += ', '

        saida += ']'
        return saida
