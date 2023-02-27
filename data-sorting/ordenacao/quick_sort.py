def quicksort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1

    if inicio < fim:
        p = lista[fim]
        indice = inicio

        for j in range(inicio, fim):
            if lista[j] <= p:
                lista[j], lista[indice] = lista[indice], lista[j]
                indice += 1

        lista[indice], lista[fim] = lista[fim], lista[indice]

        quicksort(lista, inicio, indice-1)
        quicksort(lista, indice + 1, fim)


if __name__ == "__main__":
    lista = [2, 1, 3, 4, 6, 5]
    quicksort(lista)
    print(lista)
