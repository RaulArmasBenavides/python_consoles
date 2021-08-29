from tkinter import *
import tkinter as tk
import mysql.connector
from tkinter import messagebox
import metodos
from metodos import *
from datetime import datetime, date, time, timedelta
from tkinter import font
import os

import xlwt


#--- Devuelve el numero de recetas que hay en la base de datos bdasher en la tabla recetas.
def numeroDeRecetas():
	con=mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='bdasher1')
	cursor=con.cursor()
	cursor = con.cursor(buffered=True)
	var=True
	numRecetas=0
	cursor.execute("select * from recetas")
	while var:
		var=cursor.fetchone()
		if var:
			numRecetas=numRecetas + 1
	return numRecetas
	cursor.close()

#devuelve la cadena invertida
def invertirStr(cadena):
	c = cadena[::-1]
	return c

#Se ingresa un string por parametro con el formato yyyy-mm-dd y lo devuelve como dd-mm-yyyy
def ordenarFechaParaCliente(f):
	fecha=f[8:10]+"-"+f[5:7]+"-"+f[0:4]
	return fecha

#Se ingresa un string por parametro con el formato dd-mm-yyyy y lo devuelve como yyyy-mm-dd
def ordenarFechaParaMysql(f):
	fecha=f[6:10]+"-"+f[3:5]+"-"+f[0:2]
	return fecha


def calcularDeuda(idc):
	con=mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='bdasher1')
	cursor=con.cursor()
	cursor = con.cursor(buffered=True)	
	cursor.execute("SELECT SUM(monto) FROM deuda WHERE idclientes = %s;",(idc,)) # devuelve una sumatoria del total de montos de un cliente idc
	t = cursor.fetchone()

	#El if es por si el cliente no tiene deuda, para que devuelva un cero en lugar de un error.
	if t[0]==None:
		return 0
	else:
		return(t[0]) #deuda total.
	cursor.close()





def actualizarLstDetallesGeneral2(l1,l2,l3,l4,l5):
	con=mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='bdasher1')
	cursor=con.cursor()

	cursor.execute("select * from clientes inner join deuda on clientes.idclientes=deuda.idclientes ORDER BY fecha ASC")
	#-999- este while lo que hace es insertar en la lista lstDeuda los campos fecha y monto asociados al cliente.
	
	l1.delete(0, END)
	l2.delete(0, END)
	l3.delete(0, END)
	l4.delete(0, END)
	l5.delete(0, END)

	tupDetallesGeneral = cursor.fetchone()
	auxDetalleGeneral=True	
	

	while (auxDetalleGeneral and tupDetallesGeneral!=None): #la condicion tupListarDetallesGeneral!=None la pongo por si no tiene deuda. para que no de error.
		DetalleClientesNombre=str(tupDetallesGeneral[1]) #lo convierto a string porque sino no me deja mostrarlo en el listbox
		DetalleClientesApellido=str(tupDetallesGeneral[2])
		DetalleClientesFecha=str(tupDetallesGeneral[5])
		DetalleClientesFechaOrdenada=ordenarFechaParaCliente(DetalleClientesFecha)
		DetalleClientesMonto=str(tupDetallesGeneral[7])
		DetalleClientesDetalle=str(tupDetallesGeneral[8])		
		l1.insert(END,DetalleClientesNombre)
		l2.insert(END,DetalleClientesApellido)
		l3.insert(END,DetalleClientesFechaOrdenada)
		l4.insert(END,DetalleClientesMonto)
		l5.insert(END,DetalleClientesDetalle)


		tupDetallesGeneral=cursor.fetchone()		
		auxDetalleGeneral=tupDetallesGeneral
		#-999-
	cursor.close()


#Esta funcion guarda la fecha de pago en la tabla pagos.
def guardarPago(idCli,dateListaFecha,montoTotal):
	con=mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='bdasher1')
	cursor=con.cursor()
	cursor.execute("select * from clientes where idclientes = %s;",(idCli,))
	t=cursor.fetchone()
	n=t[1] #nombre
	a=t[2] #apellido
	fechaActual = datetime.now() #fecha actual.
	sqlDate="INSERT INTO pagos(idpagos,fecha_compra,monto,fecha_pago,nombre,apellido) VALUES (%s,%s,%s,%s,%s,%s)" #inserta en la tabla pagos los datos.
	cursor.execute(sqlDate,(0,dateListaFecha,montoTotal,fechaActual,n,a))		
	con.commit() #guarda cambios en la base de datos.

