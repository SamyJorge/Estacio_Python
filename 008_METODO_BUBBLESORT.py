# MÉTODO BUBBLESORT - MÉTODO DE BOLHA (Método da ordenação por bolha.)
"""
O nome desse algoritmo vem da ideia de flutuar um elemento por vez para
o fim da lista, como se fosse um conjunto de bolhas flutuando para o topo
de um líquido.
"""
"""
A ideia do método Bubblesort é você iniciar com um array contendo a lista desordenada.
Então, o algoritmo vai percorrer o array fazendo trocas par a par entre dois elementos
consecutivos, quando estiverem fora da ordem. Ao chegar ao final do array, você
recomeça do início, encerrando o algoritmo quando uma das passagens não realizar nenhuma
troca (o que significa que o array está ordenado).
"""

# Função para fazer a troca de posição dos números da lista.
"""
def trocar(seq, i):
    tmp = seq[i]
    seq[i] = seq[i + 1]
    seq[i + 1] = tmp

sequencia = [9, 3, 8, 1, 5, 10, 7, 6, 4]   # Lista desordenada
troca = 1

while troca:
    troca = 0
    i = 0
    for i in range(0, len(sequencia)-1):       # Percorrer de 0 até o penultimo item
        if sequencia[i] > sequencia[i + 1]:    # Se o elemento for maior que o proximo.
            trocar(sequencia, i)               # chama a função trocar
            troca = 1
print(sequencia)
"""

# EXEMPLO II
"""
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i] > alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1

alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)
"""


# EXEMPLO III
"""
def Bubble(lista):
    troca = True

    while troca:
        troca = False
        for i in range(len(lista)-1):
            if lista[i] > lista[i + 1]:
                troca = True
                tmp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = tmp


lista = [100, 80, 90, 70, 40, 60, 50]
Bubble(lista)
print('Lista ordenada: ', lista)
"""

# EXEMPLO IV
# O bubble sort pode ter a vantagem de reconhecer a lista ordenada e parar.
"""
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1

alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)
"""

