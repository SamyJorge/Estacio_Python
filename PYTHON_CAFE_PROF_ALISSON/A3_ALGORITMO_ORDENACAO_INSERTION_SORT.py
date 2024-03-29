# INSERTION SORT - ORDENAÇÃO POR INSERÇÃO
import random

def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = chave



lista = [4, 7, 5, 1, 8, 3]
lista2 = random.sample(range(1, 100), 20)

insertion_sort(lista)
insertion_sort(lista2)

print(lista)
print(lista2)

