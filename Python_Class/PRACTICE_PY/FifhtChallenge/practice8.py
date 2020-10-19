def run():

    m = 0
    for i in range(4):
        num = int(input('Ingresa tu numero a sumar: '))
        suma = input('¿Desea sumar el numero al resto? Y/n: ')
        
        if suma =='si':
            m = m + num
        else:
            pass

    print(m)

if __name__ == '__main__':
    run()