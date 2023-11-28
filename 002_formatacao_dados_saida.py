# FORMATAÇÃO DE DADOS DE SAIDA:
"""Quando queremos que a saida dos dados tenha um formato expecifico
existem algumas possibilidades para usar a função print()."""

hora = 12
minutos = 45
segundos = 10

# Método CONCATENAÇÃO DE STRINGS:  É possível com o operador '+'.

print('Hora atual: ' + str(hora) + ':' + str(minutos) + ':' + str(segundos))
print('Jesus'+ ' é' + ' o' + ' unico' + ' caminho.')


# Método .format()
""" Outra maneira é com o método format(), podemos montar a string com as chaves {}
indicando aonde entrarão valores das variáveis, passados por parâmetros separados
por vírgulas. """

print('Hora atualizada: {}:{}:{}'.format(hora, minutos, segundos))
print('{} {} {}'.format( 'Jesus', 'Vive', 'e voltará'))
"""
É importante observar que a quantidade de chaves precisa ser igual à
quantidade de variáveis passadas como parâmetros no método format().
"""


# Método f'string {variavel}'
""" Para tornar a saída formatada ainda mais intuitiva, e avitar possiveis erros
basta utilizar a letra ‘f’ no início dos parâmetros da função print() e colocar
cada variável dentro das chaves na posição em que deve ser impressa."""

print(f'A hora atual é: {hora}:{minutos}:{segundos}')

""" Também é possível especificar a largura de campo para exibir um inteiro.
Se a largura não for especificada, ela será determinada pela quantidade de
dígitos do valor a ser impresso. """

print(f'São: {hora :5}h :{minutos :5}min :{segundos :5}seg')
# Determinei que a variavel deveria ser impressa com 5 espaços

""" O método format() também pode ser usado para imprimir valores de ponto flutuante com a precisão definida."""

print('Resutado da divisão de 10 por 3 = {:10.5}'.format(10/3))
""" {:10.3}, determina que a impressão terá 10 espaços. 5 espaços serão
utilizados pelo numero de caracteres determinados para serem exibidos, 5 """


"""
IMPRESSÃO DE SEQUÊNCIAS: Python também permite a impressão de sequências com mais
possibilidades que C, incluindo as strings."""

SEQUENCIA = [1, 2, 3]
print (SEQUENCIA)

#IMPRIMINDO UMA SUBSTRING

str = "Hello World"
print(str[0:5])    #Imprime indices 0, 1, 2, 3 e 4.
print(str[4:11])   #Imprime indices 4, 5, 6, 7, 8, 9 e 11.

#Tambem é possivel forçar a leitura da string da direita pra esquerda.

print('Invertendo a leitura:  ' + str[::-1]) #Leia e imprima da esquerda p/ a direita.
print('Invertendo a leitura:   ' + str[11:4:-1])