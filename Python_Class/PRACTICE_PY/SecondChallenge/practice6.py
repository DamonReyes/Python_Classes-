def run():
    edad = int(input('cual es tu edad?: '))


    if edad > 30:
        print('nunca es tarde para aprender, que curso tomaremos? ')
    elif edad < 18:
        print('sabes hacia donde dirigir tu futuro? seguro puedo ayudarte. ')
    else:
        print('es un momento excelente para impulsar tu carrera! ')



if __name__ == '__main__':
    run()