#busca de manera sequencial y cual es el peor caso?
#
import random
def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista: #O(n)
        if elemento == objetivo:
            match = True
            break

    return match

if __name__ == '__main__':
    tamano_lista = int(input('de que tamano sera la lista? '))
    objetivo = int(input('que numero quieres encontrar? '))
    lista = [random.randit(0,100) for i in range(tamano_lista)]
    encontrado = busqueda_lineal(lista, objetivo)

    print(lista)
    print(f'el elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')