# QUICK SORT
"""
O algoritmo QUICK SORT se baseia na ideia de pegar um elemento
da lista, como pivô, e passar os elementos maiores que esse pivô
para a direita dele e os menores para a sua esquerda.

"""

import random as rd
def quicksort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)-1
    if inicio < fim:
        p = partition(lista, inicio, fim)
        quicksort(lista, inicio, p-1)
        quicksort(lista, p+1, fim)
def partition(lista, inicio, fim):
    pivot = lista[fim]
    index = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivot:
            lista[j], lista[index] = lista[index], lista[j]
            index += 1
    lista[index], lista[fim] = lista[fim], lista[index]
    return index


#LISTAS
aleatoria = rd.sample(range(1, 50), 20)
desordenada = [4, 7, 2, 6, 4, 1, 8, 3]
inversa = [9, 8, 7, 6, 5, 4, 3, 2, 1]
repetida = [7, 7, 7, 1, 1, 0, 9, 9, 4, 5, 4, 5, 6, 1]

if __name__ == "__main__":
    test_cases = {
        'Numeros aleatório': aleatoria,
        'Desodenados': desordenada,
        'Ordem inversa': inversa,
        'Elementos repetidos': repetida,
    }

    for name, lista in test_cases.items():
        print('\nCaso de teste: {}'.format(name))
        print(lista)
        quicksort(lista)
        print('\n Ordenado:')
        print(lista)

