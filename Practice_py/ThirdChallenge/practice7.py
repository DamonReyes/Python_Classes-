def run():
    pal1 = input('ingresa una palabra a traducir: ')
    letra = pal1[0]
    letra2 = pal1[-1]
    vocal = ['a','e','i','o','u']
    
    if letra in vocal:
        pal1 += 'way'
        print(pal1)
    else:
        pal1 += 'ay'
        print(pal1.replace(letra, letra2))




if __name__ == '__main__':
    run()