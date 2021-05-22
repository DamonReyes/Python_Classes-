def run():
    animal = input('cual es tu animal favorito?: ')
    lista = ['tortuga','Tortuga','TORTUGA']

    if animal in lista:
        print('tambien me encantan las tortugas!')
    else:
        print('ese animal es genial, pero prefiero las tortugas')




if __name__ == '__main__':
    run()