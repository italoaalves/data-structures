def insertionsort(lista):
    tam = len(lista)

    for i in range(1, tam):
        proximo = lista[i]
        atual = i - 1

        while proximo < lista[atual] and atual >= 0:
            lista[atual + 1] = lista[atual]
            atual -= 1

        lista[atual + 1] = proximo


# debug
if __name__ == "__main__":
    lista = [2, 1, 3, 4, 6, 5]
    insertionsort(lista)
    print(lista)
