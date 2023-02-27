from typing import Union
from structures.exceptions import StructureException
from structures.node import Node


class LinkedList:
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

    def insert(self, position: int, data: object) -> None:
        try:
            assert position > 0
            if self.is_empty():
                if position != 1:
                    raise StructureException(
                        'lista vazia, insira apenas na posição 1')
                self.__head = Node(data)
                self.__size += 1
                return
            if position == 1:
                node = Node(data)
                node.next = self.__head
                self.__head = node
                self.__size += 1
                return

            cursor = self.__head
            count = 1

            while (count < position - 1) and (cursor != None):
                cursor = cursor.next
                count += 1

            if cursor == None:
                raise StructureException('A posição é inválida para inserção')

            node = Node(data)
            node.next = cursor.next
            cursor.next = node
            self.__size += 1

        except TypeError:
            raise StructureException('A posição deve ser um valor inteiro')
        except AssertionError:
            raise StructureException('Posição negativa não é valida')
        except:
            raise

    def remove(self, position: int) -> None:
        try:
            assert position > 0

            if self.is_empty():
                raise StructureException('A lista está vazia')

            cursor: object = self.__head
            count: int = 1

            while (count <= position - 1) and (cursor != None):
                previous = cursor
                cursor = cursor.next
                count += 1

            if cursor == None:
                raise StructureException('Posição inválida para remoção')

            if position == 1:
                self.__head = cursor.next

            else:
                previous.next = cursor.next

            self.__size -= 1

        except TypeError:
            raise StructureException('A posição deve ser um valor inteiro')
        except AssertionError:
            raise StructureException('Posição negativa não é valida')
        except:
            raise

    def element(self, position: int) -> object:
        try:
            assert position > 0

            if self.is_empty():
                raise StructureException('A lista está vazia')
            cursor = self.__head
            count = 1

            while (count <= position - 1) and (cursor != None):
                cursor = cursor.next
                if count == position - 1:
                    return cursor.data
                else:
                    count += 1

            if cursor == None:
                raise StructureException('Posição inválida para busca')

            if position == 1:
                return self.__head.data

        except TypeError:
            raise StructureException('A posição deve ser um valor inteiro')
        except AssertionError:
            raise StructureException('Posição negativa não é valida')
        except:
            raise

    def search_by(self, key: str, data: Union[str, int]) -> list:
        try:
            if self.is_empty():
                raise StructureException('A lista está vazia')

            found_list = []
            cursor = self.__head
            count = 1
            found = 0

            while cursor != None:
                if getattr(cursor.data, key) == data:
                    found_list.append(cursor.data)
                    found += 1
                else:
                    count += 1
                cursor = cursor.next

            if found == 0:
                raise StructureException('Pokemon não registrado na pokedex')

            else:
                return found_list

        except TypeError:
            raise StructureException('A posição deve ser um valor inteiro')
        except AssertionError:
            raise StructureException('Posição negativa não é valida')
        except:
            raise

    def order_by(self, key: str) -> None:
        for i in range(self.__size-1):
            current = self.__head
            next = current.next
            previous = None
            while next:
                if getattr(current.data, key) > getattr(next.data, key):
                    if previous == None:
                        previous = current.next
                        next = next.next
                        previous.next = current
                        current.next = next
                        self.start = previous
                    else:
                        temp: object = next
                        next = next.next
                        previous.next = current.next
                        previous = temp
                        temp.next = current
                        current.next = next
                else:
                    previous = current
                    current = next
                    next = next.next
            i = i+1

    def __str__(self) -> str:
        output: str = 'Lista: ['
        cursor: object = self.__head

        while cursor != None:
            output += f'{str(cursor.data)}'
            cursor = cursor.next
            if cursor != None:
                output += ', '

        output += ']'
        return output
