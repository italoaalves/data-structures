from estruturas.excecoes import EstruturaException
from estruturas.no import Node


class PilhaEncadeada:
    def __init__(self):
        self.__head = None
        self.__tamanho = 0

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, no):
        self.__head = no

    def vazia(self):
        if self.__tamanho == 0:
            return True

    def tamanho(self):
        return self.__tamanho

    def inserir(self, dado):
        if self.vazia():
            no = Node(dado)
            self.__head = no
            no.prox = None
            self.__tamanho += 1
        else:
            no = Node(dado)
            no.prox = self.__head
            self.__head = no
            self.__tamanho += 1

    def elemento(self):
        if(self.vazia()):
            raise EstruturaException('A pilha está vazia')
        return self.__head

    def remover(self):
        if self.vazia():
            raise EstruturaException('A fila está vazia')
        self.__head = self.__head.prox
        self.__tamanho -= 1

    def __str__(self):
        saida = 'Pilha: ['
        cursor = self.__head

        while cursor != None:
            saida += f'{str(cursor.dado)}'
            cursor = cursor.prox

            if cursor != None:
                saida += ', '

        saida += ']'
        return saida
