class Exceptions(Exception):
    
    def __init__(self,mensagem):
        super().__init__(mensagem)





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


        

class Node:
    
    def __init__(self, dado = None):
        self.__dado = dado
        self.__prox = None

    @property
        
    def dado(self):
        return self.__dado

    @property

    def prox(self):
        return self.__prox

   
    @dado.setter
        
    def dado(self, novoDado):
        self.__dado = novoDado
    
    @prox.setter
        
    def prox(self, novoProx):
        self.__prox = novoProx

    def __str__(self):
        return str(self.__dado)





    
    
            
class FilaEncadeada:
    
    def __init__(self):
        self.__inicio = None
        self.__tamanho = 0

    def vazia(self):
        if self.__tamanho == 0:
            return True
    
    def tamanho(self):
        return self.__tamanho

    def remover(self):
      if self.vazia():
        raise Exceptions('A fila está vazia')
      self.__inicio = self.__inicio.prox
      self.__tamanho -= 1

    def elemento(self):
        if(self.vazia()):
            raise Exceptions('A fila está vazia')
        return self.__inicio

    def inserir(self, dado):
        cursor = self.__inicio
        
        if self.vazia():
            no = Node(dado)
            self.__inicio = no
            no.prox = None
            self.__tamanho += 1
        else:
            while cursor != None:
                ultimo_elem = cursor
                cursor = cursor.prox
            no = Node(dado)
            no.prox = ultimo_elem.prox
            ultimo_elem.prox = no
            self.__tamanho += 1

    def remover(self):
        if self.vazia():
            raise Exceptions('A fila está vazia')
        self.__inicio = self.__inicio.prox
        self.__tamanho -= 1

    def __str__(self):
        saida = 'Fila: ['
        cursor = self.__inicio

        while cursor != None:
          saida += f'{cursor.dado}'
          cursor = cursor.prox

          if cursor != None:
            saida += ', '
    
        saida += ']'
        return saida





    


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
                    raise Exceptions('lista vazia, insira apenas na posição 1')
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
                raise Exceptions('A posição é inválida para inserção')
            novo = Node(dado)
            novo.prox = p.prox
            p.prox = novo
            self.__tamanho += 1
            
        except TypeError:
            raise Exceptions('A posição deve ser um valor inteiro')
        except AssertionError:
            raise Exceptions('Posição negativa não é valida')
        except:
            raise

    def remover(self, posicao):
        try:
            assert posicao > 0

            if self.vazia():
                raise Exceptions('A lista está vazia')
            p = self.__head
            contador = 1

            while (contador <= posicao - 1) and (p != None):
                anterior = p
                p = p.prox
                contador += 1

            if p == None:
                raise Exceptions('Posição inválida para remoção')
            dado = p.dado

            if posicao == 1:
                self.__head = p.prox

            else:
                anterior.prox = p.prox
            
        except TypeError:
            raise Exceptions('A posição deve ser um valor inteiro')
        except AssertionError:
            raise Exceptions('Posição negativa não é valida')
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



class PilhaEncadeada:

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

    def inserir(self, dado):
        cursor = self.__head
        
        if self.vazia():
            no = Node(dado)
            self.__head = no
            no.prox = None
            self.__tamanho += 1
            
        else:            
               
            no = Node(dado)
            no.prox = self.__head
            self.__head = no 
            self.__tamanho += 1

    def
            raise Exceptions('A fila está vazia')
        return self.__inicio

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







 



  



    
  
        
    

  
