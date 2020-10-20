def practice_1():
    lista = ['mate','fisica','quimica','historia','lengua',]
    print(f'yo estudio {lista}')
    notas = []
    for i in lista:
        nota = input('que nota sacaste en cada asignatura?: ')
        print(f'en {i} sacaste {nota}')
        notas.append(nota)
        print(notas)


def practice_4():
    numeros = []
    for i in range(4):
        nume = int(input('cuales son los numero de la loteria?: '))
        numeros.append(nume)
        numeros.sort()
    print(numeros)

    inv = [1,2,3,4,5,6,7,8,9,10]
    inv.sort(reverse=True)
    print(inv)


def practice_5():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(alphabet), 1, -1):
        if i % 3 == 0:
            alphabet.pop(i-1)
    print(alphabet)


# \Users\steve\Documents\practice
if __name__ == '__main__':
    menu = int(input('cual ejercicio desea realizae?: '))
    if menu == 1:
        practice_1()
    elif menu == 4:
        practice_4()
    elif menu == 6:
        practice_6()
    elif menu == 10:
        practice_10()
    elif menu == 9:
        practice_9()
    else: 
        print('jaja gracias pues c:')