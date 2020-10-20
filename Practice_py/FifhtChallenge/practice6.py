def run():
    num = int(input('ingresa un numero del 1 al 10?: '))
    
    
    for i in range(num + 1):
        print(num - i)


if __name__ == '__main__':
    run()