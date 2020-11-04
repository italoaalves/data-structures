class Dado:
    def __init__(self, dado):
        self.__dado = dado

    @property
    def dado(self):
        return self.__dado

    @dado.setter
    def dado(self, novoDado):
        self.__dado = novoDado

    def __str__(self):
        return str(f'{self.__dado}')
