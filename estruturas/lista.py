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
                novo = Node(dado)
                novo.prox = self.__head
                self.__head = novo
                self.__tamanho += 1
                return

            cursor = self.__head
            contador = 1

            while (contador < posicao - 1) and (cursor != None):
                cursor = cursor.prox
                contador += 1

            if cursor == None:
                raise EstruturaException('A posição é inválida para inserção')

            novo = Node(dado)
            novo.prox = cursor.prox
            cursor.prox = novo
            self.__tamanho += 1

        except TypeError:
            raise EstruturaException('A posição deve ser um valor inteiro')
        except AssertionError:
            raise EstruturaException('Posição negativa não é valida')
        except:
            raise

    def remover(self, posicao):
        try:
            assert posicao > 0

            if self.vazia():
                raise EstruturaException('A lista está vazia')

            cursor = self.__head
            contador = 1

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

    def elemento(self, posicao):
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

    def busca_por(self, chave, dado):
        try:
            if self.vazia():
                raise EstruturaException('A lista está vazia')

            lista = []
            cursor = self.__head
            contador = 1
            ocorre = 0

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

    def __str__(self):
        saida = 'Lista: ['
        cursor = self.__head

        while cursor != None:
            saida += f'{str(cursor.dado)}'
            cursor = cursor.prox
            if cursor != None:
                saida += ', '

        saida += ']'
        return saida

    def ordena_por(self, chave):
        for i in range(self.__tamanho-1):
            atual = self.__head
            seguinte = atual.prox
            anterior = None
            while seguinte:
                if getattr(atual.dado, chave) > getattr(seguinte.dado, chave):
                    if anterior == None:
                        anterior = atual.prox
                        seguinte = seguinte.prox
                        anterior.prox = atual
                        atual.prox = seguinte
                        self.start = anterior
                    else:
                        temp = seguinte
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
