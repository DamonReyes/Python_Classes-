def run():
    recta = input('recta p o n?: ')
    num = int(input('ingresa el numero de recta?: '))
    
    if recta == 'p':
        for i in range(num + 1):
            print(i)
    else:
        for i in range(num + 1):
            print(i - num)




if __name__ == '__main__':
    run()