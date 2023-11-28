#ESTRUTURAS DE DECISÃO E DE REPETIÇÃO
"""Implementar solução para receber dois numeros e
identificar qual é maior"""


#SOLUÇÃO 01
print('SOLUÇÃO 01')
numA = 10
numB = 20

if(numA > numB) :
    maior = numA
else:
    maior = numB

print(f'Entre 10 e 20 o maior é: {maior}')


#SOLUÇÃO 02
print('SOLUÇÃO 02')
numX = 10
numY = 20
maior = numX

if(numY > numX) :
    maior = numX

print(f'Entre 10 e 20 o maior é: {maior}')


#Implementar solução para identificar se é par ou impar!
#Matematica basica: O numero é par quando dividido por ele mesmo o resto é 0(zero)

x = 23

if(x % 2 == 0) :
    print(f'O numro {x} é PAR')
else:
    print(f'O numero {x} é IMPAR')
    


#Implementar solução se o aluno foi APROVADO ou REPROVADO!
aluno = "Marcos"
notaFinal = 4.5
situacao = ()

if(notaFinal >= 7) :
    situacao = 'Aprovado!'
elif(notaFinal >= 5 ):
    situacao = 'Em recuperação!'
else:
    situacao = 'Reprovado!'

print(f'O aluno {aluno} teve a media {notaFinal} e está {situacao}')



