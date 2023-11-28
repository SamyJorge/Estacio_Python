# ARVORES EM PYTHON
"""
Árvores (trees) são estruturas de dados hierárquicas e não linearizadas.
Basicamente, as árvores são formadas por um conjunto de elementos, que
chamamos de nós (ou nodos ou vértices), conectados por um conjunto de
arestas. Um dos nós, que dizemos estar no nível 0, é a raiz da árvore
e está no topo da hierarquia.

A raiz está conectada a outros nós, no nível 1, que, por sua vez, estão
conectados a outros nós, no nível 2, e assim por diante. Os nós que estão
no fim da árvore são chamados de folhas.

As conexões entre os nós de uma árvore seguem uma nomenclatura genealógica.
Um nó, em dado nível, está conectado a seus filhos (no nível abaixo) e a
seu pai (no nível acima). A raiz da árvore, que está no nível 0, possui
filhos, mas não possui pai. Os nós que estão no final da árvore (os mais
distantes da raiz) são chamados de nós folhas (leafs).
"""

# ARVORES BINÁRIAS
"""
Falando formalmente, uma árvore binária "T" é um conjunto vazio ou é composta
pelos seguintes elementos: uma entidade "n", chamada nó raiz, e pelas entidades 
"Te" e "Td", respectivamente, as subárvores esquerda e direita de "T", que também são
árvores binárias.

Observe que, como "Te" e "Td" são árvores binárias, a definição é recursiva, isto é, 
"Te" possui um nó raiz ou é uma subárvore vazia. O mesmo vale para "Td".
"""
"""
Os nós de uma árvore binária possuem um valor (intitulado chave)
e dois apontadores, um para o filho da esquerda e outro para
o filho da direita. Esses apontadores representam as ligações
(arestas) de uma árvore."""
"""
class NoArvore:
    def __init__(self, chave = None, esquerda = None, direita = None):
        self.chave = chave
        self.esquerda = esquerda
        self.deireita = direita

if __name__ == '__main__':
    raiz = NoArvore(6)               # Raiz da arvore valor 6
    raiz.esquerda = NoArvore(8)      # Filho esquerdo valor 8
    raiz.direita = NoArvore(4)       # Filho direito valor 4
"""
""" Os nós, cujos valores são 8 e 4, não possuem filhos, seus apontadores
à esquerda e à direita são None, ou seja, não apontam para qualquer
outro nó."""


# Árvores binárias de busca e sua operacionalização
"""O problema da busca, inserção e remoção é um dos principais objetivos do estudo
de estruturas de dados. Utilizar a estrutura de árvores para aplicar regras ao
acessar seus dados pode facilitar, computacionalmente, a busca, a inserção e a
remoção de dados.

As árvores binárias de busca (do inglês binary search trees – BST’s) são árvores
de nós organizados de acordo com certas propriedades. A partir desse ponto,
considere que as árvores não permitem elementos repetidos.
Observe a seguinte definição:"""
class NoArvore:
    def __init__(self, chave = None, esquerda = None, direita = None):
        self.chave = chave
        self.esquerda = esquerda
        self.deireita = direita

    def buscaBST(raiz, chave):
        if raiz is None or raiz.chave == chave:
            return raiz
        if raiz.chave < chave:
            buscaBST(raiz.direita, chave)
            return chave
        else:
            buscaBST(raiz.esquerda, chave)
            return chave


# Testando
"""if __name__ == '__main__':
    raiz = NoArvore(55)
    raiz.esquerda = NoArvore(35)
    raiz.direita = NoArvore(75)

    raiz.esquerda.esquerda = NoArvore(25)
    raiz.esquerda.direita = NoArvore(45)
    raiz.direita.esquerda = NoArvore(65)
    raiz.direita.direita = NoArvore(85)"""

cont = [10]

def imprimeArvoreRecur(raiz, nivel):
    if (raiz == None):
        return nivel + cont[0]

    imprimeArvoreRecur(raiz.direita, nivel)
    print()
    for i in range(cont[0], nivel):
        print(end="")
        print(f"{raiz.chave}<")

    imprimeArvoreRecur(raiz.esquerda, nivel)

