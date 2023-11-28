# MODULOS PYTHON PARA ARVORES BALANCEADAS
"""
Os frameworks são coleções de módulos de softwares e ferramentas que
ajudam o programador no momento de construir seus projetos.
Eles proporcionam uma ajuda fundamental aos profissionais, porque contêm
embasamentos teóricos e práticos que otimizam o tempo, evitam erros comuns
e repetitivos e, por tanto, deixam o processo mais fluido e simplificado.
"""
"""
Existem diversos tipos de framework em Python, que veremos a seguir, mas
as outras linguagens de programação também contam com seus próprios
frameworks.
"""
"""
Alguns módulos em Python para árvores balanceadas ainda são pouco explorados.
Vejamos alguns exemplos:
"""

# pyavl
"""
Trata-se de um pacote em C composto de um conjunto independente de rotinas
dedicadas à manipulação de árvores AVL (arquivos avl.c, avl.h) e de um
módulo de extensão para Python que se baseia nele (arquivo avlmodule.c)
para fornecer objetos do tipo 'avl_tree' em Python, que pode se comportar
como contêineres classificados ou listas sequenciais. Apesar da existência
desse pacote de módulos, ele ainda é pouco explorado, existindo poucos
exemplos na literatura de sua implementação.
"""

# rbtree
"""
Trata-se, sob a licença GPL 3, de um pacote composto de conjunto
de rotinas para manutenção de árvores balanceadas rubro-negras.
Ainda é um pacote com poucos módulos desenvolvidos e que carece
de atualização (a última é de 2008).
"""

# bisect
"""
Para usar os recursos do bisect, é necessário instalar seus pacotes.
Use o pip install bisect. 
"""
"""
No algoritmo a seguir, utilizamos os recursos do bisect para implementar
as operações básicas de uma árvore binária:
"""
"""
import bisect

class Arvore(object):
    def __init__(self, elemento):
        self.arvore = []
        self.addElementos = elemento

    # Adicionar muitos elementos
    def addElementos(self, elemento):
        for i in elemento:
            if i in self: continue
            self.addElemento = i

    # Adicionar um unico elemento
    def addElemento(self, elemento):
        if elemento not in self:
            bisect.insort(self.arvore, elemento)

    # Remove Elemento
    def removeElemento(self, elemento):
        try:
            self.arvore.remove(elemento)
        except ValueError:
            return False
        return True

    # Método de iteração e método de modo de exibição (__str()__).
    def __iter__(self):
        for element in self.arvore:
            yield element

    def __str__(self):
        return str(self.arvore)

if __name__ == '__main__':
    arvore = Arvore([12, 7, 7, 1, 3, 10])

print("Arvore: ", arvore)
print("Tem 7 na arvore? ", 7 in arvore)

arvore.addElemento(4)
print("Adicionei o 4: ", arvore)

arvore.removeElemento(3)
print("Removendo 3:", arvore)

arvore.removeElemento(7)
print("Removendo 7:", arvore)

arvore.addElementos([8, 40, 15, 68])
print("Adicionando vários elementos:", arvore)
"""

# Módulo SBBST
"""
Uma árvore binária de busca autobalanceada é uma estrutura de
dados avançada, que otimiza os tempos de inserção, deleção
e busca. Um módulo Python que implementa e executa essas
atividades eficientemente é a sbbst (do inglês self-balancing
binary search tree).

Use !pip install sbbst para instalar o módulo.
"""

from sbbst import sbbst

tree = sbbst()
nums = [131, 4, 134, 135, 180, 1, 3, 21, 14, 142, 80, 146]
for num in nums:
       tree. insert (num)

print("Número de elementos:",tree.getSize())
print("altura:",tree.getHeightTree())
print("Min valor:",tree.getMinVal())
print("Max valor:",tree.getMaxVal())
print("3º menor valor:",tree.kthsmallest(3))
print("2º maior valor:",tree.kthlargest(2))
print("Pre-Orden:", tree.preOrder())
print("In-Ordem:",tree.inOrder())
print("Pos-Ordem:",tree.postOrder())
tree.delete(128)
tree.delete(3)
tree.insert(55)
print(tree)