#Esta funcion guarda la fecha de pago en la tabla pagos.
def guardarPagoFechaCambiada(idCli,dateListaFecha,montoTotal,fechaCambiada):
	con=mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='bdasher1')
	cursor=con.cursor()
	cursor.execute("select * from clientes where idclientes = %s;",(idCli,))
	t=cursor.fetchone()
	n=t[1] #nombre
	a=t[2] #apellido
	sqlDate="INSERT INTO pagos(idpagos,fecha_compra,monto,fecha_pago,nombre,apellido) VALUES (%s,%s,%s,%s,%s,%s)" #inserta en la tabla pagos los datos.
	cursor.execute(sqlDate,(0,dateListaFecha,montoTotal,fechaCambiada,n,a))		
	con.commit() #guarda cambios en la base de datos.

#---- Esta funcion crea un archivo Pagos.txt con todos los datos de la tabla pagos. (sirve de backup)
def backupTablaPagos():
	con=mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='bdasher1')
	cursor=con.cursor()
	cursor.execute("select * from pagos")
	
	tup = cursor.fetchone()
	aux=True	
	

	# creamos el fichero excel
	wb = xlwt.Workbook()
			 
	# añadimos hoja
	ws = wb.add_sheet('Datos de pagos')
			 
	# escribimos encabezados
	ws.write(0,0,'Fecha de compra')
	ws.write(0,1,'Monto')
	ws.write(0,2,'Fecha de pago')
	ws.write(0,3,'Nombre')
	ws.write(0,4,'Apellido')


	i=2
	while (aux and tup!=None):  #este while recorre la tabla pagos y va escribiendo los datos en el archivo Pagos.txt
		
		fechaCompra=str(tup[1]) 
		#file.write(ordenarFechaParaCliente(fechaCompra) + "       ")
		monto=str(tup[2])
		#file.write(monto + "   ")
		fechaPago=str(tup[3])
		#file.write(ordenarFechaParaCliente(fechaPago) + "    ")
		nombre=str(tup[4])
		#file.write(nombre + "    ")
		apellido=str(tup[5])
		#file.write(apellido + "     "+'\n')		
		
		ws.write(i,0,ordenarFechaParaCliente(fechaCompra))
		ws.write(i,1,monto)
		ws.write(i,2,ordenarFechaParaCliente(fechaPago))
		ws.write(i,3,nombre)
		ws.write(i,4,apellido)


		tup=cursor.fetchone()		
		aux=tup
		i=i+1


	cursor.close()
	wb.save('C:/programas_phyton/compras/Pagos.xls')


def backupTablaClientes():
	con=mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='bdasher1')
	cursor=con.cursor()
	cursor.execute("select * from clientes ORDER BY nombre ASC")
	
	tup = cursor.fetchone()
	aux=True	
	

	# creamos el fichero excel
	wb = xlwt.Workbook()
			 
	# añadimos hoja
	ws = wb.add_sheet('Datos de clientes')
			 
	# escribimos encabezados
	ws.write(0,0,'Nombre')
	ws.write(0,1,'Apellido')
	ws.write(0,2,'Telefono')


	i=2
	while (aux and tup!=None):  #este while recorre la tabla clientes y va escribiendo los datos en el archivo Clientes.txt
				
		ws.write(i,0,tup[1])
		ws.write(i,1,tup[2])
		ws.write(i,2,tup[3])
	


		tup=cursor.fetchone()		
		aux=tup
		i=i+1

	wb.save('C:/programas_phyton/compras/clientes.xls')


	cursor.close()



def comprobarExistenciaCampo(nombre):
	con=mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='bdasher1')
	cursor=con.cursor()
	cursor.execute("SHOW COLUMNS FROM ingredientes") # selecciona las columnas de la tabla ingredientes.
	aux=False
	tup=cursor.fetchone()
	while(aux==False and tup): # Este while comprueba si existe el campo con el nombre "nombre".
		if (tup[0]==nombre):
			aux=True
		tup=cursor.fetchone()
	return aux   # Devuelve True si el campo con ese nombre existe y False si no existe.

# verifica si un nombre tiene espacios.
def verificarEspacios(nombre):
	return nombre.count(" ")






