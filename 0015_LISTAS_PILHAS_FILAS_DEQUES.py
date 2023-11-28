# LISTA CIRCULAR
"""A ideia da lista circular é permitir a representação de uma lista
de dados cíclica, como um loop sem fim. Para isso, você precisa fazer
com que o último nó seja seguido pelo primeiro, fechando o laço eterno.

No caso encadeado, isso pode ser facilmente resolvido apontando o
ponteiro próximo do último nó para o primeiro nó, ao invés de apontar
para nulo. Se sua lista for duplamente encadeada, você também precisa
apontar o ponteiro anterior do primeiro nó para o último.

Entretanto, é importante continuar mantendo duas variáveis, uma apontando
para o “início” da lista, e outra, para o “final“ da fila. Essas duas
variáveis são importantes para você fazer as operações de inserção e
remoção da lista. """


# Inserção em lista circular
"""A inserção em lista circular funciona exatamente como na lista linear, com
a única diferença que se você inserir após o “final” da lista, você deve
atualizar a variável que aponta para o final da lista. No caso de ser
encadeada, também precisará atualizar os ponteiros associados.
O código a seguir mostra este caso:"""

def circular(novoNo):
    if inicioLista == None:                 # Se lista vazia
        inicioLista = novoNo
        novoNo.proximo = novoNo
    else:
        finalLista.proximo = novoNo        # Insere o nó
        finalLista = novoNo                # Atualiza ponteiros
        finalLista.proximo = inicioLista


# Remoção em lista circular
"""A remoção em lista circular funciona de forma semelhante à lista linear, precisando
apenas atualizar os ponteiros de início e final da lista, caso um dos extremos seja
removido. No caso de lista encadeada, experimente usar o seguinte código:"""


def removeCircular:
    if noAnterior == inicioLista:
        return None
    if finalLista == iniciolista:
        lista  = None
        return 0
    if noAnterior == finalLista:
        finalLosta.proximo = inicioLista.proximo
        iniciolist = finalLista.proximo
    elif noAnterior.proximo == finalLista:
        finalLista = noAnterior
        noAnterior.proximo = inicioLista
    else:
        noAtual = noAnterior.proximo
        noAnterior.proximo = noAtual.proximo
    return 0

