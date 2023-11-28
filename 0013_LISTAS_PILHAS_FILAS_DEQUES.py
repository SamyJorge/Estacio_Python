# LISTAS, PILHAS, FILAS E DEQUES - Módulo 03 C2
# PILHAS

"""
CONCEITO DE PILHA
A estrutura de dados pilha tem esse nome porque se assemelha conceitualmente
às pilhas (de roupas, caixas, livros etc.) do mundo real. Nela, quem chegou
primeiro fica embaixo de todos os outros. Ora, para você remover uma caixa
que está abaixo de várias outras, você precisa remover primeiro as de cima.

Essa estrutura faz com que o nó mais recente seja sempre o retirado da pilha.
Essa política também é chamada de Last In First Out, com o acrônimo LIFO.
"""

# IMPLEMENTAÇÃO DA PILHA
"""
A pilha pode ser implementada em alocação contígua ou encadeada, como as listas.
De fato, a pilha é uma lista especial na qual todos os nós são inseridos e
removidos apenas no início da lista.

Para uma alocação encadeada, você só precisa manter um ponteiro para o início
(comumente chamado de topo) da pilha. Se a pilha estiver vazia, o TopoPilha
apontará para o valor nulo. O código a seguir apresenta a classe Pilha e seu
construtor.
"""

# ALOCAÇÃO ENCADEADA
class pilhaEncadeada:
    def __init__(self, topo = None):
        self.topo = topo

maxPilha = 5
pilha = [None] * maxPilha
topoPilha = None

# Inserção em pilha - Caso Encadeado
""" A inserção na pilha deve ocorrer sempre no topo da pilha. Essa operação
é comumente chamada de PUSH."""
"""Para o caso encadeado, você pode usar o código abaixo (novoNo deve estar
alocado e com o próximo apontando para o nulo):"""

def pushEnc(self, novoNo):
    novoNo.proximo = self.topo     # Insere o nó
    self.topoPilha = novoNo             # Atualiza o topo da pilha


# Remoção da pilha Encadeada
"""" A remoção da pilha (comumente chamado de POP) deve ocorrer sempre no topo da pilha. Para o caso encadeado,
você pode usar este código: """

def popEnc(self):
   if self.topo == None:
       return None                # Erro pilha vazia
   k = self.topo                  # Salva o nó removido
   self.topo = self.topo.proximo  # remove o nó
   return k                       # Retorna o nó removido


# Inserção em pilha - Caso Contiguo
"""Para o caso contíguo, você possui 3 variáveis: Pilha guarda o espaço de memória, MaxPilha guarda o número
máximo de elementos na pilha, TopoPilha guarda o índice do topo da pilha. Experimente usar este código:"""

def pushCont(novoNo):
    global pilha
    global topoPilha
    global maxPilha

    if topoPilha == None:                # Pilha vazia
        pilha[0] = novoNo                # Insere nó
        topoPilha = 0                    # Atualiza o topo da pilha
    elif (topoPilha == maxPilha-1):      # Pilha cheia
        return -1                        # Erro pilha cheia
    else:
        topoPilha = maxPilha + 1         # Atualiza o topo da pilha
        pilha[topoPilha] = novoNo       # Insere o nó
    return topoPilha                     # Saída normal



# Remoção da pilha Contigua
""" Para o caso contíguo, você possui 3 variáveis: Pilha guarda o espaço de memória, MaxPilha guarda o número
máximo de elementos na pilha, TopoPilha guarda o índice do topo da pilha. Experimente este código: """

def popCont():
    global pilha        # Guarda o espaço de memoria
    global topoPilha    #  Guarda o indice do topo da pilha
    global maxPilha     #  Guarda o numero de elementos

    if topoPilha == None:       # Indica erro pilha vazia
        return None             # None indica erro pilha vazia
    else:
        k = pilha[topoPilha]           # Salva o nó removido
        if topoPilha == 0:
            topoPilha = None           # Pilha vazia após remoção
        else:
            topoPilha = topoPilha -1   # Remove nó
        return k                       # Retorne k=0 nó consumido


# TESTAR
print(pilha)
for i in range(10):
    pushCont(i)
    print(pilha)
print(pushCont(11))
for i in range(10):
    print(popCont())
print(popCont())



