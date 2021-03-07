print(coleções de dados)

'''
list

São usadas para armazenar vários itens em uma única variável.
Os itens da lista são indexados, o 1º item tem o índice[0], o 2º item tem o índice[1], etc...
- permite valores duplicados
- os itens são mutáveis
- os itens são ordenados
'''
shop_list = ['chocolate', 'leite', 'arroz']
weights = [45, 67, 110, 32, 25]
heights = [1.45, 1.53, 1.78, 1.87]
random_list = [5, 'maçã', 0.53, 'uva']

'''
Tuples

São usadas para armazenas vários itens em uma única variável.
Os itens da lista são indexados, o 1º item tem o índice[0], o 2º item tem o índice[1], etc...
- os itens são imutáveis
- os itens são ordenados
'''
shop_list_2 = ('chocolate', 'leite', 'arroz')
weights_2 = (45, 67, 110, 32, 25)
heights_2 = (1.45, 1.53, 1.78, 1.87)
random_list_2 = (5, 'maçã', 0.53, 'uva')

'''
Set

São usadas para armazenas vários itens em uma única variável.
- não é ordenado
- é desindexada
- são imutáveis
- não permite valores duplicados
'''
shop_list_3 = {'chocolate', 'leite', 'arroz'}
weights_3 = {45, 67, 110, 32, 25}
heights_3 = {1.45, 1.53, 1.78, 1.87}
random_list_3 = {5, 'maçã', 0.53, 'uva'}

'''
Dictionary

São usados para armazenas valores de dados em pares. 
- geralmente correspondentes
- é ordenada
- é mutável
- não permite valores duplicados
'''

students_course = {
    'José': 'python',
    'Maria': 'javascript',
    'Ana': 'python',
    'João': 'python',
    'Carla': 'javascript'
}