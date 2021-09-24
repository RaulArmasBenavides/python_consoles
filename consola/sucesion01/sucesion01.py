"""  Escriba un programa que calcule términos de la sucesión Un+1 = 3 Un + 1, si Un es impar y Un+1 = Un / 2, si Un es par. 
El programa tiene que pedir el término U0 y el número de términos a calcular. Muestre la lista. 
a. 
Muestre los elementos que se encuentren en el medio y los extremos. 
b. Agregue dos números mayores a la lista mostrada. 
c. Solicite un número y verifique que no está dentro de la lista, además que dichos números estén dentro de los valores extremos de la lista. 
Insértelo en la posición siguiente del mayor menor, es decir: [2, 5, 7, 9] y si ingreso 8 debe estar después del 7. 
d. Solicite un número y verifique que no está dentro de la lista, además que dichos números estén dentro de los valores extremos de la lista. 
Insértelo en la posición siguiente del mayor menor, es decir: [2, 5, 7, 9] y si ingreso 8 debe estar después del 7; 
además elimine el mayor menor del número ingresado.
"""  
import locale

def funcionSecuencia(Lista,n)->float:
 try:
 
   if n%2==0 :
         return [3*n+1 for n in Lista]
   else: 
         return [n/2 for n in Lista]
 except Exception as e: 
        print("Hubo un error en el proceso de la lista")
        print( type(e).__name__)
 finally:
        print("Secuencia creada")


def crearLista(n):
 try:
   lst = []
   for i in range(n+1):
        lst.append(i)
   return(lst)
 except Exception as e: 
        print("Hubo un error en la creación de la lista")
        print( type(e).__name__)
 finally:
        print("Lista creada")
   

#Bloque principal 

locale.setlocale(locale.LC_ALL,'es')
cantidad =0 
Lista = []
ListaSecuencia = []
cantidad = int(input("Ingrese el número de términos a calcular: "))
Lista = crearLista(cantidad)
print(Lista)
ListaSecuencia = funcionSecuencia(Lista,cantidad)
print(ListaSecuencia)
elemento1 = int(input("Ingrese un n1 para agregar a la ListaSecuencia: "))
elemento2 = int(input("Ingrese un n2 para agregar a la ListaSecuencia: "))
#Ingrese dos elementos
while ListaSecuencia.count(elemento1) > 0  or  ListaSecuencia.count(elemento2)> 0:
   print("Por favor ingrese números que no estén en la ListaSecuencia")
   elemento1 = int(input("Ingrese un n1 para agregar a la ListaSecuencia: "))
   elemento2 = int(input("Ingrese un n2 para agregar a la ListaSecuencia: "))
else:
		print("Validación correcta")
ListaSecuencia.append(elemento1)
ListaSecuencia.append(elemento2)
ListaSecuencia.sort()
print(ListaSecuencia)	