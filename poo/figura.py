""" Se pide que cree una clase rectángulo y una clase cuadrado, y una super clase, figura.
 Los atributos para el rectángulo es cada lado y del cuadrado es el lado. 
 Debe crear un constructor para figura y crear los métodos que permitan calcular el perímetro, 
 el área y graficar cada uno. Se deben solicitar los datos correspondientes y 
 debidamente validados para hacer los cálculos correspondientes.""" 
 
#Se importa sqrt de math
from math import sqrt
#Se importa ABCMeta, abstractmethod, abstractproperty
from abc import ABCMeta, abstractmethod,abstractproperty
from turtle import * 
import time


# creamos la clase Figura
class Figura:
    # inicializamos los atributos de la clase
  class Figura(object):

    #__metaclass__ = ABCMeta

    @abstractmethod
    def area(self):
    #Calcula el area
        pass

    @abstractmethod
    def perimetro(self):
    #Calcula el perimetro"""
        pass

    @abstractmethod
    def graficar(self):
    #se grafica con la librería turtle"""
        pass


class Rectangulo(Figura):
    """ Esta clase modela un rectángulo en el plano. """

    def __init__(self, base, altura):
        """ base (número) es la longitud de su base,
            altura (número) es la longitud de su base,
            origen (Punto) es el punto del plano de su esquina
            inferior izquierda. """
        self.base = base
        self.altura = altura


    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def graficar(self):
        forward(self.base*10)
        left(90)
        forward(self.altura*10)
        left(90)
        forward(self.base*10)
        left(90)
        forward(self.altura*10)
        left(90)
        exitonclick()

# Esta clase modela un cuadrado en el plano.
class Cuadrado(Figura):
     
    def __init__(self, lado):
        """ base (número) es la longitud de su base,
            altura (número) es la longitud de su base,
            origen (Punto) es el punto del plano de su esquina
            inferior izquierda. """
        self.lado = lado
        

    def area(self):
        return self.lado * self.lado

    def perimetro(self):
        return self.lado*4

    def graficar(self):
        for i in range(4):
            forward(self.lado*10)
            right(90)
        exitonclick()


# bloque principal
print("*APLICATIVO DE FIGURAS*")
figura = input("Ingresar figura que desea graficar (C) para cuadrado o (R) para rectángulo :")
if figura =="C":
 lado = float(input("Ingresar longitud de lado: "))
 cu = Cuadrado(lado);
 AREA = cu.area()
 PERIMETRO = cu.perimetro()
 cu.graficar()
elif figura =="R":
  base = float(input("Ingresa longitud de la base : "))
  altura = float(input("Ingresa la altura de la base : "))
  rec= Rectangulo(base,altura)
  AREA = rec.area()
  PERIMETRO = rec.perimetro()
  rec.graficar()

else:
 print("No está configura la figura en el aplicativo.Por favor revise")


print("Presione enter para imprimir datos")
#time.sleep(25)
print("El perímetro del polígono es:", PERIMETRO)
print("El área del polígono es :", AREA)
