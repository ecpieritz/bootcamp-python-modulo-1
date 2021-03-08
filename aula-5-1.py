'''
O que são funções, condições e loops?

As funções são linhas de código organizadas e agrupadas que vão cumprir uma função em nosso
código. Uma função pode agrupar condições, que são argumentos que desejamos que sejam satisfeitos.

O loop são repetições que geralmente abarcam condições que são criadas para auxiliar o desenvolvedor nas rotinas.
'''

y = 30
x = 200

''' if

O if em Python funciona como uma forma de colocar condições em seu código. 

A condição if é muito utilizada em loops, ou quando desejamos colocar condições em nosso código
'''

if x > y:
    print('A variável x é maior que a variável y')

''' elif

O elif é a junção das palavras else + if. Devemos utilizar a condição if somente uma vez, todas as demais devem ser elif.
'''

if x > y:
    print('A variável x é maior que a variável y')
elif x < y:
    print('A variável y é maior do que a variável x')

''' for

Um loop for é útil para a iteração sobre uma sequência (ou é uma list, uma tuple, um dictionary, um set ou uma string).

Com o loop for, podemos executar um conjunto de instruções, uma vez para cada item em uma list, tuple, set, etc.
'''
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for i in numeros:
    print(i)
