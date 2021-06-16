import pandas as pd
global lista #definimos lista servicios
lista = list()

# creamos la clase Servico
class Servicio:
    unidad = ""
    monto  =0
 
def registrarServicio():
	#print "Registro de Servicios"
     s =  Servicio()
     s.unidad = input("Ingresar unidad del servicio ")
     s.monto = float(input("Ingresar monto "))
     lista.append(s);

def listarServicio():
    for s in lista:
     print (s.unidad ," Monto ", s.monto)

def search(valor):
    for x in lista:
        if x.monto == valor:
          print("El servicio con mayor monto es ",x.unidad,x.monto)
          break
    else:
        x = None
   
def EncontrarMayorMontoServicio():
    hiscore = 0
    for x in lista:
       count = 0
       if x.monto > hiscore:
              hiscore = x.monto
              count += 1
    print("El mayor monto es  ",hiscore)
    search(hiscore)


def listarServicioAgrupados():
     df = pd.DataFrame(o.__dict__ for o in lista)
     print("Listando los servicios")
     print(df)
     df.groupby(['unidad'])['monto'].sum().reset_index()
     print("Listando los servicios acumulados")
     print( df.groupby(['unidad'])['monto'].sum().reset_index())

# bloque principal
name = input("########## REGISTRO SEMANAL DE REGISTROS POR UNIDAD  ###########")
while name != "ok":
    name = input("########### Ingresar los datos. Escriba ok para finalizar el programa  ###########")
    if name !="ok":
     registrarServicio()

#listarServicio()
EncontrarMayorMontoServicio()
listarServicioAgrupados()
