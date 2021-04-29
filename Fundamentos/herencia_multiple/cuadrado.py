from figura_geometrica import FiguraGeometrica
from color import Color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        # Inicializando los valores de las clases padres
        FiguraGeometrica.__init__(self, lado, lado)
        # Inicializando los valores de las clases padres
        Color.__init__(self, color)
        # super().__init__(lado,lado) -> Si es una sola clase se realiaza esta linea, al ser dos clases se inicializa como arriba

    def area(self):
        return self.alto*self.ancho
