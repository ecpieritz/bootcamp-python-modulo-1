#Listas (Arrays)

fruits = ['banana', 'maçã', 'abacate', 'uva', 'morango']
person_balance = [500.00, 245.50, 636.70, 45.23, 1234,12]
patients_numbers = [33, 54, 12, 67]
fruits_2 = ['pêssego', 'laranja', 'pitaya']

#permite duplicados
numbers = [33, 54, 12, 67, 33]

#calcular tamanho da lista
print(len(person_balance))

#pode conter vários tipos de dados
random_list = [23, 'jamanta', 456.23]

#acessar um item da lista
print(fruits[2])
print(person_balance[1])

#adicionar item na lista
fruits.append('cereja')
fruits.append('mirtilo')
print(fruits)

#unir listas
fruits.extend(fruits_2)
print(fruits)