# Atividade discursiva - Python Basico - Primeiro Programa.
"""
- A função eval() permite que você execute uma string como código Python, ou seja
você pode inserir uma string e ela será interpretada como um comando Python válido.
- Isso é incrivelmente poderoso, mas também extremamente perigoso, pois permite que
código malicioso seja executado sem que você saiba.
"""
# Exemplo:
# x = input("Insira um comando Python válido: ")
# eval(x)


print("________ CALCULADORA DE IMC _______ ")
peso = eval(input('Primeiro informe seu peso(ex. 56.0): '))
altura = eval(input('Agora informe sua altura(ex. 1.80): '))

imc = peso / (altura**2)    # Armazena resultado do calculo (peso / altura ao quadrado)

print(f'Seu IMC é = {imc}')


