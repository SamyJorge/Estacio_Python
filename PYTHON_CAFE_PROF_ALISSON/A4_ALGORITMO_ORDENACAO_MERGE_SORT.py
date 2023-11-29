# MERGE SORT
import random as rd

def mergesort(lista, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista)

    if(fim - inicio > 1):
        meio = (fim + inicio)//2
        mergesort(lista, inicio, meio)     #Primeria div. do inicio até o meio (lado direito)
        mergesort(lista, meio, fim)        #Segunda div. do meio até o fim  (lado esquerdo)
        merge(lista, inicio, meio, fim)    #Chama a função Merge

def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0

    for k in range(inicio, fim):
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right += 1
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left += 1
        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left += 1
        else:
            lista[k] = right[top_right]
            top_right += 1

#LISTAS
aleatoria = rd.sample(range(1, 50), 20)
desordenada = [4, 7, 2, 6, 4, 1, 8, 3]
inversa = [9, 8, 7, 6, 5, 4, 3, 2, 1]
repetida = [7, 7, 7, 1, 1, 0, 9, 9, 4, 5, 4, 5, 6, 1]

# TESTANDO
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
        mergesort(lista)
        print('\n Ordenado:')
        print(lista)

