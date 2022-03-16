#TEMA : MATETMÁTICAS
#ax2 + bx + c = 0 
import math

def ecuacion2grado(a,b,c)->float:
 try:
   x = (b**2)-(4*a*c)
   if x < 0 :
        print("Solucion solo en numeros complejos,se mostrará parte real e imaginaria")   
        x1 = -b/(2*a) #-> parte real 
        x2 = math.sqrt(abs(x))/(2*a) #->parte imaginaria 
   else :
        x1 = (-b + math.sqrt(x)) / (2*a)
        x2 = (-b - math.sqrt(x)) / (2*a)
   return x,x1,x2
 except Exception as e: 
        print("Hubo un error en el cálculo")
        print( type(e).__name__)
 finally:
        print("Proceso finalizado")


#Pedimos la entrada de los tres valores de la ecuación
a = float(input("Ingrese el valor de a: ")) # a = cociente del termino cuadrático
b = float(input("Ingrese el valor de b: ")) # b = cociente de termino lineal
c = float(input("Ingrese el valor de c: ")) # c = cociente de termino independiente

resultado = ecuacion2grado(a,b,c)
#Imprimiendo  resultados
if resultado[0]>0 :
  print("resultado: x1", resultado[1] , "x2", resultado[2])
else: #si el resultado es complejo 
  print("resultado: x1", resultado[1],"+",resultado[2],"i")
  print("resultado: x1", resultado[1],"-",resultado[2],"i")