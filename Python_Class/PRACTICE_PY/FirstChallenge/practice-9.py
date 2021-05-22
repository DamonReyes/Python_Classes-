def run():
    cantidad_dias = int(input('de cuantos dias ocupas la infromacion? '))

    hora = 24
    minuto = 1440
    segundo = 86400

    total1 = hora * cantidad_dias
    total2 = minuto * cantidad_dias
    total3 = segundo * cantidad_dias
    total1 = str(total1)
    total2 = str(total2)
    total3 = str(total3)
    print('hay' + total1 + 'horas en esa cantidad de dias')
    print(total1)
    print('horas en esa cantidad de dias')
    print(total2)
    print('minutos en esa cantidad de dias')
    print(total3)
    print('segundos en esa cantidad de dias')

if __name__ == '__main__':
    run()