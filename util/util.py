import datetime 
import locale


locale.setlocale(locale.LC_ALL,'es')



def multiples(n,m,starting_from=1,increment_by=1):
    """
    #Una forma elegante para calcular los múltiplos 
    # Where n is the number 10 and m is the number 2 from your example. 
    # In case you want to print the multiples starting from some other number other than 1 then you could use the starting_from parameter
    # In case you want to print every 2nd multiple or every 3rd multiple you could change the increment_by 
    """
    print(n*x for x in range(starting_from,m+1,increment_by))

#es buena práctica  indicar el tipo de datos que devuelve el método
# método para determinar si es par o impar
def par_o_impar(numero) -> str:
  if (numero%2) == 0:
    return "PAR"
  else:
  	return "IMPAR"


def dividir(a, b) -> float:
    try:
        return a/b
    except Exception as e: 
        print("No se puede dividir entre cero")
        print( type(e).__name__)
    finally:
        print("Proceso finalizado")


#ahora
dt = datetime.datetime.now()   
#print(dt.year)
#print(dt.month)
#print(dt.year)
#print(dt.minute)
#print(dt.second)
#print(dt.microsecond)
#print(dt)
tiempo = dt.strftime("%A %d %B %Y  %T:%H")
print(tiempo)
tiempo2 = dt.strftime("%A %d %B del %Y  %H:%M")
print(tiempo2)


cadena_sample1="Hola Mundo".upper()
print(cadena_sample1)
cadena_sample1="Hola Mundo".lower()
print(cadena_sample1)
cadena_sample1="Hola Mundo".capitalize()
print(cadena_sample1)
cadena_sample1="Hola Mundo".title()

#determinar el nro de veces que aparece un caracter
nro_veces = cadena_sample1.count('o')


#borrar los espacios 
cadena_aux ="        hola     mundo !    ".strip()
print(cadena_aux)
cadena_aux ="*hola mundo!***".strip('*')
print(cadena_aux)









