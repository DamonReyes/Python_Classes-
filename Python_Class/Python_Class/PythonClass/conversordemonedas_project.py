def conversor(tipo_pesos, valor_dolar):
    pesos = input(" cuantos pesos" + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares + " dolares")

menu = """ 
Bienvenido al conversor de monedas 

1 - pesos colombianos
2 - pesos argentinos
3 - colones constaricenses

elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("costaricenses", 515)
else:
    print('ingresa una opcion correcta por favor')
# if elif y else son condicionales

