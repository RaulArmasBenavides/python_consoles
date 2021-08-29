import pandas as pd
from tqdm import tqdm 
from time import sleep 
import random


global lista #definimos lista servicios
lista = [] 
# creamos la clase Servico
class Transaccion:
    tipo = ""
    monto=0

    # inicializamos los atributos de la clase

  

    def __init__(self,num_cajero,DNI,tipo,monto):
        self.num_cajero = num_cajero
        self.DNI=DNI
        self.tipo=tipo
        self.monto = monto
 
    # imprimimos los datos de la transacción
    def __str__(self):
        print("El titular de la cuenta con DNI : {} ha realizando la transaccion {} con monto S/.{}".format(self.DNI,self.tipo,self.monto))
        print("Esta transacción se realizó")

    def __del__(self):
        print("Destruyendo objeto")
 

def registrarTransaccion(num_cajero,dni):
     t = Transaccion(num_cajero,dni,"",0)
     t.tipo = input("Ingresar el tipo de la transacción : ")
     t.monto = float(input("Ingresar monto S/.: "))
     return t 

def listarTransaccion(lista):
    #s =  Transaccion("","","",0)
    for s in lista:
     print("num_cajero,dni,tipo trans,monto")
     print(s)

    

def EncontrarMayorMontoTransaccion():
    hiscore = 0
    for x in lista:
       count = 0
       if x.monto > hiscore:
              hiscore = x.monto
              count += 1
    #print("El mayor monto es  ",hiscore)
    search(hiscore)

def search(valor):
    for x in lista:
        if x.monto == valor:
          print("La transaccion con mayor monto es ",x.tipo)
          break
    else:
        x = None


def AgruparTransacciones():
     df = pd.DataFrame(o.__dict__ for o in lista)
     print("Listando las transacciones")
     print(df)
     print("Listando las transacciones agrupadas por tipo de transaccion")
     print(df.groupby(['tipo']).agg(['mean', 'count']))
    

     print("Contando las transacciones por cajero")
     print(df.groupby(['tipo']).agg(['count']))

     #print( df.groupby(['tipo'])['monto'].sum().reset_index())
     #promedio por tipo de transaccion
     #df["monto"].mean()

# bloque principal

name = input("########## REGISTRO DE TRANSFERENCIA ###########")  
cajeros = "1234567"
   
# exception raised

while name != "ok":
    DNI = input("Ingrese DNI: ")
    print("CAJERO # :",random.choice(cajeros)) 
    num_cajero = random.choice(cajeros)
    name = input("########### Registrar la transacción. Escriba ok para finalizar el programa  ###########")
    if name !="ok":
     lista.append(registrarTransaccion(num_cajero,DNI))

#listarServicio()

##listarTransaccion(lista)
for obj in lista:
    print( obj.num_cajero, obj.DNI , obj.tipo, obj.monto )

EncontrarMayorMontoTransaccion()
AgruparTransacciones()