def imprimeArvore(raiz):
    imprimeArvoreRecur(raiz, 0)


# BUSCA DE NÓS EM BST
"""
O algoritmo de busca decorre diretamente da definição. Considere 
a chave que desejamos localizar. Compara-se com a raiz; se está
nessa raiz, o algoritmo de busca para. Caso contrário, se é menor
que a raiz, executa-se o algoritmo recursivamente na subárvore
esquerda, caso contrário, na subárvore direita. """


def buscaBST(raiz, chave):
    if raiz is None or raiz.chave == chave:
        return raiz
    if raiz.chave < chave:
        return buscaBST(raiz.direita, chave)
    else:
        return buscaBST(raiz.esquerda, chave)


"""
Na busca, existem algumas situações especiais. A primeira ocorre quando
a chave buscada está na raiz. Nesse caso, o nó que contém a chave não tem pai,
por isso, o algoritmo de busca deverá retornar NULO na referência para o pai.
-> Outra situação especial ocorre quando é realizada uma busca em uma
árvore vazia. Nesse cenário, o algoritmo deverá retornar: 
-> NULO - para o nó que contem a chave!
-> NULO - p/ referencia do nó que é pai do no que contem a chave buscada
-> FALSE - P/ referencia ao booleano. """

""""
O algoritmo de busca é utilizado nas operações de inserção e de remoção
de nós nas árvores binárias de busca.
-> Sabemos que a análise de complexidade é baseada na identificação do
pior caso e na análise do número de operações elementares que o resolva.
O pior caso é, sem dúvida, não encontrar a chave buscada. Nesse cenário,
o algoritmo realizará uma comparação por nível até encontrar um nó que não
possua o filho no qual a chave buscada poderia estar.

Pela definição de árvore binária de busca, não há restrição para a altura
da árvore, sendo uma árvore com topologia zigue-zague, que são árvores nas
quais cada nó só possui um filho, podendo ser uma árvore binária de busca.
Entretanto, árvores desse teor possuem altura proporcional à 'n'.
Assim, a complexidade da busca em uma árvore binária de busca é O(n).
"""

# Inserção e remoção em BST
""" A inserção de uma nova chave em uma árvore binária de busca ocorre
sempre em um novo nó, posicionado como uma nova folha da árvore.
Isso decorre do fato de que a posição do nó que contém a nova chave
é determinada pela sua busca na árvore."""

""" Já vimos que estruturas de dados, nas quais realizamos busca, inserção
e remoção, não permitem chave duplicada. Assim, a busca pela chave que
desejamos inserir na árvore deverá, obrigatoriamente, falhar e retornar
como resultado o nó que será pai do novo nó inserido na árvore."""

def InserirBST(raiz, chave):
    if raiz is None:
        return NoArvore(chave)
    else:
        if raiz.chave == chave:
            return raiz
        elif raiz.chave < chave:
            raiz.direita = InserirBST(raiz.direita, chave)
        else:
            raiz.esquerda = InserirBST(raiz.esquerda, chave)
        return raiz

if __name__ == '__main__':
    arvore = NoArvore(55)
    InserirBST(arvore, 35)
    InserirBST(arvore, 75)
    InserirBST(arvore, 25)
    InserirBST(arvore, 45)
    imprimeArvore(arvore)

# Remoção de nós em BST
"""O processo de remover o nó de uma árvore binária deve obedecer
a algumas regras:

1- O nó a ser deletado é uma folha: a remoção é simples, basta
buscar pelo nó e removê-lo.

2- O nó a ser excluído tem apenas um filho: copie o filho para
o nó e o exclua.

3- O nó a ser excluído tem dois filhos: encontre o sucessor em
ordem do nó. Copie o conteúdo do sucessor em ordem para
o nó e o exclua.
"""

def DeleteBST(raiz, chave):
    if raiz is None:
        return raiz
    if chave < raiz.chave:
        raiz.esquerda = DeleteBST(raiz.esquerda, chave)
    elif (chave > raiz.chave):
        raiz.direita = DeleteBST(raiz.direita, chave)
    else:
        if raiz.esquerda is None:
            temp = raiz.direita
            raiz = None
            return temp
        elif raiz.direita is None:
            temp = raiz.esquerda


