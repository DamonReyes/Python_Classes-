def run():
    name = input('cual es tu nombre? ')
    edad = int(input('cual es tu edad? '))

    resta = edad - 1
    print('tu edad el ano pasado era ')
    print(resta)

    print('*******')

    suma = edad + 1
    print('tu edad el siguiente ano sera ')
    print(suma)



if __name__ == '__main__':
    run()