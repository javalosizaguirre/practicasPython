from cuadrado import Cuadrado
from figura_geometrica import FiguraGeometrica

#No es posible crear objetos de una clase abstracta
#figuraGeometrica = FiguraGeometrica()
cuadrado = Cuadrado(4, "rojo")
print(cuadrado.area())
print(cuadrado.color)

# Method Resolution Order
print(Cuadrado.mro())
