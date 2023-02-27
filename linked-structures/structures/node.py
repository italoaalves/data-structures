class Node:
    def __init__(self, data=None) -> None:
        self.__data: object = data
        self.__next = None

    @property
    def data(self) -> object:
        return self.__data

    @property
    def next(self) -> object:
        return self.__next

    @data.setter
    def data(self, new_data) -> None:
        self.__data = new_data

    @next.setter
    def next(self, new_next) -> None:
        self.__next = new_next

    def __str__(self) -> str:
        return str(self.__data)
