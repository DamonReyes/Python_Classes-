def run():
    pass
    cantidad = int(input('cuanta cantidad de millas quieres?: '))
    km = 1.609344

    total = cantidad * km
    total = str(total)
    print(total + ' ' + 'kilometros')



if __name__ == '__main__':
    run()