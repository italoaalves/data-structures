def bubblesort(lista):
    tam = len(lista)
    cont = tam
    aux = 0

    while cont >= 0:
        for j in range(tam-1):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux

        cont -= 1


# debug
if __name__ == "__main__":
    lista = [2, 1, 3, 4, 6, 5]
    bubblesort(lista)
    print(lista)
