# ARVORES BINARIAS - Segundo Prof. Alisson (Canal Python Café)

#Classe do nó com seus atributos
class nodeBinar:
    def __init__(self, data):
        self.data = data
        self.esq = None
        self.dir = None

    # Convertendo para string
    def __str__(self):
        return str(self.data)

# Classe para a arvore. Servirá dizer quem é a raiz
# e tambem conter alguns metodos, como veremos.

class binarTree:
    def __init__(self, data):
        no = nodeBinar(data)   # Criando um nó que receberá o valor por parametro.
        self.raiz = no         # Raiz recebe valor da var. no



# Testando
if __name__ == "__main__":
    tree = binarTree(7)             # Chamando classe que cria a arvore com raiz 7
    tree.raiz.esq = nodeBinar(14)   # Crinado nó filho esquerdo
    tree.raiz.dir = nodeBinar(18)   # Criando nó filho direito

print(tree.raiz)
print(tree.raiz.esq)
print(tree.raiz.dir)


