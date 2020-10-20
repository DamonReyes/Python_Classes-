def run():
    limite_sup = int(input('escribe el limite superior: '))
    limite_inf = int(input('escribe el limite inferior: '))
    comparacion = int(input('escribe un numero: '))

    if comparacion > limite_sup:
        print('el numero es mayor al limite')
    elif comparacion < limite_inf:
        print('el numero es inferior al limite')
    else:
        print('el numero esta en medio de los limites permitidos')


if __name__ == '__main__':
    run()