# PERCURSOS EM ÁRVORES - Formalização
""" Um percurso é a visita sistemática aos elementos de uma estrutura
de dados. Vale destacar que visitar significa realizar uma operação e
não acessar o conteúdo armazenado no elemento da estrutura de dados.
Ou seja, especificamente para árvores, acessar um nó da árvore não
configura uma visita. A visita é uma operação que tem sentido na
semântica da aplicação desejada. A visita mais simples que podemos
definir é a impressão do rótulo da chave armazenada no nó visitado.

Observe que o conceito de árvore é recursivo, isto é, a estrutura foi
definida em termos recursivos. Por tal razão, as definições dos
percursos também são recursivas. Existem três maneiras clássicas de
percursos em árvores:
"""
# PRÉ ORDEM ####
""" Visitar, primeiro, a raiz, depois a subárvore esquerda e,
por último, a subárvore direita."""
# EM ORDEM ####
""" Visitar, primeiro, a subárvore esquerda, depois a raiz e,
por último, a subárvore direita."""
# PÓS ORDEM ####
"""Visitar, primeiro, a subárvore esquerda, depois a subárvore
direita e, por último, a raiz."""


# Algoritmos em Python para percursos em árvores.
"""
Os algoritmos recursivos para os percursos em pré-ordem, ordem simétrica
e pós-ordem são consequências diretas das definições dos percursos.

Vamos conferir agora o algoritmo do percurso em pré-ordem.
"""

def visitaPreOrdem(raiz):
    if(raiz):
        print(raiz.chave)
        visitaPreOrdem(raiz.esquerda)
        visitaPreOrdem(raiz.direita)

"""
Para realizar o percurso em pré-ordem, são necessários três acessos ao
nó. No caso da pré-ordem, no primeiro, executamos a visita; no segundo,
chamamos recursivamente o algoritmo para a subárvore esquerda e, no
terceiro, ocorre a chamada do percurso em pré-ordem do ramo direito.
Assim, a complexidade computacional do percurso em pré-ordem é O(n).
"""

# Algoritimo de percurso em ordem Simétrica
"""
O algoritmo do percurso em ordem simétrica é semelhante ao pré-ordem.
Modificamos somente o momento da visita.
"""

def visitaInOrdem(raiz):
    if (raiz):
        visitaInOrdem(raiz.esquerda)
        print(raiz.chave)
        visitaInOrdem(raiz.direita)

"""
A análise de complexidade é análoga à realizada no algoritmo do percurso
em pré-ordem. Observe que a única diferença é a ordem das visitas.
Sendo assim, a complexidade computacional do algoritmo para percurso em
ordem simétrica é O(n).
"""

# Algoritimo de percurso pós-ordem
""" Finalmente, temos o algoritmo para o percurso em pós-ordem
(algoritmo 10), que é resultado direto da definição, como o da
pré-ordem e o da ordem simétrica. """

def visitaPosOrdem(raiz):
    if (raiz):
        visitaPosOrdem(raiz.esquerda)
        visitaPosOrdem(raiz.direita)
        print(raiz.chave)


# Expressões INFIXA, PREFIXA, POSFIXA
"""
Podem ser implementados sob diversas técnicas de programação.
A técnica que usaremos aqui é a recursividade, que apresenta um
algoritmo mais elegante e conciso.

--- Algoritmo prefixo em Python ---
Para realizar o percurso prefixo, são necessários três acessos ao nó:
"""
def Prefixa(raiz):
   if (raiz):
      print(raiz.chave)
      Prefixa(raiz.esquerda)
      Prefixa(raiz.direita)

"""
--- Algoritmo infixo em Python ---
Segue-se a implementação, que é semelhante à aplicada na visita
em ordem (simétrica).
"""
def Infixo(raiz):
   if (raiz):
      Infixo(raiz.esquerda)
      print(raiz.chave)
      Infixo(raiz.direita)

"""
--- Algoritmo pós-fixo em Python ---
A implementação é semelhante à aplicada na visita em pós-ordem.
"""
def Posfixo(raiz):
    if (raiz):
      Posfixo(raiz.esquerda)
      Posfixo(raiz.direita)
      print(raiz.chave)

