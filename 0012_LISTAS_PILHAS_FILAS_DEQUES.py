# LISTAS, PILHAS, FILAS E DEQUES - Módulo 03 C1

# CASO FILA ENCADEADA - IMPLEMENTAÇÃO
"""
A fila pode ser implementada em alocação contígua ou encadeada, como as listas.
De fato, a fila é uma lista especial na qual todos os nós são inseridos ao final
da lista, e todos os nós são removidos apenas no início da lista.

Para uma alocação encadeada, você pode manter duas variáveis, uma para o início
da fila, e outra para o final da fila. Se a fila estiver vazia, ambas as variáveis
apontarão para o valor nulo. Se houver apenas um elemento, ambas apontarão para
esse elemento. Com mais elementos, InícioFila apontará para o nó que pode ser
removido, e FinalFila apontará para o último elemento a entrar, que apontará para
o próximo nó a ser inserido.
O código a seguir representa a criação da classe e seu construtor.
"""

class filaEncadeada:
    def __init__(self, inicio = None):
        self.inicio = inicio
        self.final = inicio

# INSERÇÃO EM FILA ENCADEADA
"""
A inserção em fila deve ocorrer sempre no final da fila.
Para o caso encadeado, você pode usar o seguinte código 
(novoNo deve estar alocado e com próximo apontando para o nulo):
"""
def insere(self, novoNo):
    if self.inicio == None:          # Fila vazia
        self.inicio = novoNo         # Atualiza o inicio da fila
        self.final = novoNo          # Atualiza o final da fila
    else:
        self.final.proximo = novoNo  #Insere o nó
        self.final = novoNo          #Atualiza o final da fila

# REMOÇÃO EM FILA ENCADEADA
def remove(self):
    if self.inicio == None:    # Tratando erro fila vazia
        return None            # None indica erro fila vazia
    else:
        k = self.inicio                      # Salva nó removido
        self.inicio = self.inicio.proximo    # Remove o nó
        return k                             # Retorne nó consumido


####################################################################

# CASO FILA ALOCAÇÃO CONTIGUA
"""
Para uma alocação contígua, você tem duas opções:
1) -Manter sempre o início da fila no endereço inicial da memória alocada, e ir
inserindo ao final da fila, no próximo endereço vazio. Para facilitar esse
processo, você pode manter uma variável guardando o final da fila. Entretanto,
esse método tem a desvantagem de que, quando um nó é removido (do início), todo
o restante da fila tem que ser ajustado para frente em memória.

2) Ir alocando os nós sequencialmente em memória, e manter uma variável para o
início da fila, e uma para o final da fila. Ao remover um nó (do início), você
apenas move a variável InícioFila um nó para frente. Ao inserir um novo nó,
você move a variável FinalFila um nó para frente, para o novo nó. Esta é a opção
mais comum em se tratando de alocação contígua.
"""

# O código a seguir inicializa uma fila com máximo de 10 valores
maxFila = 10
fila = [None] * maxFila
inicioFila = None
finalFila = None

# INSERÇAO EM LISTA CONTIGUA
"""
Para o caso contíguo, você possui 4 variáveis: Fila guarda o espaço de memória. MaxFila guarda o número máximo
de elementos na fila, InicioFila e FinalFila guardam os índices de início e final da fila, respectivamente.
Você pode usar o seguinte código:
"""
def insereFila(novoNo):
    global inicioFila
    global maxFila
    global finalFila
    global fila

    if inicioFila == None:     # Se fila vazia
        fila[0] = novoNo       # Insere nó
        inicioFila = 0         # Atualiza o inicio da fila
        finalFila = 0          # Atuiliza o final da fila
    elif(finalFila + 1) % maxFila == inicioFila:   # Fila cheia
        return -1              # Erro fila cheia
    else:
        finalFila = (finalFila + 1) % maxFila   # Atualiza o final da fila
        fila[finalFila] = novoNo                # Insere nó
    return finalFila                            # Saída normal


def removeFila():
    global inicioFila       # Indica acesso a variáveis globais
    global maxFila
    global finalFila
    global fila

    if inicioFila == None:  # Fila vazia
        return None         # Erro fila vazia

    k = fila[inicioFila]    # Salva o nó removido

    if finalFila == inicioFila:
        inicioFila = None        # Fila vazia após remoção
    else:
        inicioFila = (inicioFila + 1) % maxFila  # Remove o nó
    return k                                     # Retorne k = 0 nó consumido


# TESTANDO FILA EM ALOCAÇÃO CONTIGUA
"""print(fila)
for i in range(10):
    insereFila(i)
    print(fila)
print(insereFila(11))
for i in range(10):
    print(removeFila())
print(removeFila())"""


# DANDO ERRO >>> TESTANDO FILA ENCADEADA
"""e0=No(0,'Joao')
fila=FilaEncadeada(e0)
k0=fila.busca(0)
print(k0.valor)
fila.print()
e1=No(1,'Maria')
fila.insere(e1)
fila.print()
e2=No(-1,'Ana')
fila.insere(e2)
fila.print()
e3=No(2,'Arthur')
fila.insere(e3)
fila.print()
k=fila.remove()
print("No removido: "+k.valor)
fila.print()"""