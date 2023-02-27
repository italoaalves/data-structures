from structures.exceptions import StructureException
from structures.node import Node


class LinkedStack:
    def __init__(self) -> None:
        self.__head = None
        self.__size = 0

    @property
    def head(self) -> object:
        return self.__head

    @head.setter
    def head(self, new_head: object = None) -> None:
        self.__head = new_head

    @property
    def size(self) -> int:
        return self.__size

    def is_empty(self) -> bool:
        if self.__size == 0:
            return True

    def insert(self, data: object) -> None:
        node = Node(data)

        if self.is_empty():
            self.__head = node
            node.next = None
            self.__size += 1
        else:
            node.next = self.__head
            self.__head = node
            self.__size += 1

    def remove(self) -> None:
        if self.is_empty():
            raise StructureException('A fila está vazia')
        self.__head = self.__head.next
        self.__size -= 1

    def element(self) -> object:
        if(self.is_empty()):
            raise StructureException('A pilha está vazia')
        return self.__head.data

    def __str__(self) -> str:
        output: str = 'Pilha: ['
        cursor: object = self.__head

        while cursor != None:
            output += f'{str(cursor.data)}'
            cursor = cursor.next

            if cursor != None:
                output += ', '

        output += ']'
        return output
