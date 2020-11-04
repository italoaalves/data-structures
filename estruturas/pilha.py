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
        cursor = self.__head

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

    def
            raise Exceptions('A fila está vazia')
        return self.__inicio

    def __str__(self):
        saida = 'Fila: ['
        cursor = self.__head

        while cursor != None:
            aux = cursor.dado
            saida += f'{cursor.dado}'
            cursor = cursor.prox
            if cursor != None:
                saida += ', '

        saida += ']'
        return saida
