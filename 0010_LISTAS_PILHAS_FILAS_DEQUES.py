# LISTAS, PILHAS, FILAS E DEQUES - MODULO 02

# PRIMEIRA APLICAÇÃO:
"""Nossa primeira aplicação para uma lista em alocação contígua é uma lista cadastral.
Imagine que você tem um mercado e quer organizar uma lista dos seus produtos.
O primeiro passo é criar uma chave para essa lista, que possa ser buscada. Nesse caso,
podemos criar um campo “produtoID” para ser a chave da nossa lista."""

def inserir(prod, L, tam):
    L.append('')
    estoque[tam] = prod
    tam += 1
    return estoque

def cadastro():
    id = int(input('Id do produto: '))
    nome = str(input('nome do produto: '))
    val = float(input('Valor R$ '))
    inserir((id, nome, val), estoque, len(estoque))

estoque = []

# ----- INTERFACE ------
print(''' 
---- Cadastro de produto ----
Escolha uma das opções abaixo:
[1] Para cadastrar produto.
[2] Para encerrar.
-----------------------------''')
opcao = int(input('O que você deseja fazer? '))

while opcao <= 2:
    if opcao == 2:
        print('Cadastramento Encerrado')
        opcao = opcao + 1
    else:
        cadastro()
        opcao = int(input('O que você deseja fazer? '))

print('Estoque: ', estoque)