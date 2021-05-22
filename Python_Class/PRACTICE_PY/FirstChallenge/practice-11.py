def run():
    mayor = int(input('ingresa un numero mayor a 1000: '))
    menor = int(input('ingresa un numero menor a 100: '))

    total = mayor / menor
    print(round(total, 2))
    
    

if __name__ == '__main__':
    run()