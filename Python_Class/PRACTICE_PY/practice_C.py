def practice_1():
    edad = int(input('cual es tu edad?: '))
    if edad > 18:
        print('eres mayor de edad')
    else:
        print('eres menor de edad')

    cont = 'contrasena'
    preg = input('cual es la contrasena?: ')

    if preg != cont:
        print('la contrasena no es igual')
    else:
        print('la contrasena es correcta ')


def practice_3():
    num1 = int(input('digita un numero?: '))    
    num2 = int(input('digita otro numero?: '))
    div = num1 / num2
    
    if num2 == 0:
        print('error, try again')
        practice_3()
    else:
        pass

    nume = float(input('ingrese numero: '))
    if nume % 2 == 0:
        print('el numero es par')
    else:
        print('el numero es inpar')


def practice_5():
    edad = int(input('cual es tu edad: '))
    ingre = int(input('cuanto de ingreso mensual: '))

    if edad < 16:
        print('no puedes tributar por tu edad')
    elif ingre < 100000:
        print('no puedes tributar por la cantidad de dinero')
    else:
        print('si puedes tributar')


def practice_6():
    nomb = input('cual es tu nombre?: ')
    sex = int(input('eres [1]hombre o [2]mujer?: '))

    a = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
    b = ['n','o','p','q','r','s','t','u','v','w','x','y','z']

    if sex == 1 and nomb[0] in b:
        print('perteneces al grupo b')
    elif sex == 2 and nomb[0] in a:
        print('perteneces al grupo a')
    else:
        print('perteneces al grupo c')

def practice_7():
    rent = int(input('renta anual: '))

    if rent < 10000:
        print('tu inpositivo es 5%')
    elif rent > 10000 and rent < 20000:
        print('tu inpositivo es 15%')
    elif rent > 20000 and rent < 35000:
        print('tu inpositivo es 20%')
    elif rent > 35000 and rent < 60000:
        print('tu inpositivo es 30%')
    elif rent > 60000:
        print('tu inpositivo es 45%')
    else:
        pass


def practice_9():
    edad = int(input('cual es tu edad?: '))

    if edad < 4:
        print('menores de 4 no pagan')
    elif edad > 4 and edad < 18:
        print('debe pagar 5 $')
    else:
        print('debe pagar 10 $')




if __name__ == '__main__':
    menu = int(input('cual ejercicio desea realizae?: '))
    if menu == 1:
        practice_1()
    elif menu == 3:
        practice_3()
    elif menu == 5:
        practice_5()
    elif menu == 6:
        practice_6()
    elif menu == 7:
        practice_7()
    elif menu == 9:
        practice_9()
    else: 
        print('jaja gracias pues c:')