def run():
    curso = input('cual es tu animal favorito?: ')
    cant = int(input('cuantas veces?: '))
    
    for i in curso * cant:
        print(i)


if __name__ == '__main__':
    run()