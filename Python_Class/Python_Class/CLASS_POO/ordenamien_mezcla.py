import random

def ordenamiento_mezcla(lista):
        #caso base
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(izquierda, '*' * 5, derecha)

        #llamada recursiva
        izquierda = ordenamiento_mezcla(izquierda)
        derecha = ordenamiento_mezcla(derecha)

        #iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        #Iterador para la lista principal
        k = 0

        while i< len(izquierda) and j < len(derecha): #mientras podamos seguir comparando
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k+= 1
        #copiar los pedazos de las listas que quedaron
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i+=1
            k += 1
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
        print(f'izquierda  {izquierda}. derecha  {derecha}')
        print(lista)
        print('--' * 30)

    return lista



if __name__ == '__main__':
    tamano_lista = int(input('de que tamano sera la lista? '))
    
    lista = [random.randit(0,100) for i in range(tamano_lista)]
    print(lista)
    print('-' * 2)

    lista_ordenada = ordenamiento_mezcla(lista)
    print(lista_ordenada)