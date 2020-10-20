def run():
    oracion = input('indica una oracion de 10 o mas caracteres: ')
    long = len(oracion)
    ini = int(input('numero de rango inicial: '))
    fina = int(input('numero de rango final: '))
    
    print(oracion[ini:fina + 1])



if __name__ == '__main__':
    run()