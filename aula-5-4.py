#loops

work = input('Você trabalha hoje? ')
day = input('O dia está bonito? ')
lazy = input('Você está com preguiça? ')

if work == 'sim':
    print('Que coisa! Mas bora trabalhar!')
elif work == 'não':
    print('Aproveite o dia!')
else:
    print('Resposta errada! Digite sim ou não.')


if day == 'sim' and work == 'não':
    print('Aproveite para caminhar no tempo livre!')
elif day == 'não' and work == 'não':
    print('Bora ver um filme ou série!!!')

if lazy == 'sim' and work == 'não':
    print('Aproveita e dorme mais!')
elif lazy == 'não' and work == 'não':
    print('Bora estudar então?')