#La encapsulación nos permite agrupar datos y controlar su 
# comportamiento en nuestra clase. También nos permite 
# controlar el acceso a nuestros datos y prevenir 
# modificaciones no autorizadas.
#Si por ejemplo, queremos controlar el acceso a una de 
#nuestras variables o realizar una acción adicional al 
#intentar acceder a un dato lo podremos hacer con los getters 
#y setters.
# con getters accedemos a variable privada @property
# con setters sobreescribimos la info de la variable .setter
class ListadoBebidas:

    def __init__(self):
        self._bebida = 'Test cola'
        self._bebidas_validas = ['Test cola', 'Cerveza']

    @property
    def bebida(self):
        return f'La bebida oficial es {self._bebida}'

    @bebida.setter
    def bebida(self, bebida):
        if bebida in self._bebidas_validas:
            self._bebida = bebida
        else:
            raise ValueError(f'La bebida {bebida} no está en el listado de bebidas válidas')

if __name__ == "__main__":
    bebidas = ListadoBebidas()
    print(bebidas.bebida)
    bebidas.bebida = 'Limonada'