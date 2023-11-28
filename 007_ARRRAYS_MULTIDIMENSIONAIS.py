# ARRAYS MULTIDIMENSIONAIS - ARRAY DE ARRAYS - MATRIZES
"""
O uso de dados multidimensionais em Python pode ser feito, assim como no caso
unidimensional, por meio do uso de listas ou de arrays com a biblioteca numpy.
O jeito mais simples de tratar dados multidimensionais em Python é utilizando
listas. Elas são uma abstração fundamental da linguagem Python e podem ser
aninhadas diversas vezes, ou seja, você pode fazer listas de listas e assim
por diante. Além disso, as listas em Python estão preparadas para ter tipos de
dados distintos, o que permite ter um elemento da lista que é uma lista e outro
apenas um número ou uma palavra (“String”).
"""

# Exemplo de como declarar uma lista multidimensional
amigos = [['João', 25, 'Portugues'],['Maria', 20],['Ana', 33, 'Brasileira']]

# append - Inserindo elementos no final da matriz.
"""
amigos.append(['Rogério', 45, 'Gaucho'])    # Adicionar essa lista no final
print(amigos)
"""

# append - Inserindo um elemento no segundo nível.
"""
amigos[1].append('Brasileira')      # Adicinar na lista de indice 1 o item Brasileira.
print(amigos)
"""

# remove - removendo do vetor um item conhecido.
"""amigos.remove(['Ana', 33,'Paulista'])
print(amigos)"""


# remove - Removendo um item do segundo nivel(indice) do vetor.
"""
amigos[1].remove('Brasileira')
print(amigos)
"""


# pop - removendo um elemento do vetor atravez do indice.

"""
amigos.pop(0)
print(amigos)

amigos[1].pop(2)  # Removendo elemento de indice 2, do elemento indice 1 da lista
print(amigos)
"""


# ITERANDO SOBRE A MATRIZ
"""
A iteração sobre uma matriz é similar ao caso do vetor, mas a cada nível de aninhamento
você pode realizar uma nova iteração. Digamos que você queira apenas imprimir a lista,
linha a linha, com cada linha contendo os dados de cada amigo.
"""

"""
for x in amigos:  # para cada item em amigos
    print(x)      # imprima x
"""


# Para imprimir cada elemento em uma linha, você pode usar dois iteradores aninhados
"""
for x in amigos:
    for y in x:
        print(y)
"""


"""
Esse código funciona bem no nosso exemplo porque todos elementos de amigos é uma lista,
mas as listas podem ter diversos tipos de elementos. O que acontece com esse último
código se, na lista amigos, tiver um elemento que contém apenas um nome, como “Mário”?
"""
"""
alunos =[['João', 25, 'Câncer'], ['Maria', 23, 'Áries'], ['Ana', 31, 'Aquário'], ['Mário']]

for x in alunos:
    for y in x:
        print(y)
"""
"""
[Mário] foi tratado indevidamente como uma lista. Para resolver esse problema, você pode
usar a função isinstance(x,list) que retorna verdadeiro se x for um objeto do tipo lista.
"""
alunos =[['João', 25, 'Branco'], ['Maria', 23, 'Preto'], ['Ana', 31, 'Moreno'], ['Mário']]
"""
for x in alunos:
    if isinstance(x, list):
        for y in x:
            print(y)
    else:
        print(x)
"""
"""
Repare que esse código só usa o iterador aninhado se o item de alto nível
for uma lista, o que é checado usando-se a função isinstance().
"""


# MATRIZES USANDO ARRAYS
"""
- Da mesma forma que no caso unidimensional, você pode preferir utilizar arrays
diretamente para representar dados multidimensionais. É importante ressaltar que,
diferentemente das listas, o objeto array deve ser homogêneo, ou seja, deve conter
elementos de mesmo tipo.
- Para ficar mais fácil entender, vamos começar declarando uma matriz usando array
da biblioteca numpy.
"""

# DECLARANDO MATRIZES COMO ARRAYS
import numpy as np
# np é um mnemonico(apelido).

# matriz1 = np.array([[1, 2], [3, 4], [5, 6]])
# matriz2 = np.array([[8, 9], [10, 11], [12, 13]])
# matriz3 = np.array([[1, 2], [3], [5, 6]])

# print(matriz1)
# print(matriz3)
"""A matriz1 foi corretamente declarada e salva como um array de arrays (uma matriz).
Já a matriz3 foi incorretamente declarada, pois o seu segundo elemento tem tamanho 1
ao invés de 2. Assim, ela foi salva como um array de listas. Retornará um erro.
"""
# Para acessar determinado elemento da matriz, podemos usar a variável seguida do
# índice entre colchetes.

# print(matriz1[0])                # imprimindo o indice 0 da matriz1
# print('Número:', matriz1[2][1])  # Selcionando o indice 2 da matriz e o elemento de indice 1


# OPERAÇÕES SIMPLES COM MATRIZES
"""
Você pode realizar operações simples, como soma e subtração, com matrizes que
tenham o mesmo tamanho de forma direta.
"""
"""matriz2 += matriz1
print('Resultado da soma de matriz2 + matriz1')
print(matriz2)

matriz2 -= matriz1
print('Resultado da subtração de matriz2 - matriz1')
print(matriz2)"""

# Podemos usar funções do numpy para cálculos simples direto na matriz.
"""
minimo = matriz1.min()
maximo = matriz1.max()
soma = matriz1.sum()
media = matriz1.mean()
desvio = matriz1.std()
"""
"""
print('Minimo = ', minimo)
print('Maximo = ', maximo)
print('Soma = ', soma)
print('Media = ', media)
print('Desvio = {:.4f}'.format(desvio))
"""

