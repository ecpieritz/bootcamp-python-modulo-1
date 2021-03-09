#elif

age = int(input('Digite a sua idade: '))

print(type(age))

if age >= 18:
    print('Você já pode dirigir.')
elif age < 18:
    print('Você ainda não pode dirigir')

exercise = int(input('Quantos minutos você se exercita por dia? '))

if exercise < 30:
    print('Você deveria se exercitar mais')
elif exercise >= 30 and exercise <= 60:
    print('Você está no caminho certo!')
elif exercise > 60 and exercise <= 120:
    print('Você é um(a) atleta!')
else:
    print('Uau! Você se exercita muito!!!')