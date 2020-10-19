def run():
    limite = int(input('escribe un numero: '))
    numero2 = int(input('escribe otro numero: '))

    resta2 = limite - numero2
    resta1 = numero2 - limite

    if limite < numero2:
        print(str(limite) + ' se encuentra fuera del rango permitido ' + ' por ' + str(resta1) + ' numeros')
    elif limite == numero2:
        print(str(limite) + ' y ' + str(numero2) + ' son iguales')
    else:
        print(str(limite) + ' esta en el rango permitido ' + ' por ' + str(resta2) + ' numeros')



if __name__ == '__main__':
    run()