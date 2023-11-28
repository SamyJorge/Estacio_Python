# LISTA ENCADEADA (LINKED LIST)
""" Obs. A classe NoEncad poderia estar em um arquivo separado e ser
referenciada como fazemos com as bibliotecas Python. """
class NoEncad:
    def __init__(self, data):
        self.data = data
        self.next = None

class listaEncad:
    def __init__(self):
        self.head = None
        self._size = 0

    """ Inserção de elemento encadeada. """
    def append(self, elem):
        # Inserção no final quando ja possui elementos na lista
        if self.head:                     # Se tiver um elemento na cabeça
            pointer = self.head           # pointer(ponteiro) recebe o elemento
            while(pointer.next):         # Enquanto tiver um proximo
                pointer = pointer.next
            pointer.next = NoEncad(elem)
        else:
            # Primeira inserção
            self.head = NoEncad(elem)
        self._size += 1

    def __len__(self):
        """Retorna o tamenho da lista"""
        return self._size

    def _getNoEncad(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:  # Se pointer não vazio
                pointer = pointer.next
            else:
                raise IndexError("list index out range")
        return pointer

    def set(self, index, elem):
        pass

    def __getitem__(self, index):
        pointer = self._getNoEncad(index)
        if pointer:                                        # Se pointer não vazio
            return pointer.data
        else:
            raise IndexError("list index out range")

    def __setitem__(self, index, elem):
        pointer = self._getNoEncad(index)
        if pointer:
            pointer.data = elem
        else:                                                  # Se pointer não vazio
            raise IndexError("list index out range")

    """Função retorna o indice de elementos na lista"""
    def index(self, elem):
        pointer = self.head
        i = 0                  #Variavel indexadora
        while(pointer):
            if pointer.data == elem:      # Se for igual
                return i             # retorne o i
            pointer = pointer.next   # Prociga
            i += 1
        raise ValueError('{} não está na lista!'.format(elem))

    def insert(self, index, elem):
        """Para inserir no inicio da lista"""
        if index == 0:
            node = NoEncad(elem)   #Criando novo nó com o elemento desejado
            node.next = self.head  #O proximo do no criado passa a ser a cabeça
            self.head = node       #Determinando quem é agora a cabeça da lista
        else:
            pointer = self._getNoEncad(index-1)
            node = NoEncad(elem)
            node.next = pointer.next
            pointer.next = node

        self._size = self._size + 1

    def remove(self):
        pass


# --------  textes ----------
lista = listaEncad()    # Criando lista vazia
lista.append('Jorge')   # Inserindo elemento
lista.append('Iago')
lista.append('Marcia')
print("A lista tem {} elementos".format(len(lista)))
lista.set(0, 'Samy')
print(lista[1])
print(lista.index('Iago'))

lista.insert(0, "Roger")
print(lista.index('Roger'))
print(lista.index('Samy'))


