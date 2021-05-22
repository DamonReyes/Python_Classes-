#enfocarnos en la info relevante
#separar las variables con '_'
#en POO lo def son 'Metodos' y siempre recibe 'self'
#con un '_' se hace un metodo o variable, protegido
# y con '__' se hacen privados
#cuando se agrega el '_' es para restarle importancia

class Automovil:
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en reposo'
        self._motor = Motor(cilindro=4)

    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.llenar_tanque(10)
        else:
            self._motor.llenar_tanque(3)

        self._estado = 'en movimineto'

class Motor:
    def __init__(self, cilindro, tipo='gasolina'):
        self.cilindro = cilindro
        self.tipo = tipo
        self._temperatura = 0

    def llenar_tanque(self, cantidad):
        self.cantidad = cantidad

################################################
################################################

class Lavadora:
    def __init__(self):
        pass

    def lavar(self, temperature='frio'):
        self._llenar_agua(temperature)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_agua(self, temperature):
        print(f'llenando el tanque con agua {temperature}')

    def _anadir_jabon(self):
        print(f'anadiendo jabon')

    def _lavar(self):
        print(f'lavando la ropa')

    def _centrifugar(self):
        print(f'centrifugando la ropa')


if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar