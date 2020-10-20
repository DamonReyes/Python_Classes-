def run():
    num1 = float(input('ingresa un numero con decimales: '))
    num2 = float(input('ingresa otro numero con decimales: '))

    mult = num1 * num2

    print(round(mult, 2))


if __name__ == '__main__':
    run()