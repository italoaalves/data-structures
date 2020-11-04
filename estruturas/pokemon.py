class Pokemon:
    def __init__(self, id, nome, altura, peso, tipo):
        self.__id = id
        self.__nome = nome
        self.__altura = altura
        self.__peso = peso
        self.__tipo = tipo

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def altura(self):
        return self.__altura

    @property
    def peso(self):
        return self.__peso

    @property
    def tipo(self):
        return self.__tipo

    @id.setter
    def id(self, novo_id):
        self.__id = novo_id

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @altura.setter
    def altura(self, nova_altura):
        self.__altura = nova_altura

    @peso.setter
    def peso(self, novo_peso):
        self.__peso = novo_peso

    def __str__(self):
        return str(f'{self.__nome}')
