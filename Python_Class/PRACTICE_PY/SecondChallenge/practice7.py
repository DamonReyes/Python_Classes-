def run():
    numero = int(input('indica un numero entre 1 y 6: '))
    
    if numero > 6 or numero < 1:
        print('escoge un numero en el rango')
        run()
    elif numero == 1:
        print('Hoy aprenderemos sobre prorgamación')
    elif numero == 2:
        print('¿Qué tal tomar un curso de marketing digital?')
    elif numero == 3:
        print('Hoy es un gran día para comenzar a aprender de diseño')
    elif numero == 4:
        print('¿Y si aprendemos algo de negocios online?')
    elif numero == 5:
        print('Veamos un par de clases sobre producción audiovisual')
    elif numero == 6:
        print('Tal vez sea bueno desarrollar una habilidad blanda en Platzi')
    else:
        pass

if __name__ == '__main__':
    run()