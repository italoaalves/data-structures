def mergesort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)

    if(fim - inicio > 1):
        meio = (fim + inicio)//2
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)

        esquerda = lista[inicio:meio]
        direita = lista[meio:fim]

        topo_esquerda = 0
        topo_direita = 0

        for k in range(inicio, fim):
            if topo_esquerda >= len(esquerda):
                lista[k] = direita[topo_direita]
                topo_direita += 1

            elif topo_direita >= len(direita):
                lista[k] = esquerda[topo_esquerda]
                topo_esquerda += 1

            elif esquerda[topo_esquerda] < direita[topo_direita]:
                lista[k] = esquerda[topo_esquerda]
                topo_esquerda += 1

            else:
                lista[k] = direita[topo_direita]
                topo_direita += 1


# debug
if __name__ == "__main__":
    lista = [2, 1, 3, 4, 6, 5]
    mergesort(lista)
    print(lista)
