from estruturas.excecoes import EstruturaException
from estruturas.no import Node


class FilaEncadeada:
    def __init__(self):
        self.__inicio = None
        self.__tamanho = 0

    def vazia(self):
        if self.__tamanho == 0:
            return True

    def tamanho(self):
        return self.__tamanho

    def remover(self):
        if self.vazia():
            raise Exceptions('A fila está vazia')
        self.__inicio = self.__inicio.prox
        self.__tamanho -= 1

    def elemento(self):
        if(self.vazia()):
            raise Exceptions('A fila está vazia')
        return self.__inicio

    def inserir(self, dado):
        cursor = self.__inicio

        if self.vazia():
            no = Node(dado)
            self.__inicio = no
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

    def remover(self):
        if self.vazia():
            raise Exceptions('A fila está vazia')
        self.__inicio = self.__inicio.prox
        self.__tamanho -= 1

    def __str__(self):
        saida = 'Fila: ['
        cursor = self.__inicio

        while cursor != None:
            saida += f'{cursor.dado}'
            cursor = cursor.prox

            if cursor != None:
                saida += ', '

        saida += ']'
        return saida
