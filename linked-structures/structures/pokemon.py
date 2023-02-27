class Pokemon:
    def __init__(self, id, name, height, weight, type):
        self.__id = id
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__type = type

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def height(self):
        return self.__height

    @property
    def weight(self):
        return self.__weight

    @property
    def type(self):
        return self.__type

    @id.setter
    def id(self, new_id):
        self.__id = new_id

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @height.setter
    def height(self, nova_altura):
        self.__height = nova_altura

    @weight.setter
    def weight(self, novo_peso):
        self.__weight = novo_peso

    def __str__(self):
        return str(f'{self.__name}')
