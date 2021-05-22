def run():
    # total a pagar*
    # cuantas personas a dividir cuanta*
    # porcentaje de propina
    # porcentaje de impuestos
    # total incluyendo todo
    # total por persona
    total1 = int(input('cual es el total a pagar?: '))
    propina = total1 * 0.70
    impuesto = total1 * 0.60
    total2 = total1 + propina + impuesto
    print('el total a pagar, mas propina mas impuesto es ')
    print(total2)
    amigos = int(input('cuantos personas son?: '))
    total3 = total2 / amigos
    print('el total por persona seria')
    print(total3)


if __name__ == '__main__':
    run()