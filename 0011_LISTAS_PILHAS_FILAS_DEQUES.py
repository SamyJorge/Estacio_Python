# CONCEITO DE ALOCAÇÃO ENCADEADA
"""
-> Em uma lista encadeada, existe o primeiro nó da lista, para onde apontamos
   a variável da lista ou seja, a variável Lista guarda o endereço deste
   nó inicial).
-> Nessa lista, como você já viu, cada nó é composto pelos seus campos, como
   chave, nome, data etc., mas, além disso, possui um campo especial, um
   ponteiro para o próximo nó da lista.
-> Essa estrutura permite que os nós estejam salvos em espaços não contíguos
   da memória, espalhados por diversos endereços distantes entre si, mas,
   que ainda assim, seja possível percorrer a lista sem se perder.
-> Para isso, o ponteiro para o próximo nó deve armazenar o endereço em que
   está salvo o próximo nó.
-> O último nó da lista, por sua vez, aponta para um valor nulo (representado
   por lambda).
"""

# ALOCANDO ESPAÇO PARA SUA LISTA
"""
-> No caso da lista encadeada, quando você cria um nó para ser inserido nela,
   você já está alocando o espaço de memória que irá armazená-lo. Portanto,
   não precisa se preocupar em alocar previamente espaços para sua lista.
   Sua única preocupação é que, conforme a lista vai crescendo, o espaço em
   memória necessário para mantê-la aumenta a ponto de consumir o espaço
   disponível para seu programa.
-> Além disso, o tratamento dos ponteiros, apontando para os próximos nós,
   deve ser feito sempre com cuidado, pois, se você perder o apontamento
   para o próximo nó, todo o restante da lista estará perdido em endereços
   desconhecidos da memória.
"""

# O código a seguir cria a classe nó e seu construtor.

class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None

"""O próximo código cria a classe ListaEncadeada e seu construtor,
além de uma função de impressão para facilitar seus testes."""

class ListaEncadeada:
     def __init__(self, cabeca=None):
         self.cabeca = cabeca

     def print(self):
         current = self.cabeca
         while current:
             print(current.valor)
             current = current.proximo


# Lista duplamente encadeada
"""
-> Com o conceito de lista encadeada, você pode percorrer a lista apenas em
   um sentido, seguindo os ponteiros “próximo”. Existe a estrutura de lista
   duplamente encadeada, na qual um nó armazena não só o ponteiro para o
   próximo nó, como também um ponteiro para o nó anterior. Dessa forma, a
   lista pode ser percorrida em ambos os sentidos. 
-> Entretanto, você consegue apenas começar pelo primeiro nó, pois só tem a
   variável que aponta para ele. 
   Uma maneira de resolver esse problema é manter uma variável apontando para
   o último nó da lista, permitindo que você percorra a lista no sentido
   inverso, seguindo os ponteiros anteriores.
"""


# Busca em listas em alocação encadeada.
"""
No caso de termos uma lista em alocação encadeada, você pode buscar determinado
nó, por meio de sua chave, simplesmente percorrendo a lista e procurando por
essa chave.

Imagine que você possua uma lista contendo nós compostos por [chave, valor, próximo].
O código a seguir apresenta a busca por uma chave.
"""

def busca(self, k):
    noAtual = self.cabeca             # inicio da busca
    if noAtual.chave == k:
        return noAtual                #chave encontrada
    while noAtual.proximo != None:
        noAtual = noAtual.proximo     #passe pro proximo nó
        if noAtual.chave == k:
            return noAtual            #Chave encontrada
    return None                       #Chave não achada


"""
Você percebeu que antes de começar o laço temos que testar com o primeiro nó?
Isso acontece porque a lista pode conter apenas um nó. Para evitar esse problema,
você pode utilizar um artifício que chamamos de “nó cabeça”.

Atenção!
O princípio do nó cabeça é que a lista sempre terá, ao menos, um nó que não faz
parte da lista de verdade, chamado de nó cabeça, que serve apenas para evitar
essas checagens extras, ou seja, se você quiser usar um nó cabeça, ao criar
a lista vazia, na verdade, deverá criar contendo um nó (o cabeça) que não
armazena valores válidos de um campo.
"""


# Inserção em lista em alocação encadeada.
"""
Primeiramente, vamos considerar o caso da lista não ordenada. Nesse caso, você pode inserir
o novo nó ao final da lista, então, no passo 2, apontará para o valor nulo.

Caso você não tenha uma variável apontando para o final da lista, terá que percorrê-la toda
até encontrar o último nó. Ou seja, inserir ao final da lista só é eficiente se você tiver
uma variável apontando para o final da lista. O código a seguir mostra a inserção
no final da lista.
"""

def insereFinal(self, novoNo):
    noAtual = self.cabeca
    if noAtual:                            #Caso lista esteja vazia
        while noAtual.proximo:
            noAtual = noAtual.proximo    #Busca o fim da lista
            noAtual.proximo = novoNo
    else:                                    #Caso lista esteja vazia
        self.cabeca = novoNo

"""
-> Existe outra solução mais simples, caso você não queira manter uma variável para o final da lista.
-> Você pode, em vez de inserir ao final da lista, inserir novos nós no início da lista. Embora pareça
   estranho, lembre-se de que a lista não é ordenada. Nesse caso, o código é bem simples:
"""
def insereInicio(self, novoNo):
    novoNo.proximo = self.cabeca
    self.cabeca = novoNo


# Caso a Lista seja ordenada
"""
Caso a sua lista seja ordenada, o processo de inserção começa com a busca pela posição correta de
inserção, mas, ao encontrá-la, a inserção em si é simples, como as anteriores.
"""

def insereOrdenada(self, novoNo):
    noAtual = self.cabeca              #Inicio da busca da posição
    if noAtual.chave > novoNo.chave:
        novoNo.proximo = self.cabeca
        self.cabeca = novoNo           #Insere no inicio
        return 0

    if noAtual.proximo != None:
        while(noAtual.chave < novoNo.chave):
            if (noAtual.proximo == None):
                noAtual.proximo = novoNo  #insere no final da lista
                return 0
            noAnterior = noAtual
            noAtual = noAtual.proximo    #Continua a busca
                                         #Fim da busca
        novoNo.proximo = noAtual         #Aponta novo nó
        noAnterior.proximo = novoNo      #Inserir novo nó


# Remoção em lista em alocação encadeada.
"""
A terceira e última operação básica em uma estrutura de dados é a remoção de um nó.
No caso da lista encadeada, você deve buscar o nó a ser removido, e depois basta fazer o nó anterior
apontar para o nó posterior ao nó removido.
"""

def removeLista(self, k):
    noAtual = self.cabeca
    if noAtual == None:                             #Erro lista vazia
        return None
    if noAtual.chave == k:
        self.cabeca = noAtual.proximo
        return 0
    noAnterior = noAtual                            #Continua busca
    noAtual = noAtual.proximo
    while(noAtual != None):
        if noAtual.chave == k:
            noAnterior.proximo = noAtual.proximo    #removeu o nó
            return k
        else:
            noAnterior = noAtual                    #continua a busca
            noAtual = noAtual.proximo
    return -1                                       #Erro chave não encontrada



e0 = No(0,'Joao')
Lista = ListaEncadeada(e0)

k0 = Lista.busca(0)
print(k0.valor)
Lista.print()

e1 = No(1,'Maria')
Lista.insereFinal(e1)
Lista.print()

e2=No(-1,'Ana')
Lista.insereInicio(e2)
Lista.print()

e3=No(2,'Arthur')
Lista.insereOrdenada(e3)
Lista.removeLista(2)
Lista.print()
