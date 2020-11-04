class Dado:
    def __init__(self, dado0, dado1, dado2):
        self.__dado0 = dado0
        self.__dado1 = dado1
        self.__dado2 = dado2

    @property
    def dado0(self):
        return self.__dado0

    @property
    def dado1(self):
        return self.__dado1

    @property
    def dado2(self):
        return self.__dado2

    @dado0.setter
    def dado0(self, novoDado):
        self.__dado0 = novoDado

    @dado1.setter
    def dado1(self, novoDado):
        self.__dado1 = novoDado

    @dado2.setter
    def dado2(self, novoDado):
        self.__dado2 = novoDado

    def __str__(self):
        return str(f'[{self.__dado0}, {self.__dado1}, {self.__dado2}]')
