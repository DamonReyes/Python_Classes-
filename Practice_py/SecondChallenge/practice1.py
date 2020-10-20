def run():
    numero1 = int(input('escribe un numero: '))
    numero2 = int(input('escribe otro numero: '))

    resta1 = numero1 - numero2
    resta2 = numero2 - numero1

    if numero1 > numero2:
        print(str(numero1) + ' es mayor que ' + str(numero2) + ' por ' + str(resta1) + ' numeros')
    elif numero1 == numero2:
        print(str(numero1) + ' y ' + str(numero2) + ' son iguales')
    else:
        print(str(numero1) + ' es menor que ' + str(numero2) + ' por ' + str(resta2) + ' numeros')



if __name__ == '__main__':
    run()