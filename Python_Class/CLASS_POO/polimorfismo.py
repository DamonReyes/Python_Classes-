# habilidad de tomar varias formas
#nos permite cambiar el comportamiento de una superclase para
#adaptarlo a la subclase
#
class Vehiculo:

    def __init__(self, nombre):
        self.nombre = nombre

    def num_ruedas(self):
        pass

class Motocicleta(Vehiculo):
    def __init__(self):
        super().__init__('Motocicleta')

    def num_ruedas(self):
        return 2

#if __name__ == "__main__":
    #moto = Motocicleta()
    #print(moto.num_ruedas())


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print('ando caminando')

class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('ando en bici')


def main():
    persona = Persona('david')
    persona.avanza()

    ciclista = Ciclista('daniel')
    ciclista.avanza()



if __name__ == "__main__":
    main()