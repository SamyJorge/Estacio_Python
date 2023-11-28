# SELECTION SORT - OREDENAÇÃO POR SELEÇÃO
import random

def selection_sort(lista):
    n = len(lista)
    for j in range(n-1):
        min_index = j
        for i in range(j, n):
            if lista[i] < lista[min_index]:
                min_index = i
        if lista[j] > lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux

lista = [7, 5, 1, 8, 3]
lista2 = random.sample(range(1, 100), 20)

selection_sort(lista)
selection_sort(lista2)
print(lista)
print(lista2)

