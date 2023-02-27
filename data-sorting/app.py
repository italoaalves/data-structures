import random
from time import time
from copy import copy

from ordenacao.bubble_sort import bubblesort
from ordenacao.insertion_sort import insertionsort
from ordenacao.merge_sort import mergesort
from ordenacao.quick_sort import quicksort
from ordenacao.shell_sort import shellsort


def mede_tempo(metodo, lista):
    inicio = time()
    metodo(lista)
    fim = time()

    return fim - inicio


li = [random.randint(1, 5000) for i in range(20000)]


if __name__ == "__main__":
    print("Rodando bubble sort...")
    tempo_bubble = mede_tempo(bubblesort, copy(li))

    print("Rodando insertion sort...")
    tempo_insertion = mede_tempo(insertionsort, copy(li))

    print("Rodando merge sort...")
    tempo_merge = mede_tempo(mergesort, copy(li))

    print("Rodando quick sort...")
    tempo_quick = mede_tempo(quicksort, copy(li))

    print("Rodando shell sort...")
    tempo_shell = mede_tempo(shellsort, copy(li))

    print(f'''
    Tempo de execução dos algoritmos:

    Bubble: {tempo_bubble:.4f} segundos
    Insertion: {tempo_insertion:.4f} segundos
    Merge: {tempo_merge:.4f} segundos
    Quick: {tempo_quick:.4f} segundos
    Shell: {tempo_shell:.4f} segundos
    ''')