# Carga un ingrediente nuevo en la tabla ingredientes_existentes.
def cargarIngredienteNuevo(nombre,entry):
	con=mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='bdasher1')
	cursor=con.cursor()
	#Las siguientes 2 lineas son para comprobar que no exista ya un registro con ese nombre de ingrediente.
	cursor.execute("select * from ingredientes_existentes where nombre=%s;",(nombre,)) 
	tup=cursor.fetchone() 
	if (tup == None):
		sql2="INSERT INTO ingredientes_existentes(idingredientes_existentes,nombre) VALUES (%s,%s)" # Inserta en la tabla ingredientes los datos.
		cursor.execute(sql2,(0,nombre))
		con.commit()
		entry.delete(0,END)
		cursor.close()
	else:
		messagebox.showerror("Error!!!","ERROR!!!, El ingrediente ya existe.")
	






def cargarRecetaNueva(nombre):
	con=mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='bdasher1')
	cursor=con.cursor()
	sql="INSERT INTO recetas(idrecetas,nombre) VALUES (%s,%s)" # Inserta en la tabla ingredientes los datos.
	cursor.execute(sql,(0,nombre))
	con.commit()
	cursor.close()


#borra una receta por el nombre.
def borrarReceta(lst):
	con=mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='bdasher1')
	cursor=con.cursor()
	item=lst.curselection()  #selecciona el lugar en el listbox lst
	if (len(item)==0):
			messagebox.showerror("Error!!!","ERROR!!!, debe seleccionar una receta.")
	else:
		nombre=lst.get(item)	 #obtiene el elemento del lst
		cursor.execute("DELETE FROM recetas WHERE nombre=%s;",(nombre,)) #borra de tabla
		con.commit()  #guarda en base de datos
		cursor.close() #cierra conexion
		actualizarTablaRecetas(lst)  #actualiza el listbox pasado por parametro con las recetas de la tabla recetas.


#borra un ingrediente por el nombre.
#se le pone como parametro un listbox, del cual se obtendra el nombre del ingrediente a borrar.
#el ingrediente se borrara de la tabla ingredientes_existentes.
def borrarIngrediente(lst):
	con=mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='bdasher1')
	cursor=con.cursor()
	item=lst.curselection()  #selecciona el lugar en el listbox lst
	if (len(item)==0):
		messagebox.showerror("Error!!!","ERROR!!!, debe seleccionar un ingrediente.")
	else:
		nombre=lst.get(item)	 #obtiene el elemento del lst
		cursor.execute("DELETE FROM ingredientes_existentes WHERE nombre=%s;",(nombre,)) #borra de tabla
		con.commit()  #guarda en base de datos
		cursor.close() #cierra conexion
		actualizarTablaIngredientes(lst)  #actualiza el listbox pasado por parametro con las recetas de la tabla recetas.
	

# Imprime en el listBox Lis todos los elementos de la tabla ingredientes.
def actualizarTablaIngredientes(lis):
	con=mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='bdasher1')
	cursor=con.cursor()
	cursor = con.cursor(buffered=True)
	lis.delete(0, END)  # Deja el listBox pasado por parametro vacio.
	cursor.execute("select * from ingredientes_existentes ORDER by nombre")	
	tupIngredientes = cursor.fetchone()
	# Este while es para imprimir en el listBox Lis todos los elementos de la tabla ingredientes.
	while tupIngredientes != None:
		s=str(tupIngredientes[1])
		lis.insert(END,s)
		tupIngredientes=cursor.fetchone()
	cursor.close()

# Imprime en el listBox Lis todos los elementos de la tabla recetas.	
def actualizarTablaRecetas(lis):
	con=mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='bdasher1')
	cursor=con.cursor()
	cursor = con.cursor(buffered=True)
	lis.delete(0, END)  # Deja el listBox pasado por parametro vacio.
	cursor.execute("select * from recetas ORDER by nombre")	
	tupRecetas = cursor.fetchone()
	# Este while es para imprimir en el listBox Lis todos los elementos de la tabla recetas.
	while tupRecetas != None:
		s=str(tupRecetas[1])
		lis.insert(END,s)
		tupRecetas=cursor.fetchone()
	cursor.close()





# Este metodo devuelve el idrecetas de la receta pasada por parametro.
def obtenerIdReceta(n):
	con=mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='bdasher1')
	cursor=con.cursor()
	cursor.execute("select * from recetas where nombre = %s;",(n,))
	tup=cursor.fetchone()
	idcli=tup[0]
	return idcli



