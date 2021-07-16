#version 1.2

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
#subclases
class CuentaSimple(CuentaAhorro):
    # iniciamos los atributos de la clase
    def __init__(self,titular,cantidad):
        super().__init__(titular,cantidad)
 
    # imprimimos los datos de la cuenta
    def imprimir(self):
        print("Subtipo simple")
        super().imprimir()

class CuentaDigital(CuentaAhorro):
    # iniciamos los atributos de la clase
    def __init__(self,titular,cantidad):
        super().__init__(titular,cantidad)
 
    # imprimimos los datos de la cuenta
    def imprimir(self):
        print("Subtipo simple")
        super().imprimir()


class CuentaSuperTasa(CuentaAhorro):
    # iniciamos los atributos de la clase
    def __init__(self,titular,cantidad):
        super().__init__(titular,cantidad)
 
    # imprimimos los datos de la cuenta
    def imprimir(self):
        print("Subtipo simple")
        super().imprimir()


class CuentaMillonaria(CuentaAhorro):
    # iniciamos los atributos de la clase
    def __init__(self,titular,cantidad):
        super().__init__(titular,cantidad)
 
    # imprimimos los datos de la cuenta
    def imprimir(self):
        print("Subtipo simple")
        super().imprimir()


# esta clase también hereda atributos de la clase Cuenta
class PlazoFijo(CuentaAhorro):
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


class CuentaSueAFP(Cuenta):
    # iniciamos los atributos de la clase
    def __init__(self,titular,cantidad):
        super().__init__(titular,cantidad)
 
    # imprimimos los datos de la cuenta
    def imprimir(self):
        print("Tipo sueldo y AFP")
        super().imprimir()

#subclases
class CuentaSueldo(CuentaSueAFP):
    # iniciamos los atributos de la clase
    def __init__(self,titular,cantidad):
        super().__init__(titular,cantidad)
 
    # imprimimos los datos de la cuenta
    def imprimir(self):
        print("Subtipo Sueldo")
        super().imprimir()

class CuentaAFP(CuentaSueAFP):
    # iniciamos los atributos de la clase
    def __init__(self,titular,cantidad):
        super().__init__(titular,cantidad)
 
    # imprimimos los datos de la cuenta
    def imprimir(self):
        print("Subtipo AFP")
        super().imprimir()



 #clase Cliente

class Cliente:
    cmillonaria = CuentaMillonaria("",0)
    cplazofijo = PlazoFijo("",0,0,0)
    csueldo = CuentaSueldo("",0)
    cafp = CuentaAFP("",0)
    #cfijo = PlazoFijo("",0,0,0)
    #cahorro = CuentaAhorro("",0)
    def __init__(self,nombre):
        self.nombre=nombre
      
    def Registrar(self,nombre,apellido,dni):
         self.nombre = nombre 
         self.apellido = apellido
         self.dni = dni
         print("Bienvenido sr(a)" ,nombre,"", apellido,"DNI",dni)
    #Cada vez que se cree una cuenta se especificará si es tipo SAFP ( sueldo y afp) o tipo A ( cuenta de ahorro)
    #Los subtipos son:

    #Cuenta ahorro
    #PF- > Plazo fijo
    #M -> Cuenta millonario 
    #D -> Cuenta digital 
    #S -> Cuenta Simple

    #Cuenta sueldo y afp 
    #SUEL -> Cuenta sueldo
    #AFP  -> Cuenta AFP
     
    def CrearCuenta(self,nombre,monto,tipo,subtipo):
         if tipo == "A":

            if subtipo =="PF":
             self.cplazofijo.titular = nombre 
             self.cplazofijo.plazo = float(input("Para depósitos a cuentas de ahorro plazo fijo debe ingresar el plazo en días: "))
             self.cplazofijo.interes = float(input("Ingrese la tasa de interés: ")) 
             self.cplazofijo.cantidad = self.cfijo.cantidad + monto
             self.cplazofijo.imprimir()

            elif subtipo =="M":
              self.cafp.cantidad = self.cahorro.cantidad + monto 
              self.cafp.titular =nombre 
              self.cafp.imprimir()

            elif subtipo =="AFP":
              self.cafp.cantidad = self.cahorro.cantidad + monto 
              self.cafp.titular =nombre 
              self.cafp.imprimir()

            elif subtipo =="AFP":
              self.cafp.cantidad = self.cahorro.cantidad + monto 
              self.cafp.titular =nombre 
              self.cafp.imprimir()

         elif tipo =="SAFP":
             if subtipo =="SUEL":
              self.csueldo.cantidad = self.cahorro.cantidad + monto 
              self.csueldo.titular =nombre 
              self.csueldo.imprimir()
             elif subtipo =="AFP":
              self.cafp.cantidad = self.cahorro.cantidad + monto 
              self.cafp.titular =nombre 
              self.cafp.imprimir()

         print("Cuenta creada")

    def depositar(self,monto,tipo,subtipo):
        if tipo == "A":
            if subtipo =="PF":
             self.cplazofijo.cantidad = self.cfijo.cantidad + monto
             self.cplazofijo.imprimir()
        elif tipo =="SAFP":
            if subtipo =="SUEL":
               self.csueldo.cantidad = self.cahorro.cantidad + monto 
               self.csueldo.imprimir()
            elif subtipo =="AFP":
               self.cafp.cantidad = self.cahorro.cantidad + monto  
               self.cafp.imprimir()



    def extraer(self,monto,tipo,subtipo):
        if tipo == "A":
            if subtipo =="PF":
              self.cplazofijo.cantidad = self.cfijo.cantidad - monto
              self.cplazofijo.imprimir()
        elif tipo =="SAFP":
            if subtipo =="SUEL":
              self.csueldo.cantidad = self.cahorro.cantidad - monto 
              self.csueldo.imprimir()
            elif subtipo =="AFP":
              self.cafp.cantidad = self.cahorro.cantidad - monto  
              self.cafp.imprimir()

    def retornar_monto(self,tipo,subtipo):
         if tipo =="F":
            return self.monto
         elif tipo == "A":
            return self.monto
    
    def imprimirSaldo(self,tipo,subtipo):
        if tipo =="F":
           print("Sr(a). " ,self.nombre,"tiene depositado la suma de",self.cfijo.cantidad)
           self.cplazofijo.imprimir()
        elif tipo == "A":
           print("Sr(a). " ,self.nombre,"tiene depositado la suma de",self.cfijo.cantidad)
           self.cahorro.imprimir()
 
# bloque principal
print("*APLICATIVO DE CUENTAS*")
cliente1 = Cliente("")
cliente2 = Cliente("")
cliente1.Registrar("Raúl","Armas","73262442")
cliente1.CrearCuenta("Raúl",4000,"A","PF")
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