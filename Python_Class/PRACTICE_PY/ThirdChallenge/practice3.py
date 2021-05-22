def run():
    nombre = input('cual es tu nombre?: ')
    apellido = input('cual es tu apellido?: ')
    pais = input('cual es tu pais de origen?: ')

    print(nombre.capitalize() + apellido.capitalize() + pais.capitalize())


    
if __name__ == '__main__':
    run()