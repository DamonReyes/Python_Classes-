
def run():
    num = 1
    song = print(f'{num} elefante se balanceaba Sobre la tela de una araña, Como veía que resistía, Fueron a llamar otro elefante')
    preg1 = int(input('cuantos elefantes se balancearan?: '))

    num += 1

    while num == preg1:
        song = print(f'{num} elefante se balanceaba Sobre la tela de una araña, Como veía que resistía, Fueron a llamar otro elefante')
        num += 1
        preg1 = int(input('cuantos elefantes se balancearan?: '))
        if preg1 != num:
            print('intente denuevo')
            run()
        elif preg1 == 10:
            song = print(f'{num} elefante se balanceaba Sobre la tela de una araña, Como veía que resistía, Fueron a llamar otro elefante')
            print('final')
            break
        break


    
# Escribe un programa que inicie mostrando en pantalla la letra 
# de “Un elefante se balanceaba” iniciando con el número 1, 
# después pregunta al usuario cuantos elefantes más se 
# balancearán y debe responder un número más al mostrado. 
# En caso de ingresar un número diferente pedirle que intente 
# de nuevo y repetir el ciclo hasta tener 10 elefantes.
# Tomar en cuenta cuando el texto muestra un solo elefante y 
# varios elefantes.
# Ejemplo de inicio:

# def run():
    # num = 1
    # mensaje = 'elefante se balanceaba \n Sobre la tela de una araña \n Como veía que resistía \n Fue a llamar otro elefante'
    # print(f'{num} {mensaje}')
    # mensaje1='elefantes se balanceaban \n Sobre la tela de una araña \n Como veíanque resistían \n Fueron a llamar otro elefante'
    # while num<10:
    #     preg=int(input('¿Cuantos elefantes más se balancearán? '))
    # while preg!=num+1:
    #     preg=int(input(f'Ingresa un numero que sea mayor a {num} mas 1 ¿Cuantos elefantes más se balancearán?: '))
    #     num=num+1
    #     print(f'{num} {mensaje1}')


if __name__ == '__main__':
    run()