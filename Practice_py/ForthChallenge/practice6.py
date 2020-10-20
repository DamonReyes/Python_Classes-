import math

def run():
    num1 = int(input('ingresa un numero: '))
    num2 = int(input('ingresa otro numero: '))
    
    div = num1 / num2
    modl = num1 % num2

    print(round(div, 2))
    print(modl)

    print(str(num1) + ' dividido entre ' + str(num2) + ' es ' + str(round(div, 2)) + ' y sobra ' + str(modl) + ' .')


if __name__ == '__main__':
    run()