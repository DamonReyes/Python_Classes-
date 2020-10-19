import math

def triangulo():
    print('escoge la base y la altura: ')
    base = int(input('cual es la base?: '))
    alt = int(input('cual es la altura?: '))
    area=int (base) * int (alt) / 2.0
    print('el area es: ' + str(area))


def cuadrado():
    print('lado del cuadrado: ')
    lado = float(input('ingrese el lado: '))
    area = lado * lado
    print('el area es: ' + str(area))


def circulo():
    print('radio del circulo: ')
    radio = int(input('ingrese el radio del circulo: '))
    area = math.pi * radio ** 2
    return print('el area del circulo es %.3f ' % area)



def run():
    cal = print('calculo de area')
    choise = int(input('***' + '[1]triangulo ' + ' [2]circulo ' + ' [3]cuadrado ' + '*** : '))
    
    if choise == 1:
        return triangulo()
    elif choise == 2:
        return circulo()
    elif choise == 3:
        return cuadrado()
    else:
        print('gracias ')
        

    



if __name__ == '__main__':
    run()