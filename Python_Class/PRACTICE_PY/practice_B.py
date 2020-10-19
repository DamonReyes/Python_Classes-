def practice_1():
    pal = input('escribe una palabra?: ')
    for i in pal:
        print(pal)
    
    edad = int(input('que edad tienes?: '))
    for i in range(edad):
        print(i + 1)

    num = int(input('digita un numero?: '))
    for i in range(1, num + 1, 2):
        print(i, end = ',')

    nume = int(input('digita un numero?: '))
    for i in range(nume, -1, -1):
        print(i)


def practice_5():
    cant = float(input('cantidad a invertir: '))
    inte = float(input('interes anual: '))
    anos = int(input('numero de anos: '))
    for i in range(anos):
        cant *= 1 + inte / 100 
        print("Capital tras " + str(i+1) + " años: " + str(round(cant, 2)))


def practice_6():
    nume = int(input('digita un numero?: '))
    ast = 1
    for i in range(nume):
        print("*"*(i+1))

    for i in range(11):
        print(f'1 por {i} es {i*1}')

    contra = 'contrasena'
    preg = input('cual es la contrasena?: ')
    while preg != contra:
        preg = input('cual es la contrasena?: ')
    else:
        print('la contrasena es correcta')


def practice_10():
    nume = int(input('digita un numero?: '))
    for i in range(1, nume):
        if nume % i != 0:
            print(f'{i} es primo')
        else:
            print(f'{i} no es primo')



if __name__ == '__main__':
    menu = int(input('cual ejercicio desea realizae?: '))
    if menu == 1:
        practice_1()
    elif menu == 5:
        practice_5()
    elif menu == 6:
        practice_6()
    elif menu == 10:
        practice_10()
    elif menu == 9:
        practice_9()
    else: 
        print('jaja gracias pues c:')