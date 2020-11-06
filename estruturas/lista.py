from estruturas.excecoes import EstruturaException
from estruturas.no import Node


class ListaEncadeada:
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

    def inserir(self, posicao, dado):
        try:
            assert posicao > 0

            if self.vazia():
                if posicao != 1:
                    raise EstruturaException(
                        'lista vazia, insira apenas na posição 1')
                self.__head = Node(dado)
                self.__tamanho += 1
                return

            if posicao == 1:
                no = Node(dado)
                no.prox = self.__head
                self.__head = no
                self.__tamanho += 1
                return

            cursor = self.__head
            contador = 1

            while (contador < posicao - 1) and (cursor != None):
                cursor = cursor.prox
                contador += 1

            if cursor == None:
                raise EstruturaException('A posição é inválida para inserção')

            no = Node(dado)
            no.prox = cursor.prox
            cursor.prox = no
            self.__tamanho += 1

        except TypeError:
            raise EstruturaException('A posição deve ser um valor inteiro')
        except AssertionError:
            raise EstruturaException('Posição negativa não é valida')
        except:
            raise

    def remover(self, posicao) -> None:
        try:
            assert posicao > 0

            if self.vazia():
                raise EstruturaException('A lista está vazia')

            cursor: object = self.__head
            contador: int = 1

            while (contador <= posicao - 1) and (cursor != None):
                anterior = cursor
                cursor = cursor.prox
                contador += 1

            if cursor == None:
                raise EstruturaException('Posição inválida para remoção')

            if posicao == 1:
                self.__head = cursor.prox

            else:
                anterior.prox = cursor.prox

            self.__tamanho -= 1

        except TypeError:
            raise EstruturaException('A posição deve ser um valor inteiro')
        except AssertionError:
            raise EstruturaException('Posição negativa não é valida')
        except:
            raise

    def elemento(self, posicao) -> object:
        try:
            assert posicao > 0

            if self.vazia():
                raise EstruturaException('A lista está vazia')
            cursor = self.__head
            contador = 1

            while (contador <= posicao - 1) and (cursor != None):
                cursor = cursor.prox
                if contador == posicao - 1:
                    return cursor.dado
                else:
                    contador += 1

            if cursor == None:
                raise EstruturaException('Posição inválida para busca')

            if posicao == 1:
                return self.__head

        except TypeError:
            raise EstruturaException('A posição deve ser um valor inteiro')
        except AssertionError:
            raise EstruturaException('Posição negativa não é valida')
        except:
            raise

    def busca_por(self, chave, dado) -> list:
        try:
            if self.vazia():
                raise EstruturaException('A lista está vazia')

            lista: list = []
            cursor: object = self.__head
            contador: int = 1
            ocorre: int = 0

            while cursor != None:
                if getattr(cursor.dado, chave) == dado:
                    lista.append(cursor.dado)
                    ocorre += 1
                else:
                    contador += 1
                cursor = cursor.prox

            if ocorre == 0:
                raise EstruturaException('Pokemon não registrado na pokedex')

            else:
                return lista

        except TypeError:
            raise EstruturaException('A posição deve ser um valor inteiro')
        except AssertionError:
            raise EstruturaException('Posição negativa não é valida')
        except:
            raise

    def __str__(self) -> str:
        saida: str = 'Lista: ['
        cursor: object = self.__head

        while cursor != None:
            saida += f'{str(cursor.dado)}'
            cursor = cursor.prox
            if cursor != None:
                saida += ', '

        saida += ']'
        return saida

    def ordena_por(self, chave) -> None:
        for i in range(self.__tamanho-1):
            atual: object = self.__head
            seguinte: object = atual.prox
            anterior: object = None
            while seguinte:
                if getattr(atual.dado, chave) > getattr(seguinte.dado, chave):
                    if anterior == None:
                        anterior = atual.prox
                        seguinte = seguinte.prox
                        anterior.prox = atual
                        atual.prox = seguinte
                        self.start = anterior
                    else:
                        temp: object = seguinte
                        seguinte = seguinte.prox
                        anterior.prox = atual.prox
                        anterior = temp
                        temp.prox = atual
                        atual.prox = seguinte
                else:
                    anterior = atual
                    atual = seguinte
                    seguinte = seguinte.prox
            i = i+1
