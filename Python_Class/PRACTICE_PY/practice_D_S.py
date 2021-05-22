def practice_1():
    nomb = input('cual es tu nombre?: ')
    nume = int(input('escribe el numero de reps: '))
    print(f' {nomb} tiene {len(nomb)} letras')

    math1 = 2+3/2.5**2
    print(math1)


def practice_7():
    horas = int(input('numero de horas trabajadas?: '))
    coste = horas * 1000
    paga = print(f'su paga es {coste} por {horas} horas')

    ent = int(input('entero: '))
    suma = ent + 1 **2
    print(suma)


def practice_9():    
    peso = int(input('cual es tu peso? en kg: '))
    estatura = float(input('cual es tu estatura? en mts:'))
    imc = peso / estatura **2
    print(f'Tu indice de masa corporal es {round(imc, 3)}')


def practice_10():  
    num1 = int(input('digita un numero: '))
    num2 = int(input('digita otro numero: '))
    cociente = num1 // num2
    resto = num1 % num2
    print(f'{num1} entre {num2} da un cociente de {cociente} y un resto de {resto}')

    

def practice_11():
    cantidad = int(input('digita la cantidad a invertir: '))
    interes =  int(input('digita el interes anual: '))
    anos = int(input('digite la cantidad de anos: '))
    oper = cantidad * interes / 100
    oper2 = oper * anos
    print(f'el capital de la inversion es {oper} y por {anos} anos seria {oper2}')


def practice_12():
    pes_clown = 112
    pes_doll = 75
    clown = int(input('cuantos payasos vendieron?: '))
    doll = int(input('cuantas munecas vendieron?: '))
    print(clown * pes_clown)
    print(doll * pes_doll)
    peso = (pes_clown + pes_doll) * (clown + doll)
    print(f'el peso total de la venta es {peso}')


def practice_13():
    ano1 = int(input(''))
    ano2 = int(input(''))
    ano3 = int(input(''))
    suma = ano1 + ano2 + ano3
    interes = 4.20
    operacion = suma * interes
    print(f'la cantidad de ahorro en estos 3 anos es {operacion}')


def practice_14():
    pan = 600
    panan = pan / 0.6

    barrasan = int(input('cuantas barras anejas quieres?: '))
    total  = pan * barrasan
    print(f'el total es {total}')
    print(f'se hixo un descuento de {panan}')




if __name__ == '__main__':
    hi = print('hola mundo!')

    menu = int(input('cual ejercicio desea realizae?: '))
    if menu == 1:
        practice_1()
    elif menu == 7:
        practice_7()
    elif menu == 9:
        practice_9()
    elif menu == 10:
        practice_10()
    elif menu == 11:
        practice_11()
    elif menu == 12:
        practice_12()
    elif menu == 13:
        practice_13()
    elif menu == 14:
        practice_14()
    else: 
        print('jaja gracias pues c:')