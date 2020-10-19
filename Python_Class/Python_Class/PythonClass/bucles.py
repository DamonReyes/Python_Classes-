def run():
    LIMITE = 1000
# se pone en mayuscula para que sea constante(contrario de variable)
# osea no cambia y siempre es igual
    contador = 0
    potencia = 2**contador
    while potencia < LIMITE:
        print('2 elevado a ' + str(contador) + 'es igual a: ' + str(potencia))
        contador = contador + 1
        potencia = 2**contador

if __name__ == '__main__':
    run()