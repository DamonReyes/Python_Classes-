def run():
    nombre = input('ingresa tu nombre: ')
    long = len(nombre)

    if long > 5:
        print('hola, ' + nombre.capitalize())
    else:
        apellido = input('cual es tu apellido?: ')
        print('hola, ' + nombre.capitalize() + ' ' + apellido.capitalize())



if __name__ == '__main__':
    run()