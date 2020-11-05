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
            p = self.__head
            contador = 1

            while (contador < posicao - 1) and (p != None):
                p = p.prox
                contador += 1
            if p == None:
                raise EstruturaException('A posição é inválida para inserção')
            novo = Node(dado)
            novo.prox = p.prox
            p.prox = novo
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
            p = self.__head
            contador = 1

            while (contador <= posicao - 1) and (p != None):
                anterior = p
                p = p.prox
                contador += 1

            if p == None:
                raise EstruturaException('Posição inválida para remoção')
            dado = p.dado

            if posicao == 1:
                self.__head = p.prox

            else:
                anterior.prox = p.prox

        except TypeError:
            raise EstruturaException('A posição deve ser um valor inteiro')
        except AssertionError:
            raise EstruturaException('Posição negativa não é valida')
        except:
            raise

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
