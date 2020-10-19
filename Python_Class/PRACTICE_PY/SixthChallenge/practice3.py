def run():
    num1 = int(input('escribe un numero: '))
    num2 = int(input('escribe otro numero: '))
    suma = num1 + num2
    print(f'******{suma}******')
    
    preg = input('quieres anadir otro numero?: ')

    while preg == 'si':
        num3 = int(input('escribe otro numero: '))
        suma = suma + num3
        print(f'******{suma}******')
        preg = input('quieres anadir otro numero?: ')
    else:
        print('ese fue el resultado')





if __name__ == '__main__':
    run()