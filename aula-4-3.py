#Tuple

fruits = ('banana', 'maçã', 'abacate', 'uva', 'morango')
person_balance = (500.00, 245.50, 636.70, 45.23, 1234.12)
patients_numbers = (33, 54, 12, 67)
fruits_2 = ('pêssego', 'laranja', 'pitaya')

#valores são indexados
print(fruits[3])
print(person_balance[0:3])
print(patients_numbers[2:])
print(fruits[:3])

#permite duplicados
person_balance_2 = (500.00, 245.50, 636.70, 45.23, 1234.12, 45.23, 500.00)

#juntar tuples
fruits_tuple = fruits + fruits_2
print(fruits_tuple)

#contar valores repetidos em uma tuple
patients_numbers_2 = (33, 54, 12, 67, 33, 54, 12, 67, 33, 54, 12, 67, 33, 54, 12, 67, 33, 54)
print(patients_numbers_2.count(54))