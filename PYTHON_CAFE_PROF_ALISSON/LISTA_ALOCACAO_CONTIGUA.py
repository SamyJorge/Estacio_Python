# Python Café - Prof. Alisson
# LISTAS CONTIGUAS
lista = []                         # Lista vazia
listaNum = [94, 7, 3, 12, 56]      # Lista uniforme - somente um tipo de elemento (int)
listaMista = ["Roger", 30, 78.5]   # Python acita tipos diferentes em listas

# Acessando elementos aleatóriamente.
# Acessando e imprimindo elemento indice 0 - primeiro elemento.

print("Na lista o elemento com indice 0 é o ", listaNum[0])

# A função python "len" retorna o tamanho da lista indicada.
# Acessando o Último elento válido (tamanho da lista - 1)
len(lista)-1  # Rertorna o indice do ultimo elemento e não seu valor.


# BUSCAS LINEARES EM LISTAS |  Complexidade O(n) |
"""Retorna indice do elemento se estiver na lista ou, caso contrario, None(não encontrado)"""

def busca(lista, elem):
    for i in range(len(lista)):  # Percorer cada elemento até o fim da lista.
        if lista[i] == elem:     # Se for identico
            return i             # Retorne o indice encontrado
    return None                  # Se não, retorne None


# Testando a função de busca criada.
# Obs. Python aceita lista compostas por varios tipos de elementos.
lista_estranha = [8, "5", 32, 0, "python", 11.3]
elemento = 11.3

indice = busca(lista_estranha, elemento)  # Chamando e passando paramentros p/ função busca.

if indice is not None:   # Se o indice não for None(vazio)
    print('Em lista_estranha o indice do element'
          'o {} é {}'.format(elemento, indice))
else:
    print('O elemento {} não existe na lista'.format(elemento))


