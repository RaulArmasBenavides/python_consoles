
# creamos la clase Cuenta
class Cuenta:
	# inicializamos los atributos de la clase
	def __init__(self,titular,cantidad):
		self.titular=titular
		self.cantidad=cantidad
 
	# imprimimos los datos
	def imprimir(self):
		print("Titular: ",self.titular)
		print("Cantidad: ", self.cantidad)
 
 
# creamos la clase CuentaAhorro
# esta clase hereda atributos de la clase Cuenta
class CuentaAhorro(Cuenta):
	# iniciamos los atributos de la clase
	def __init__(self,titular,cantidad):
		super().__init__(titular,cantidad)
 
	# imprimimos los datos de la cuenta
	def imprimir(self):
		print("Cuenta de caja de ahorros")
		super().imprimir()
 
 
# creamos la clase PlazoFijo
# esta clase también hereda atributos de la clase Cuenta
class PlazoFijo(Cuenta):
	# inicializamos los atributos de la clase
	def __init__(self,titular,cantidad,plazo,interes):
		super().__init__(titular,cantidad)
		self.plazo=plazo
		self.interes=interes
 
 
	# calculamos la ganancia
	def ganancia(self):
		ganancia=self.cantidad*self.interes/100
		print("El importe de interés es: ",ganancia)
 
 
	# imprimimos los resultados
	def imprimir(self):
		print("Cuenta a plazo fijo")
		super().imprimir()
		print("Plazo disponible en días: ",self.plazo)
		print("Interés: ",self.interes)
		self.ganancia()
 #clase Cliente

class Cliente:
    cfijo = PlazoFijo("",0,0,0)
    cahorro = CuentaAhorro("",0)
    def __init__(self,nombre):
        self.nombre=nombre
      
    def Registrar(self,nombre,apellido,dni):
         self.nombre = nombre 
         self.apellido = apellido
         self.dni = dni
         print("Bienvenido sr(a)" ,nombre,"", apellido,"DNI",dni)
    #Cada vez que se cree una cuenta se especificará si es tipo F ( plazo fijo) o tipo A ( cuenta de ahorro)
     
    def CrearCuenta(self,nombre,monto,tipo):
         if tipo == "F":
          self.cfijo.titular = nombre 
          self.cfijo.plazo = float(input("Para depósitos a plazo fijo debe ingresar el plazo en días: "))
          self.cfijo.interes = float(input("Ingrese la tasa de interés: ")) 
          self.cfijo.cantidad = self.cfijo.cantidad + monto
          self.cfijo.imprimir()
         elif tipo =="A":
          self.cahorro.cantidad = self.cahorro.cantidad + monto 
          self.cahorro.titular =nombre 
          self.cahorro.imprimir()
         print("Cuenta creada")

    def depositar(self,monto,tipo):
        if tipo == "F":
         self.cfijo.cantidad = self.cfijo.cantidad + monto
         self.cfijo.imprimir()
        elif tipo =="A":
         self.cahorro.cantidad = self.cahorro.cantidad + monto 
         self.cahorro.imprimir()


    def extraer(self,monto,tipo):
        if tipo == "F":
         self.cfijo.cantidad = self.cfijo.cantidad - monto
         self.cfijo.imprimir()
        elif tipo =="A":
          self.cahorro.cantidad = self.cahorro.cantidad - monto 
          self.cahorro.imprimir()

    def retornar_monto(self,tipo):
         if tipo =="F":
            return self.monto
         elif tipo == "A":
            return self.monto
    
    def imprimirSaldo(self,tipo):
        if tipo =="F":
           print("Sr(a). " ,self.nombre,"tiene depositado la suma de",self.cfijo.cantidad)
           self.cfijo.imprimir()
        elif tipo == "A":
           print("Sr(a). " ,self.nombre,"tiene depositado la suma de",self.cfijo.cantidad)
           self.cahorro.imprimir()
 
# bloque principal
print("*APLICATIVO DE CUENTAS*")
cliente1 = Cliente("")
cliente2 = Cliente("")
cliente1.Registrar("Raúl","Armas","73262442")
cliente1.CrearCuenta("Raúl",4000,"A")
#se depositará 200 más
print("DEPOSITANDO...")
cliente1.depositar(200,"A")
print("*******************************")
cliente2.Registrar("Ronnie","Oliva","53260441")
cliente2.CrearCuenta("Ronnie",6000,"F")
print("EXTRAYENDO...")
cliente2.extraer(10,"F")
#caja1=CuentaAhorro("Manuel",5000)
#caja1.imprimir()
 
#plazo1=PlazoFijo("Isabel",8000,365,1.2)
#plazo1.imprimir()