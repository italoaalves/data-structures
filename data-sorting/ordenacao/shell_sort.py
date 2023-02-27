def shellsort(lista):
    aux = len(lista)//2
    indice = len(lista)//2
    incremento = len(lista)//2
    incremento_indice = (len(lista)//2)

    while incremento > 0:
        incremento_indice = incremento

        while incremento_indice < len(lista):
            aux = lista[incremento_indice]
            indice = incremento_indice

            while indice >= incremento and aux < lista[indice - incremento]:
                lista[indice] = lista[indice - incremento]
                indice -= incremento

            lista[indice] = aux
            incremento_indice += 1

        incremento = incremento//2


# debug
if __name__ == "__main__":
    lista = [2, 1, 3, 4, 6, 5]
    shellsort(lista)
    print(lista)
