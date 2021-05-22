def run():
    curso = input('cual es tu curso favorito en platzi?: ')
    veces = int(input('que cantidad de veces se repite?: '))
    
    for i in range(veces):
        print(curso)


if __name__ == '__main__':
    run()