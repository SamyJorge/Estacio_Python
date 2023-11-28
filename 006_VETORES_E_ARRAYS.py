# VETORES E ARRAYS

# MANIPULANDO ARRAYS

""" familia = ['Marcia', 'Samy', 'Iago']
print(familia)"""


# append -Acrescentar no fim do array

""" familia.append('Augusto')
print(familia) """

# remove - Remover elemento pelo nome(chave).
"""
familia.remove('Leia')
print(familia)
"""

# pop - Remover elemento pelo indice.

""" familia.pop(1)
print(familia) """


# OUTRA FORMA DE MANIPULAR VETORES E ARRAYS -> USANDO BIBLIOTECAS
# NUMPY
"""
Para usar arrays diretamente no python pecisamos importar a biblioteca NUMPY.

Importante:
Ao contrário das listas o array da biblioteca Numpy só permite o uso de
elementos de um mesmo tipo (int, float, string ...).
Utilizando “as np”, após o nome do pacote, estamos atribuindo um apelido
para o mesmo que é utilizado apenas para simplificar o código, e podemos
atribuir o apelido que quisermos.
"""
import numpy as np

""" nomes = np.array(['João', 'Maria', 'Ana'])
print('Array original => ',nomes)"""


# copy: cria cópia independente que se for manipulada não afeta o array original.
"""
amigos = np.array(["João", "Roberto"])
copia = amigos.copy()                      # Fazer cópia do array amigos
copia[0] = 'Nelson'                        # Acrescentar Nelson no indice 0, susbstituindo o valor 'João'.
print('Array original =>', amigos)
print('Copiado com modificação no indice 0 =>',copia)
"""


# view: Usando uma nova variável criamos uma refenencia ao array original, uma imagem,
# que ao ser manipulada afetará também o array original.
"""
nomes = np.array(['Carlos', 'Julio'])
visao = nomes.view()                   # Cria uma cópia(imagem) do array nomes.
visao[0] = 'Julio'                     # Substituir João por Julio e afetará também o aray original.
print(nomes)
print(visao)
"""


# enumerate:
""" Percorre o array e cria uma cópia retornando uma lista apresentando cada elemento
com seus respectivos indices.  A sáida será:  0-Arara   1-Papagaio   2-Perequito
"""
"""
aves = np.array(['Arara', 'Papagaio', 'Perequito'])
for indice, valor in enumerate(aves):   # Para cada indice e valor do array aves
    print(indice, valor)                # Imprima indice e valor
"""


# comando len (do ingles length) - retorna o tamanho, comprimento do array,
# a quantidade de itens.
"""
funcionarios = np.array(["Maria"])
x = len(funcionarios)
print('Empresa com {} funcionario(s)'.format(x))
"""


# Iterando sobre a lista - Precorrer todos os elementos
"""
Outra necessidade comum em um array é a de percorrê-lo elemento por elemento.
Em Python, você pode iterar sobre a lista (elemento por elemento)  usando
o laço for, como código a seguir: """
"""
parentes = ['Pai', 'Mãe', 'Irmão']
for x in parentes :
    print(x)
"""


# Acessando um elemento do array
# usamos: nome_do_array[indice]

"""parentes = ['Pai', 'Mãe', 'Irmão']
print('Eu amo minha', parentes[1])
print('Também amo meu {} e meu {}'.format(parentes[0], parentes[2]))"""


# Você pode também acessar os elementos contando de trás para frente, usando índices negativos.
"""parentes = ['Pai', 'Mãe', 'Irmão']
print('Eu amo minha', parentes[-2])"""


# .dtype - Identificando o tipo de array
"""
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.5, 3.9, 4.1])
z = np.array(['Samy', 'Jorge', 'Ramos'])
print(x.dtype)
print(y.dtype)
print(z.dtype)
"""

# Determinando o tipo de dado do array
"""
num = np.array([1, 2, 3], dtype='S')  # S = string 
print(num.dtype)
"""