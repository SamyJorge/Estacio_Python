# LISTAS, PILHAS, FILAS E DEQUES - Módulo 03 C2

# DEQUES - CONCEITO
"""
A estrutura de dados deque é uma generalização da fila e da pilha, essencialmente permitindo que se adicione
ou remova nós do início ou do final da lista. Para evitar confusões, as operações são normalmente identificadas
com qual lado da fila está sendo alterado. A remoção de um nó do início pode ser chamada de pop_front, enquanto
a remoção de um nó ao final pode ser chamada de pop_back.
"""
# Implementação de deque
# O módulo collections do Python já possui uma implementação de deque. Você pode acessá-la usando este comando:

from collections import deque

# Exemplos de operações em deque, como inserção e remoção em ambas as pontas:
q = deque()         # Cria o deque
q.append('b')       # Insere no final
q.append('c')       # Insere no final
q.append('d')
q.appendleft('a')   # Insere no inicio

print('Lista deque criada => ', q)
print('Elemento removido do inicio => ', q.popleft())
print('Elemento removido do fim da fila=> ', q.pop())
print('Deque após a remoção => ', q)


"""
Caso queira implementar seu próprio deque, ele pode ser implementado em alocação
contígua ou encadeada, assim como as listas.
"""
"""
Para uma alocação encadeada, você precisa manter um ponteiro para o início e para
o final do deque. Se o deque estiver vazio, ambos apontarão para o valor nulo.
Usualmente, utilizamos um encadeamento duplo, que permite percorrer a lista em
qualquer uma das direções e a partir de qualquer uma das pontas.
"""
# Deque - Alocação Encadeada.

class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None
        self.anterior = None

class DequeEncad:
    def __init__(self, inicio=None):
        self.inicio = inicio
        self.final = inicio

# Inserção em deques
""" A inserção no deque pode ocorrer no início ou final da estrutura.
Quando ocorre no início da estrutura, seu funcionamento é idêntico a
inserção na pilha, apenas ajustando-se as variáveis InicioDeque e
FinalDeque. Essa operação pode ser chamada PUSH_front.

Quando a inserção ocorre no final da estrutura, seu funcionamento é
idêntico à inserção na fila. Essa operação também pode ser chamada
PUSH_back."""

def pushFront(self, novoNo):
    novoNo.proximmo = self.inicio
    self.inicio = novoNo

# Remoção do deque
"""
A remoção do deque pode ocorrer no início ou no final da estrutura.
Quando ocorre no início, seu funcionamento é idêntico à remoção da pilha,
apenas ajustando-se os ponteiros de início e final do deque (no caso encadeado)
ou as variáveis InicioDeque e FinalDeque(no caso contíguo). 
Essa operação pode ser chamada popFront ou popLeft.

Quando a remoção ocorre no final da estrutura, seu funcionamento pode
ser chamado popBack ou popRight.
Para o caso encadeado, você pode usar o código abaixo:
"""
# CASO ENCADEADO
def popBack(self):
    if self.inico == None:   # Erro -deque vazia
        return None          # None indica erro deque vazia
    else:
        k = self.final                     # Salva o nó removido
        self.final = self.final.anterior   # Remove nó
        self.final.proximo = None          # Aponta o proximo do final p/ vazio
        return k                           # Retorna k=0 nó consumido



# Deque - Alocação Contigua.
"""Para uma alocação contígua, você pode usar um vetor circular, como fizemos para a fila. As duas variáveis
(InicioDeque e FinalDeque) indicam as pontas do deque e vão se deslocando conforme os nós são inseridos
e removidos. Ao chegar ao fim do espaço alocado e ser incrementada, a variável faz a volta e o índice
volta para zero."""

"""De forma similar, se o valor estiver em 0 e for decrementado, passa para o maior valor possível.
Normalmente, usamos a lógica modular para fazer esses incrementos/decrementos, assim como vimos na fila.
O código a seguir é um exemplo de alocação do deque."""

maxDeque = 5
deque = [None] * maxDeque
inicioDeque = None
finalDeque = None


# REMOÇÃO - CASO CONTIGUO
""" Para o caso contíguo, você possui 4 variáveis: Deque guarda o espaço
de memória, MaxDeque guarda o número máximo de elementos do deque,
InicioDeque e FinalDeque guardam o índice do início e final do deque.
Você pode usar este código:  """

def popBackCont():
    global inicioDeque			               #indica o acesso a variáveis globais
    global maxDeque
    global finalDeque
    global deque
    if inicioDeque == None:				       #Deque vazia
        return None				               #erro Deque vazia
    k = deque [inicioDeque]				       #salva o nó removido
    if finalDeque == inicioDeque:
        inicioDeque=None 		               #Deque vazia após remoção
    else:
        finalDeque=(finalDeque-1) % maxDeque    #remove o nó
    return k			               	   	    # retorne k=o nó consumido

