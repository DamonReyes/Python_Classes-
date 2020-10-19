def run():
    nombre = input('escribe tu nombre invitad@: ')
    preg = input('quieres invitar a alguien mas?: ')
    
    cont = 1
    while preg == 'si':
        nombre = input('escribe tu nombre invitad@: ')
        if nombre == nombre:
            cont += 1
        preg = input('quieres invitar a alguien mas?: ')
    else:
        print(f'son {cont} invitados')





if __name__ == '__main__':
    run()