#Carga un nuevo ingrediente con sus respectivos datos, en la tabla ingredientes. 
def cargarIngredienteEnReceta(nombre,cant,idRecetas,e1,e2):
	con=mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='bdasher1')
	cursor=con.cursor()
	sql2="INSERT INTO ingredientes(idingredientes,nombre,cantidad,recetas_idrecetas) VALUES (%s,%s,%s,%s)" # Inserta en la tabla ingredientes los datos.
	cursor.execute(sql2,(0,nombre,cant,idRecetas))
	con.commit()
	cursor.close()
	e1.delete(0, END)  #Entry para el nombre de receta
	e2.delete(0, END)  #Entry para la cantidad de porciones



#Devuelve el numero de registros que tiene la tabla cantidades.
def obtenerIdCantidad():
	con=mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='bdasher1')
	cursor=con.cursor()
	cursor.execute("select count(*) from cantidades")
	iii = cursor.fetchone()
	return(iii[0])
	cursor.close()

#vacía la tabla compras y pone el idcompras en 0.
def borrarTablaCompras():
	con=mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='bdasher1')
	cursor=con.cursor()
	cursor.execute("delete from compras where idcompras>=0")
	cursor.execute("ALTER TABLE compras AUTO_INCREMENT = 0")	
	con.commit()
	cursor.close()



#vacía la tabla compras y pone el idcompras en 0.
def borrarTablaCompras_final():
	con=mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='bdasher1')
	cursor=con.cursor()
	cursor.execute("delete from compras_final where idcompras_final>=0")
	cursor.execute("ALTER TABLE compras_final AUTO_INCREMENT = 0")	
	con.commit()
	cursor.close()



def crearArchivoCompras():
	con=mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='bdasher1')
	cursor=con.cursor()

	#cursor.execute("select * from compras_final")
	cursor.execute("SELECT ingrediente, sum(cantidad) as cantidad FROM compras_final group by ingrediente")

	tup = cursor.fetchone()
	aux=True	
	
	file = open("C:/programas_phyton/compras/compras.txt", "w")  #Crea el archivo compras.txt



	while (aux and tup!=None):  #este while...
		 
		file.write(tup[0] + "       ----------->     ")
		
		file.write(str(tup[1]))
		file.write('\n')
		tup=cursor.fetchone()		
		aux=tup	
	cursor.close()



#----------------- Crea backup de las deudas de los clientes y genera un archivo en compras. (sirve de backup)
def backupDeudasClientes():
	con=mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='bdasher1')
	cursor=con.cursor()
	cursor.execute("select * from clientes inner join deuda on clientes.idclientes=deuda.idclientes ORDER BY fecha ASC")
	tupDetallesGeneral = cursor.fetchone()
	auxDetalleGeneral=True	
	


	# creamos el fichero excel
	wb = xlwt.Workbook()
		 
	# añadimos hoja
	ws = wb.add_sheet('Datos deuda')
		 
	# escribimos encabezados
	ws.write(0,0,'Nombre')
	ws.write(0,1,'Apellido')
	ws.write(0,2,'Fecha')
	ws.write(0,3,'Monto')
	ws.write(0,4,'Detalle')


	ws.write(0,6,'(Deuda actual)')

	i=2 #indice contador de filas (lo inicializo en 2 para que deje una fila en blanco)
	
	while (auxDetalleGeneral and tupDetallesGeneral!=None): #la condicion tupListarDetallesGeneral!=None la pongo por si no tiene deuda. para que no de error.
		DetalleClientesNombre=str(tupDetallesGeneral[1]) #lo convierto a string porque sino no me deja mostrarlo en el listbox
		DetalleClientesApellido=str(tupDetallesGeneral[2])
		DetalleClientesFecha=str(tupDetallesGeneral[5])
		DetalleClientesFechaOrdenada=ordenarFechaParaCliente(DetalleClientesFecha)
		DetalleClientesMonto=str(tupDetallesGeneral[7])
		DetalleClientesDetalle=str(tupDetallesGeneral[8])
		
		#Va escribiendo los datos en el excel (la i representa las filas y los numeros las columnas)
		ws.write(i,0,DetalleClientesNombre)
		ws.write(i,1,DetalleClientesApellido)
		ws.write(i,2,DetalleClientesFechaOrdenada)
		ws.write(i,3,"$ "+DetalleClientesMonto)
		ws.write(i,4,DetalleClientesDetalle)
		
		i=i+1 #Suma 1 en cada vuelta para que no halla un bucle infinito 

		tupDetallesGeneral=cursor.fetchone()		
		auxDetalleGeneral=tupDetallesGeneral
	
	cursor.close()
	#Guardamos el excel
	wb.save('C:/programas_phyton/compras/deudas.xls')