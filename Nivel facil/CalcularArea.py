#* Reto #4
 #* AREA DE UN POLIGONO
 #* Fecha publicacion enunciado: 24/01/22
 #* Fecha publicacion resolucion: 31/01/22
 #* Dificultad: FACIL
 #*
 #* Enunciado: Crea UNA UNICA FUNCION (importante que solo sea una) que sea capaz de calcular y retornar el area de un poligono.
 #* - La funcion recibira por parametro solo UN poligono a la vez.
 #* - Los poligonos soportados seran Triangulo, Cuadrado y Rectangulo.
 #* - Imprime el calculo del area de un poligono de cada tipo.

from abc import ABCMeta
import unittest
#Se indica la interfaz
class Poligono():
    __metaclass__ = ABCMeta
    def calcularArea(self):
        pass

class Triangulo(Poligono):
    def __init__(self, base, altura):
        self.base = base
        self.altura =altura
    def calcularArea(self):
        return float(self.base*self.altura/2)
    
class Cuadrado(Poligono):
    def __init__(self, lado):
        self.lado=lado
    def calcularArea(self):
        return float(self.lado**2)

class Rectangulo(Poligono):
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura
    def calcularArea(self):
        return float(self.base*self.altura)
    
def calcularPoligono(poligono):
    if isinstance(poligono,Poligono):
        return poligono.calcularArea()

class Pruebas(unittest.TestCase):
    def testTriangulo(self):
        triangulo = Triangulo(5, 10)
        self.assertEqual(calcularPoligono(triangulo), 25.0)
    def testRectangulo(self):
        rectangulo = Rectangulo(5, 10)
        self.assertEqual(calcularPoligono(rectangulo), 50.0)
    def testCuadrado(self):
        cuadrado = Cuadrado(5)
        self.assertEqual(calcularPoligono(cuadrado),25.0)
    def testSpecialCases(self):
        self.assertEqual(calcularPoligono(None), None)
        self.assertEqual(calcularPoligono("hola"), None)

unittest.main()