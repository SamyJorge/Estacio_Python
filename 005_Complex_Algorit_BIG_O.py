# NOTAÇÃO BIG-O
"""
Para poder fazer a comparação vamos criar duas funções diferentes
que farão a mesma coisa e retornarão o mesmo resultado.

A função receberá por parametro um número somara.
"""

def soma1(n):
    soma = 0
    for i in range(n + 1):
        soma += i
    return soma

resultado = soma1(10)
print(resultado)




