

class Proyectil:

    # CONSTANTES
    GRAVEDAD = 9.81

    # Constructor
    def __init__(self, nombre):
        self.nombre = nombre
        print(f'Se ha creado un objeto llamado {self.nombre}')

    def establecer_parametros_iniciales(self, velocidadInicial, velocidadFinal, angulo):
        # Propiedades
        self.velocidadInicial = velocidadInicial
        self.velocidadFinal = velocidadFinal
        self.angulo = angulo

    def calcular_altura(self):
        y = (self.velocidadFinal * self.velocidadFinal - self.velocidadInicial * self.velocidadInicial) / (2 * self.GRAVEDAD)

        print (f'y (altura de {self.nombre} )= ', y)

def main():
    print('Dentro de main')
    piedra = Proyectil("piedra")
    piedra.establecer_parametros_iniciales(0,50,0)
    piedra.calcular_altura()

    bala = Proyectil("bala")
    bala.establecer_parametros_iniciales(0,100,0)
    bala.calcular_altura()

if __name__ == "__main__":
    main()
