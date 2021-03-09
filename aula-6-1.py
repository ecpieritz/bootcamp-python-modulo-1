# Condições, Loops e Funções (Parte II)

num = 1

''' While
O while faz com que o Python execute um loop enquanto um, ou um conjunto de argumentos, seja satisfeito. Quando todos os argumentos forem satisfeitos
o loop deixa de ser executado e imprime o resultado.

O while é muito utilizado em situações que não conhecemos o tamanho do arquivo, ou do conjunto de dados, que estamos lidando. 
'''

while num < 10:
    print(num)
    num += 1

'''Range
A função range( ) retorna uma sequência de números, começando a partir de 0 por padrão, e acrescenta um valor (por padrão) e para um valor antes do estipulado.

É muito utilizando juntamente com o for para executar contagens com o python.
'''
for i in range(1, 21):
    print(i)

'''def
Utilizamos o def para criar funções em Python. A criação de funções em python é muito útil quando desejamos facilitar a execução de uma rotina.

Na verdade, a palavra função e rotina estão intimamente ligadas em Python. Por ser praticamente impossível que uma linguagem tenha nativamente todas funções
possíveis, existe a possibilidade de criarmos nossas próprias funções.
'''


def soma(x, y):
    return (x + y)


'''Lambda (funções anônimas)
Utilizamos o lambda para criar funções, assim como fizemos com o def. Entretanto, com o lambda nós não nomeamos as funções, por isso o nome “Função
Anônima”. São úteis em alguns casos específicos em que vamos utilizar uma função poucas vezes.
'''


# Utilizando o def:
def diminuir(x, y):
    return (x - y)


# utilizando lambda:
sum1 = lambda x, y: x + y
