#busqueda binaria
#divide y conquista, se divide en 2 por iteracion, peor caso

import random

def busqueda_binaria(lista, comienzo, final, objetivo):
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    if comienzo > final:
        return False

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio -1, objetivo)



if __name__ == '__main__':
    tamano_lista = int(input('de que tamano sera la lista? '))
    objetivo = int(input('que numero quieres encontrar? '))
    lista = sorted([random.randit(0,100) for i in range(tamano_lista)])
    encontrado = busqueda_binaria(lista,0, len(lista), objetivo)

    print(lista)
    print(f'el elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')