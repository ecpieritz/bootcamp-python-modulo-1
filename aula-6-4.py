# def (função)

def sum1(x, y):
    print(x + y)


def sub1(x, y):
    print(x - y)


def imc(weight, height):
    imc = weight / (height ** 2)


    if imc < 18.5:
        print('Magro(a) demais')
    elif imc >= 18.5 and imc <= 24.9:
        print('Normal')
    elif imc >= 25 and imc <= 29.9:
        print('Sobrepeso')
    elif imc >= 30 and imc <= 39.9:
        print('Obesidade grau 1')
    else:
        print('Obesidade grau 2')
    return

imc(70, 1.6)

