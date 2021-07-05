import datetime 
import locale


locale.setlocale(locale.LC_ALL,'es')





#es buena pràctica  indicar el tipo de datos que devuelve el método
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





