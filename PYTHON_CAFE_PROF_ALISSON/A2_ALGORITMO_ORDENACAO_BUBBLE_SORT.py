# 1- Função que recebera por parametro nome da lista
# 2- Variável para guardar o tamanho da lista (len(lista))
# 3- Percorer cada item (for i in ...)
# 4- Comparar item é maior que o proximo item (x > x+1)
# 5- Fazer a troca de posição caso item seja maior que o proximo

import random as rd   # importando biblioteca para usar nos testes

def bubble_sort(lista):
    n = len(lista)
    for i in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                # Troca a posição dos elementos
                lista[i], lista[i+1] = lista[i+1], lista[i]



# TESTES

# Gerar vinte numeros aletórios entre 1 e 100
numeros_aleatorios = rd.sample(range(1, 100), 20)

inverso = [117, 90, 88, 83, 77, 74, 69, 64, 50, 22, 16, 8, 5, 2, 1]
repetidos = [7, 7, 7, 1, 1, 0, 4, 4, 4, 4, 3, 2, 2,]

if __name__ == "__main__":
    lista = numeros_aleatorios
    print('Lista desordenada: \n',lista)
    bubble_sort(lista)
    print('Lista após ser ordenada: \n', lista)
    bubble_sort(repetidos)
    print('Lista repetidos após oredenação: \n', repetidos)