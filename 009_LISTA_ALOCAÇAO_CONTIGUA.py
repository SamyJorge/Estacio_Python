# LISTAS DE ALOCAÇÃO CONTIGUA
"""
Buscando o indice de uma chave usando a função index do Python. """
"""
amigos = ['Arthur', 'João', 'Maria', 'Ana']
n = amigos.index('Ana')
x = amigos.index('João')
print('Ana tem indice =>', n)
print('João tem indice =>', x)
"""
# Minha solução:
"""
def indice(chave):
    indice = pessoas.index(chave)
    print(f'O indice de {chave} é {indice}')

nome = input('Buscar Nome: ')
procure = indice(nome)
"""

# Caso deseje implementar sua própria busca:
# Criamos uma função para percorrer a lista.
# Essa função reberá por parametro o seguinte:
# k = Chave do elemento buscado | L = nome da lista | n = Tamanho da lista

"""
meninas = ['Anna', 'Maria', 'Clara', 'Livia']

def buscaLista( k, L, n):
    i = 0                  # Iterador - determinando a busca a partir do indice 0
    indiceL = -1           # Se encontrar armazena o indice buscado ou retorna -1(erro)
    while i < n:           # Enquanto não chegar o final da lista
        if L[i] == k:      # Se o elemento de indice i de L(lista) for igual a k
            indiceL = i    # indiceL recebe como valor o indice encontrado
            i = n + 1      # Saia do laço (i = conprimento + 1)
        i = i + 1          # Volta ao início do laço
    return indiceL         # Retorna o indice buscado ou retorna -1(erro)

indice = buscaLista('eva', meninas, len(meninas))  # Chamando a função enviando os Paramentros
print('Indice encontrado: ', indice)"""



# Outro caso.
""" No caso da lista estar ordenada por chave em ordem crescente, 
podemos melhorar a busca fazendo o laço acabar, caso a chave
encontrada seja maior do que a chave buscada. """

"""def buscaOrdenada(k, L, n):
    i = 0                # Interador - determinando a busca a partir do indice 0
    indiceL = -1         # Armazena o indice buscado ou retorna -1(erro)
    while i < n:         # Enquanto não chegar o final da lista
        if L[i] >= k:    # Se o elemento de indice i de L(lista) for maior ou igual a k
            if L[i] == k:    # Se o elemento de indice i de L(lista) for igual a k
                indiceL = i  # indiceL recebe como valor o indice encontrado
                i = n + 1    # Saia do laço (i = conprimento + 1)
            else:            # Se não
                i = n + 1    # chave > k então saia do laço (i = tam. da lista + 1)
        else:
            i = i + 1
    return indiceL

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = buscaOrdenada(7, num, len(num))
print(i)"""


# INSERÇÃO EM LISTA EM ALOCAÇÃO CONTIGUA
# Usando append inserimos ao fim da lista um novo indice(nó).

"""amigos =['Estela', 'Glaucio']
amigos.append('Iago')
print(amigos)"""


# INSERINDO DINAMICAMENTE
# Criaremos uma função p/ inserir espaço vazio(um nó) na lista.
# Inserir um elemento novo.
# Incrementar o tamnho em +1

"""cont = ['1', '2', '3']

def inserirL(k, L, n):
    L.append('')            # Insere um espaço a lista
    L[n] = k                # Insere o valor do elememto k recebido por parametro no fim da lista
    n += 1                  # Incremento p/ almentar lista em um espaço
    return L                # Retorna lista incrementada (sem essa linha por padrão retornaria none)

cont = inserirL('4', cont, len(cont))
print(cont)"""


# NUMA LISTA CONTIGUA ORDENADA POR CHAVES CRESCENTES
"""
Caso a sua lista esteja ordenada por chave, em ordem crescente, o processo
de inserção é mais complicado, pois temos que buscar a posição correta para
inserir o novo nó.
Todos os nós posteriores terão que ser “empurrados” uma posição à frente,
para abrir espaço, além disso, caso a chave buscada já exista na lista,
não poderemos inserir o nó, o que deve gerar um erro."""

# Parte 1 - Função busca a posição p/ inserir o elemento na posição correta.
"""def insereOrdenada(k, L, n):
    i = 0                     # iniciar busca no indice 0
    posInserir = -1           # Armazena o indice encontrado

    while i < n:
        if L[i] >= k:
            if L[i] == k:          # Se existir elem. identico retorne erro
                return -1
            else:
                posInserir = i     # Salva o indice
                i = n + 1          # Sai do laço
        else:
            i = i + 1              # Segue a procura

        if i == n:              # Encontrando o ultimo item da lista faça:
            posInserir = n      # Armazene o indice desse ultimo elemento

# Parte 2 - Aumenta o tamanho da lista, empura os nós pra traz e insere o elemento.
    L.append('')                # Aumenta o tamanho da lista
    i = n                       # inicio do ajuste da lista
    while i > posInserir:       
        L[i] = L[i - 1]         # Empurra cada nó pro final
        i = i - 1
    L[posInserir] = k           # Insere novo nó
    #return posInserir
    return numer

numer = [1, 2, 3, 4, 6, 7, 9, 10]

numer = insereOrdenada(11, numer, len(numer))
print(numer)

numer = insereOrdenada(5, numer, len(numer))
print(numer)
"""


# Remoção em lista em alocação contígua
""" O Python tem duas funções para isso:
remove -> Busca e remove pela chave ex.: nomeLista.remove('Jorge')
pop -> Busca e remove pelo indice ex.: nomeLista.pop(5)
"""
"""
nomes = ['João', 'Maria', 'Ana', 'José']
nomes.remove('Ana')
print(nomes)
nomes.pop(2)
print(nomes)
"""


""" Caso você queira implementar manualmente a remoção, o código a seguir
exemplifica essa operação. No caso, você possui uma lista "L" com "n" nós
e quer remover um nó de chave k """


def remover(k, L, n):
# Parte 1 - Procura o indice da chave caso ela exista na lista.
    i = 0                      # Inicio da busca pelo indice 0
    posRemocao = -1            # Variável que armazenará o indice achado

    while i < n:
        if L[i] == k:
            posRemocao = i     # Chave encontrada, armazene o indice em posRemocao
            i = n + 1          # Sair do laço
        else:
            if L[i] > k:       # Se chave na lista for maior que k (buscado)
                return -1      # Erro, Chave inesistente
            i += 1             # Continuar procurando
    if i == n:
        return -1              # Retorne erro, chave não encontrada.

# Parte 2 - Faz a remoção e ajusta o tamanho da lista.
    i = posRemocao
    while i < n - 1:
        L[i] = L[i + 1]       # Puxa cada nó posterior 1 posição
        i += 1                # i recebe o proximo nó
    L.pop(n - 1)               # Ajusta o tamanho da lista para menos

    return nomes


nomes = ['João', 'Maria', 'Ana', 'José']
nomes = remover('João', nomes, len(nomes))
print(nomes)


