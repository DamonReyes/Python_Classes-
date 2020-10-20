def run():
    curso = input('cual es tu curso favorito en platzi?: ')
    veces = int(input('que cantidad de veces se repite?: '))
    
    if veces > 15:
        for i in range(3):
            print(curso)
        print('tu numero es muy grande')
    else:    
        for i in range(veces):
            print(curso)


if __name__ == '__main__':
    run()