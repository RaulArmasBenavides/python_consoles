from tkinter import *
import tkinter as tk
import mysql.connector
from tkinter import messagebox
import metodos
from metodos import *
from datetime import datetime, date, time, timedelta
from tkinter import font
import os

#Probar el programa un tiempo. si no da errores borrar todas las conecciones comentadas.
#Solo dejar la primera la de la linea 20.



ventana=Tk()
ventana.title("Asher Aimá 1.0")
#----------------Ancho x Alto - Horizontal + Vertical
ventana.geometry('900x500+400+100')
ventana.configure(background='#008D34')


con=mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='bdasher1')

Helvfont = font.Font(family="Helvetica", size=12, weight="bold") #
HelvfontBoton = font.Font(family="Helvetica", size=10, weight="bold") #Fuente para botones
HelvfontLabel = font.Font(family="Helvetica", size=10, weight="bold") #Fuente para labels
HelvfontBoton14 = font.Font(family="Helvetica", size=14, weight="bold")
#--------VENTANAS----------

def abrirVentanaCompras():
	ventanaCompras=tk.Toplevel()
	#----------------Ancho x Alto - Horizontal + Vertical
	ventanaCompras.geometry('900x400+150+130')
	ventanaCompras.configure(background='#008D34')
	ventanaCompras.title("ventana compras")
	borrarTablaCompras() #Vacia la tabla compras.
	#Aca empiesa a generar la ventana desde donde se incorporaran las recetas.
	frmCompras = Frame(ventanaCompras,bg='#008D34') # Frame para el listbox
	frmCompras.grid(row=1,column=0,padx=5,pady=5,rowspan=3)
	# creo un scrollbar y lo coloco en el frame frmCompras
	scrollbarCompras=Scrollbar(frmCompras) 
	scrollbarCompras.pack(side=RIGHT,fill=Y)
	# creo un listbox y lo pongo en el frame frmCompras
	#-----------------------------Ancho x Alto 
	lstCompras=Listbox(frmCompras,bg='#000000',fg='#ffffff',width=45,height=20,selectmode=BROWSE,yscrollcommand=scrollbarCompras.set)
	lstCompras.pack(side=LEFT,fill=BOTH)
	# le asigno el scrollbar a el listbox lstDeuda
	scrollbarCompras.config(command=lstCompras.yview)
	
	actualizarTablaRecetas(lstCompras) #carga en lstCompras los ingredientes de bdasher1.

	
	a1= tk.StringVar() # Variable asociada a txtRecetas (nombre la receta)
	a2= tk.IntVar() # Variable asociada a txtCantidad    (cantidad de unidades de receta)
	frm2 = Frame(ventanaCompras,background='#008D34')  # Frame para los Entry y botones.
	frm2.grid(row=0,column=1,padx=5,pady=5,rowspan=3)
	
	lblReceta= Label(frm2,text="Receta",font=Helvfont,bg='#008D34')
	lblReceta.grid(row=0,column=0,padx=5,pady=5)
	lblCantidad= Label(frm2,text="Porciones",font=Helvfont,bg='#008D34')
	lblCantidad.grid(row=0,column=1,padx=5,pady=5)
	txtReceta=Entry(frm2,textvariable=a1)
	txtReceta.grid(row=1,column=0,padx=5,pady=5, sticky=tk.W)
	txtCantidad=Entry(frm2,textvariable=a2)
	txtCantidad.grid(row=1,column=1, padx=5,pady=5, sticky=tk.W)
	lstCompras.focus() # Pone el foco en txtReceta.



	#La funcion pasar() escribe en el Entry txtReceta el elemento seleccionado del listbox lstCompras.
	def pasarR():
		item=lstCompras.curselection()
		txtReceta.delete(0, END)
		if (len(item)==0):
			messagebox.showerror("Error!!!","ERROR!!!, debe seleccionar una receta.")
		else:
			txtReceta.insert(0,lstCompras.get(item))
			txtCantidad.delete(0, END)
			txtCantidad.focus()
	
	#Esta funcion agrega en la base de datos, tabla compras, la lista de compras que luego...
	#	se imprimira en el archivo C:/programas_phyton/compras/lista_compras.txt.
	def agregarPorciones():
		cursor=con.cursor()
		sql="INSERT INTO compras(idcompras,nombre_receta,cantidad_porciones) VALUES (%s,%s,%s)" # Inserta en la tabla compras los datos.
		nombre=a1.get()
		cant=a2.get()
		cursor.execute(sql,(0,nombre,cant))
		con.commit()  #guarda en base de datos
		cursor.close() #cierra conexion
		txtReceta.delete(0, END)
		txtCantidad.delete(0, END)
		lstCompras.focus() # Pone el foco en txtReceta.



 	#### seguirrrrrr acaaaaaa q no andaaa del todo
	def calcularIng():
		borrarTablaCompras_final()
		# 000 Anda joya. inserta las recetas en lisNom y las cantidades en lisCant
		# saca los valores de la tabla compras.
		cursor=con.cursor()
		cursor.execute("select * from compras")
		tup=cursor.fetchone()
		lisNom=[] # lista para recetas
		lisCant=[] # lista para cantidades de recetas (porciones)
		while(tup != None):
			lisNom.append(tup[1])
			lisCant.append(tup[2])
			tup=cursor.fetchone()
		### 000

		aux1=0

		for i in lisNom: # desde 1 hasta la cantidad de recetas.
			nom=lisNom[aux1]
			cant=lisCant[aux1]
			
			cursor=con.cursor()

			cursor.execute("select * from recetas where nombre = %s;",(nom,)) # lista de recetas con nombre nom.
			tup2=cursor.fetchone()
			idR=tup2[0] # idrecetas de la tabla recetas de la receta nom.
			cursor.execute("select * from ingredientes where recetas_idrecetas = %s;",(idR,)) # ingredientes para la receta nom.
			lisIngredientes=[] # lista para los ingredientes (nombres).
			lisCantidades=[] # lista para las cantidades de cada ingrediente.
			

			tup3=cursor.fetchone()
			while(tup3!=None):
				lisIngredientes.append(tup3[1])
				lisCantidades.append(tup3[2])
				tup3=cursor.fetchone()
			
			aux2=0
			
			for j in lisIngredientes:
				sql="INSERT INTO compras_final(idcompras_final,ingrediente,cantidad) VALUES (%s,%s,%s)"
				cursor.execute(sql,(0,lisIngredientes[aux2],cant * lisCantidades[aux2]))
				
				aux2=aux2+1
			
			con.commit()
			aux1=aux1 +1

		con.commit()
		cursor.close()
		crearArchivoCompras() 





	botonPasarR=Button(frm2,bg="#D3FFE3",activeforeground="#ffffff",activebackground="#40C16F",text="/  >>>  >",font=HelvfontBoton,command=pasarR)
	botonPasarR.grid(row=2,column=0, padx=5,pady=5, sticky=tk.W)

	botonSiguiente=Button(frm2,bg="#D3FFE3",activeforeground="#ffffff",activebackground="#40C16F",text="Siguiente . . .",font=HelvfontBoton, command=agregarPorciones)
	botonSiguiente.grid(row=1,column=2, padx=5,pady=5, sticky=tk.W)

	botonCrearArchivo=Button(frm2,bg="#D3FFE3",activeforeground="#ffffff",activebackground="#40C16F",text="Crear Lista de Compras",font=HelvfontBoton, command=calcularIng)
	botonCrearArchivo.grid(row=1,column=3, padx=5,pady=5, sticky=tk.W)







def abrirVentanaNuevaReceta():
	ventanaNuevaReceta=tk.Toplevel()
	ventanaNuevaReceta.title("Recetas nueva")
	#----------------Ancho x Alto - Horizontal + Vertical
	ventanaNuevaReceta.geometry('500x300+150+130')
	ventanaNuevaReceta.configure(background='#008D34')

	a = tk.StringVar() # Nombre de la receta.


	lblNombre= Label(ventanaNuevaReceta,text="Nombre de Receta",font=Helvfont,bg='#008D34')
	lblNombre.grid(row=0,column=0,padx=5,pady=5)
	txtNombre=Entry(ventanaNuevaReceta,textvariable=a)
	txtNombre.grid(row=0,column=1,padx=5,pady=5, sticky=tk.W)

	#--- Esta funcion agrega a la base de datos la receta especificada. 
	def onEnterAgregarReceta(event):  
   		abrirVentanaRecetas(a.get(),ventanaNuevaReceta)
    
	#--- Aca se asocia el evento Return al Entry txtNombre
	#    	para que al dar enter ejecute la funcion onEnterAgregarReceta
	txtNombre.bind('<Return>', onEnterAgregarReceta)

	txtNombre.focus()

	botonAgregar=Button(ventanaNuevaReceta,bg="#D3FFE3",activeforeground="#ffffff",activebackground="#40C16F",text="   Ok  !!! ",font=HelvfontBoton,command = lambda: abrirVentanaRecetas(a.get(),ventanaNuevaReceta))
	botonAgregar.grid(row=0,column=2, padx=5,pady=5, sticky=tk.W)


def abrirVentanaBorraReceta():
	ventanaBorrarReceta=tk.Toplevel()
	ventanaBorrarReceta.title("Borrar Recetas")
	#--------------Ancho x Alto - Horizontal + Vertical
	ventanaBorrarReceta.geometry('800x400+150+130')
	ventanaBorrarReceta.configure(background='#008D34')


	frmRecetas = Frame(ventanaBorrarReceta,bg='#008D34') # Frame para el listbox
	frmRecetas.grid(row=1,column=0,padx=5,pady=5,rowspan=3)
	
	scrollbarRecetas=Scrollbar(frmRecetas) 
	scrollbarRecetas.pack(side=RIGHT,fill=Y)
	#	#-----------------------------Ancho x Alto 
	lstRecetas=Listbox(frmRecetas,bg='#000000',fg='#ffffff',width=45,height=20,selectmode=BROWSE,yscrollcommand=scrollbarRecetas.set)
	lstRecetas.pack(side=LEFT,fill=BOTH)
	
	scrollbarRecetas.config(command=lstRecetas.yview)
	
	actualizarTablaRecetas(lstRecetas) #carga en lstRecetas las recetas de bdasher1.
	
	

	
	frm2 = Frame(ventanaBorrarReceta,background='#008D34')  # Frame para el boton.
	frm2.grid(row=0,column=1,padx=5,pady=5,rowspan=3)
	
	#--- Esta funcion agrega a la base de datos la receta especificada. 
	def onEnterBorrarReceta(event):  
   		borrarReceta(lstRecetas)
    
	#--- Aca se asocia el evento Return al listbox lstRecetas
	#    	para que al dar enter ejecute la funcion onEnterBorrarReceta
	lstRecetas.bind('<Return>', onEnterBorrarReceta)



	botonBorrar=Button(frm2,bg="#D3FFE3",activeforeground="#ffffff",activebackground="#40C16F",text="- BORRAR -",font=HelvfontBoton,command = lambda: borrarReceta(lstRecetas))
	botonBorrar.grid(row=0,column=0,padx=5,pady=5)
	
	lstRecetas.focus() # Pone el foco en txtReceta.



#---------------esta funcion crea y abre la subventana ventanaRecetas
def abrirVentanaRecetas(nom,ventana):   # El parametro (a) es el nombre de la receta nueva.
	
	ventana.destroy() #cierra la ventana pasada como parametro antes de crear la ventana ventanaRecetas.
	ventanaRecetas=tk.Toplevel()
	ventanaRecetas.title("/ Recetas /")
	#--------------Ancho x Alto - Horizontal + Vertical
	ventanaRecetas.geometry('800x400+150+130')
	ventanaRecetas.configure(background='#008D34')

	cargarRecetaNueva(nom)#carga una receta nueva con ese nombra. para luego agregarle los ingredientes correspondientes.
	idReceta = obtenerIdReceta(nom)

	#Aca empiesa a generar la ventana desde donde se incorporaran los respectivos ingredientes de la nueva receta.
	frmIngredientes = Frame(ventanaRecetas,bg='#008D34') # Frame para el listbox
	frmIngredientes.grid(row=1,column=0,padx=5,pady=5,rowspan=3)
	# creo un scrollbar y lo coloco en el frame frmDeuda
	scrollbarIngredientes=Scrollbar(frmIngredientes) 
	scrollbarIngredientes.pack(side=RIGHT,fill=Y)
	# creo un listbox y lo pongo en el frame frmDeuda
	#-----------------------------Ancho x Alto 
	lstIngredientes=Listbox(frmIngredientes,bg='#000000',fg='#ffffff',width=45,height=20,selectmode=BROWSE,yscrollcommand=scrollbarIngredientes.set)
	lstIngredientes.pack(side=LEFT,fill=BOTH)
	# le asigno el scrollbar a el listbox lstDeuda
	scrollbarIngredientes.config(command=lstIngredientes.yview)
	
	actualizarTablaIngredientes(lstIngredientes) #carga en lstIngredientes los ingredientes de bdasher1.

	
	a1= tk.StringVar() # Variable asociada a txtIngrediente (nombre del ingrediente)
	a2= tk.DoubleVar() # Variable asociada a txtCantidad    (cantidad de ingrediente)
	frm2 = Frame(ventanaRecetas,background='#008D34')  # Frame para los Entry y botones.
	frm2.grid(row=0,column=1,padx=5,pady=5,rowspan=3)
	
	lblIngrediente= Label(frm2,text="Ingrediente",font=Helvfont,bg='#008D34')
	lblIngrediente.grid(row=0,column=0,padx=5,pady=5)
	lblCantidad= Label(frm2,text="Cantidad",font=Helvfont,bg='#008D34')
	lblCantidad.grid(row=0,column=1,padx=5,pady=5)
	txtIngrediente=Entry(frm2,textvariable=a1)
	txtIngrediente.grid(row=1,column=0,padx=5,pady=5, sticky=tk.W)
	txtCantidad=Entry(frm2,textvariable=a2)
	txtCantidad.grid(row=1,column=1, padx=5,pady=5, sticky=tk.W)
	lstIngredientes.focus() # Pone el foco en lstIngredientes.
	txtCantidad.delete(0, END)



	#La funcion pasar() escribe en el Entry txtIngrediente el elemento seleccionado del listbox lstIngredientes.
	def pasarI():
		item=lstIngredientes.curselection()
		txtIngrediente.delete(0, END)
		if (len(item)==0):
			messagebox.showerror("Error!!!","ERROR!!!, debe seleccionar un ingrediente.")
		else:
			txtIngrediente.insert(0,lstIngredientes.get(item))
			txtCantidad.delete(0, END)
			txtCantidad.focus()
	

	def terminar():
		ventanaRecetas.destroy()  #destroy() es para cerrar la ventana (ventanaRecetas)
		

	# estos tres botones son de la ventanaRecetas
	

	botonAgregar=Button(frm2,bg="#D3FFE3",activeforeground="#ffffff",activebackground="#40C16F",text="Siguiente *",font=HelvfontBoton,command = lambda: cargarIngredienteEnReceta(a1.get(),a2.get(),idReceta,txtIngrediente,txtCantidad))
	botonAgregar.grid(row=1,column=2, padx=5,pady=5, sticky=tk.W)

	botonPasar=Button(frm2,bg="#D3FFE3",activeforeground="#ffffff",activebackground="#40C16F",text="> > > > >",font=HelvfontBoton,command=pasarI)
	botonPasar.grid(row=2,column=0, padx=5,pady=5, sticky=tk.W)
	
	lblExplicacion= Label(frm2,text="Cuando termine de cargar los ingredientes presione Terminar",font=Helvfont,bg='#008D34')
	lblExplicacion.grid(row=5,column=0,padx=5,pady=50,columnspan=4)

	botonTerminar=Button(frm2,width=10,height=2,bg="#D3FFE3",activeforeground="#ffffff",activebackground="#40C16F",text="Terminar",font=HelvfontBoton,command = terminar)
	botonTerminar.grid(row=6,column=0,padx=5,pady=20,rowspan=4,sticky=tk.SW)


#--- 105 Clientes
#--- Esta funcion carga un cliente nuevo.
nombreCliente= tk.StringVar()  #variables asociadas a los Entry de la ventana ventanaNuevoClientes
apellidoCliente = tk.StringVar()
telefonoCliente= tk.DoubleVar()
	
#---Esta funcion crea la ventanaNuevoClientes
def abrirVentanaNuevoClientes():
	ventanaNuevoClientes=tk.Toplevel()
	ventanaNuevoClientes.title("Cliente Nuevo")
	#----------------Ancho x Alto - Horizontal + Vertical
	ventanaNuevoClientes.geometry('250x200+40+100')
	ventanaNuevoClientes.configure(background='#008D34')
	lblNombre= Label(ventanaNuevoClientes,text="Nombre",font=Helvfont,bg='#008D34')
	lblNombre.grid(row=0,column=0,padx=5,pady=5)
	lblApellido= Label(ventanaNuevoClientes,text="Apellido",font=Helvfont,bg='#008D34')
	lblApellido.grid(row=1,column=0,padx=5,pady=5)
	lblTelefono= Label(ventanaNuevoClientes,text="Telefono",font=Helvfont,bg='#008D34')
	lblTelefono.grid(row=2,column=0,padx=5,pady=5)	
	txtNombre = Entry(ventanaNuevoClientes,textvariable=nombreCliente)
	txtNombre.grid(row=0,column=1,padx=5,pady=5)
	txtApellido = Entry(ventanaNuevoClientes,textvariable=apellidoCliente)
	txtApellido.grid(row=1,column=1,padx=5,pady=5)
	txtTelefono = Entry(ventanaNuevoClientes,textvariable=telefonoCliente)
	txtTelefono.grid(row=2,column=1,padx=5,pady=5)
	txtNombre.focus()  #Pone el foco en el Entry txtNombre.

	


	def cargarCliente():
		cursor=con.cursor()
		a2=nombreCliente.get()
		a3=apellidoCliente.get()
		a4=telefonoCliente.get()
		#Esta linea de aca abajo selecciona todos los registros donde el nombre y el apellido coincidan
		#	con a2 y a3. Si llega a haber al menos un registro, quiere decir que el cliente ya existe
		#	y en ese caso no deja cargar. Es para que no halla dos registros con el mismo nombre y apellido.
		cursor.execute("select * from clientes where nombre = %s and apellido = %s;",(a2,a3,))
		existe=cursor.fetchall()
		if len(existe)!=0:
			messagebox.showerror("Error!","El cliente ya existe en la base de datos.")
		else:
			if (a2=="" or a3==""): #Este if es por si el campo nombre o apellido estan vacios.
				messagebox.showerror("Error!","Debe ingresar nombre y apellido")
				if (a2==""):
					txtNombre.focus()
				else:
					txtApellido.focus()
			else:
				try: #esto trata de insertar un nuevo cliente en la base de datos.
					sql= "INSERT INTO clientes (idclientes,nombre,apellido,telefono) VALUES (%s,%s,%s,%s)"
					cursor.execute(sql,(0,a2,a3,a4))
					con.commit()   #-- el commit se usa para guardar los cambios realizados en la base de datos.
					messagebox.showinfo("Cliente Nuevo","Cliente cargado correctamente!!!")
				except mysql.connector.Error as err:
  						print("Something went wrong: {}".format(err))
				cursor.close() #cierra la conexion
				txtNombre.delete(0, END) #estas 3 lineas borran los Entry de la ventana ventanaBuscarClientes.
				txtApellido.delete(0, END)
				txtTelefono.delete(0, END)


	#--- Esta funcion carga un cliente nuevo a la base de datos. 
	def onEnterIngreso(event):  
   		cargarCliente()
    
	#--- Aca se asocia el evento Return a los Entrys txtNombre txtApellido txtTelefono
	#    	para que al dar enter ejecuten la funcion onEnterIngreso
	txtNombre.bind('<Return>', onEnterIngreso)
	txtApellido.bind('<Return>', onEnterIngreso)
	txtTelefono.bind('<Return>', onEnterIngreso)



	botonGuardar=Button(ventanaNuevoClientes,bg="#D3FFE3",activeforeground="#ffffff",activebackground="#40C16F",text="Guardar 5",font=HelvfontBoton,command=cargarCliente)
	botonGuardar.grid(row=3,column=0,padx=5,pady=10)

def abrirVentanaIngredienteNuevo():
	ventanaIngredienteNuevo=tk.Toplevel()
	ventanaIngredienteNuevo.title("Ingrediente Nuevo")
	#----------------Ancho x Alto - Horizontal + Vertical
	ventanaIngredienteNuevo.geometry('250x220+480+130')
	ventanaIngredienteNuevo.configure(background='#008D34')
	nombre = tk.StringVar()
	lblIngrediente=Label(ventanaIngredienteNuevo, text="Ingrediente",background='#008D34',font=Helvfont)
	lblIngrediente.grid(row=0,column=1,padx=5,pady=5)
	
	txtIngresos=Entry(ventanaIngredienteNuevo,textvariable=nombre)
	txtIngresos.grid(row=1,column=1,padx=5,pady=5)
	
	#--- Esta funcion carga un ingrediente nuevo a la base de datos. 
	def onEnterIngreso(event):  
   		cargarIngredienteNuevo(nombre.get(),txtIngresos)
    
	#--- Aca se asocia el evento Return al Entry txtIngresos
	#    	para que al dar enter ejecute la funcion onEnterIngreso
	txtIngresos.bind('<Return>', onEnterIngreso)

	lblExplicacion=Label(ventanaIngredienteNuevo, text="Los ingredientes no pueden llevar espacios!!!",background='#008D34')
	lblExplicacion.grid(row=5,column=0,padx=5,pady=5,columnspan=4)

	txtIngresos.focus()

	btnIngredienteNuevo=Button(ventanaIngredienteNuevo,bg="#D3FFE3",activeforeground="#ffffff",activebackground="#40C16F",text="           OK   -          ",font=HelvfontBoton,command = lambda: cargarIngredienteNuevo(nombre.get(),txtIngresos))
	btnIngredienteNuevo.grid(row=3,column=1,padx=5,pady=5)

def abrirVentanaBorrarIngrediente():
	ventanaBorrarIngrediente=tk.Toplevel()
	ventanaBorrarIngrediente.title("Borrar Ingrediente")
	#--------------Ancho x Alto - Horizontal + Vertical
	ventanaBorrarIngrediente.geometry('360x400+150+130')
	ventanaBorrarIngrediente.configure(background='#008D34')


	#Aca empiesa a generar la ventana con el listbox de ingredientes a borrar.
	frmIngredientes = Frame(ventanaBorrarIngrediente,bg='#008D34') # Frame para el listbox
	frmIngredientes.grid(row=1,column=0,padx=5,pady=5)
	# creo un scrollbar y lo coloco en el frame frmDeuda
	scrollbarIngredientes=Scrollbar(frmIngredientes) 
	scrollbarIngredientes.pack(side=RIGHT,fill=Y)
	# creo un listbox y lo pongo en el frame frmDeuda
	#-----------------------------Ancho x Alto 
	lstIngredientes=Listbox(frmIngredientes,bg='#000000',fg='#ffffff',width=45,height=20,selectmode=BROWSE,yscrollcommand=scrollbarIngredientes.set)
	lstIngredientes.pack(side=LEFT,fill=BOTH)
	# le asigno el scrollbar a el listbox lstDeuda
	scrollbarIngredientes.config(command=lstIngredientes.yview)
	
	actualizarTablaIngredientes(lstIngredientes) #carga en lstIngredientes los ingredientes de bdasher1.

	frmBot = Frame(ventanaBorrarIngrediente,bg='#008D34') # Frame para el listbox
	frmBot.grid(row=2,column=0,padx=5,pady=5,sticky=tk.N)
	
	#--- Esta funcion borra de la base de datos el ingrediente seleccionado en el listbox. 
	def onEnterBorrarIngrediente(event):  
   		borrarIngrediente(lstIngredientes)
    
	#--- Aca se asocia el evento Return al Listbox lstIngredientes
	#    	para que al dar enter ejecute la funcion onEnterBorrarIngrediente
	lstIngredientes.bind('<Return>', onEnterBorrarIngrediente)


	botonBorrarIngrediente=Button(frmBot,bg="#D3FFE3",activeforeground="#ffffff",activebackground="#40C16F",text="/ Borrar Ingrediente /",font=HelvfontBoton,command = lambda: borrarIngrediente(lstIngredientes))
	botonBorrarIngrediente.pack(  padx=10 , pady=10)

	#botonBorrarIngrediente.pack(after=scrollbarIngredientes, side=tk.BOTTOM, padx=10 , pady=10)


	

def abrirVentanaBuscarClientes():	
	ventanaBuscarClientes=tk.Toplevel()
	ventanaBuscarClientes.title("Buscar Cliente")
	#----------------Ancho x Alto - Horizontal + Vertical
	ventanaBuscarClientes.geometry('250x200+40+100')
	ventanaBuscarClientes.configure(background='#008D34')
	
	nombreBuscarCliente = tk.StringVar()
	apellidoBuscarCliente = tk.StringVar()
	lblNombreBuscar= Label(ventanaBuscarClientes,text="Nombre",font=Helvfont,bg='#008D34')
	lblNombreBuscar.grid(row=0,column=0,padx=5,pady=5)
	lblApellidoBuscar= Label(ventanaBuscarClientes,text="Apellido",font=Helvfont,bg='#008D34')
	lblApellidoBuscar.grid(row=1,column=0,padx=5,pady=5)
	txtNombreBuscar = Entry(ventanaBuscarClientes,textvariable=nombreBuscarCliente)
	txtNombreBuscar.grid(row=0,column=1,padx=5,pady=5)
	txtApellidoBuscar = Entry(ventanaBuscarClientes,textvariable=apellidoBuscarCliente)
	txtApellidoBuscar.grid(row=1,column=1,padx=5,pady=5)
	txtNombreBuscar.focus()   #pone el foco en el Entry txtNombreBuscar


	#--- buscarCliente busca dentro de la tabla clientes de la base de datos bdasher1
	#--- el registro en el cual coinciden el nombre y apellido tomado de los entry txtNombre y txtApellido.
	def buscarCliente():
		ventanaBuscarClientes.destroy()
		cursor=con.cursor()
		n=nombreBuscarCliente.get()
		a=apellidoBuscarCliente.get()
		
		
		#--- esta linea de abajo ejecuta una consulta mysql para buscar todos los registros de la tabla clientes
		#--- de la base de datos bdasher1 donde el campo nombre sea igual al valor (n) y el apellido igual a (a).
		
		cursor.execute("select * from clientes where nombre = %s and apellido = %s;",(n,a,))
		tup=cursor.fetchall()
		if (len(tup)==0):
			messagebox.showerror("Error","No existe el cliente")
		else: #--- si el cliente exite, crea una ventana nueva y muestra sus atributos.
			ventanaClienteEncontrado=tk.Toplevel()
			ventanaClienteEncontrado.title("Cliente Encontrado")
			#-------------------------------Ancho x Alto
			ventanaClienteEncontrado.geometry('600x260+40+100')
			ventanaClienteEncontrado.configure(background='#008D34')
			
			#--guarda el valor del campo idclientes de la tabla clientes.
			idCli=tup[0][0]

			#-- 55 Todo esto es para poder tener un listbox scrolleable
			#-- creo un frame y lo coloco en la ventanaClienteEncontrado
			
			frmFecha = Frame(ventanaClienteEncontrado)
			frmFecha.grid(row=0,column=2,padx=1,pady=5,rowspan=6)

			frmMonto = Frame(ventanaClienteEncontrado)
			frmMonto.grid(row=0,column=3,padx=1,pady=5,rowspan=6)
			
			# creo un scrollbar y lo coloco en el frame frmMonto
			scrollbarDeuda=Scrollbar(frmMonto) 
			scrollbarDeuda.pack(side=RIGHT,fill=Y)
			
			#Esta funcion es para sincronizar los listbox en su seleccion
			def seleccion(event):   #El parametro event no se para que sirve pero ni no esta da error.			
				#copia el elemento seleccionado en lstMontoDetalle en itemABorrar
				itemABorrar = lstMontoDetalle.curselection() 
				#Si habia elemento seleccionado en lstMontoDetalle entonces este if se cumple y desselecciona
				if (len(itemABorrar)!=0):
					lstMontoDetalle.selection_clear(itemABorrar)
				item = lstFechaDetalle.curselection()		
				lstMontoDetalle.select_set(item)

			# creo los listbox y los pongo en los frame 
			lstFechaDetalle=Listbox(frmFecha,exportselection=False,bg='#000000',fg='#ffffff',width=25,height=14,selectmode=BROWSE,yscrollcommand=scrollbarDeuda.set)
			lstFechaDetalle.pack(side=LEFT,fill=BOTH)
			#Asocio el evento ListboxSelect (elemento seleccionado) con la funcion seleccion en lstFechaDetalle
			lstFechaDetalle.bind('<<ListboxSelect>>',seleccion)


			lstMontoDetalle=Listbox(frmMonto,exportselection=False,bg='#000000',fg='#ffffff',width=25,height=14,selectmode=BROWSE,yscrollcommand=scrollbarDeuda.set)
			lstMontoDetalle.pack(side=LEFT,fill=BOTH)

			# le asigno el scrollbar a los listbox
			exportselection=False
			# Conecto los cinco listbox con la acción yview 
			def yview(*args):
				lstFecha.yview(*args)
				lstMonto.yview(*args)


			# le asigno el scrollbar a el listbox lstDeuda
			scrollbarDeuda.config(command=yview)
			
			
			


			# ingreso de datos, aca ingresar los datos de la base de datos para el cliente en cuestion.
			
			
			indice=tup[0][0] #toma el valor del campo idclientes de la tabla clientes
			#busca en la tabla deuda todos los registros que tengan en el campo idclientes de la tabla deuda
			#el mismo valor que indice.
			cursor.execute("select * from deuda where idclientes = %s ;",(indice,))
			
		
			#-99- este while lo que hace es insertar en la lista lstDeuda los campos fecha y monto asociados al cliente.
			tupDeuda = cursor.fetchone()
			aux=True
			
			
			while (aux and tupDeuda!=None): #la condicion tupDeuda!=None la pongo por si no tiene deuda. para que no de error.
				fecha=str(tupDeuda[1]) #lo convierto a string porque sino no me deja mostrarlo en el listbox
				monto=str(tupDeuda[3])

				f=metodos.ordenarFechaParaCliente(fecha)

			
				lstFechaDetalle.insert(END,f)
				lstMontoDetalle.insert(END,monto)

				tupDeuda=cursor.fetchone()		
				aux=tupDeuda
			#-99-	
			frameCliEncontrado = Frame(ventanaClienteEncontrado,bg='#008D34')
			frameCliEncontrado.grid(row=0,column=0,padx=5,pady=5,sticky=tk.N)

			#Frame para los botones de la ventana ventanaClienteEncontrado
			frameCliEncontradoB = Frame(ventanaClienteEncontrado,bg='#008D34')
			frameCliEncontradoB.grid(row=1,column=0,padx=5,pady=5,sticky=tk.N)


			# Estas dos tuplas las cree para que los datos encontrados en la base de datos en la tabla clientes
			# 	que estan en la tupla creada por fetchone puedan ser mostradas en los respectivos campos de texto.
			nn=tup[0][1]
			aa=tup[0][2]
			tt=tup[0][3]		


			dd=calcularDeuda(indice) #calcula deuda total del cliente con idclientes=indice


			#lblDeudaEncontrado= Label(frmDeuda,text="Deuda",bg='#008D34')
			#lblDeudaEncontrado.grid(row=0,column=0)
			lblNombreEncontrado= Label(frameCliEncontrado,text="Nombre",bg='#008D34', font=HelvfontLabel)
			lblNombreEncontrado.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
			lblApellidoEncontrado= Label(frameCliEncontrado,text="Apellido",bg='#008D34', font=HelvfontLabel)
			lblApellidoEncontrado.grid(row=1,column=0,padx=5,pady=5,sticky=tk.W)
			lblTelefonoEncontrado= Label(frameCliEncontrado,text="Telefono",bg='#008D34', font=HelvfontLabel)
			lblTelefonoEncontrado.grid(row=2,column=0,padx=5,pady=5,sticky=tk.W)
			lblDeudaTotalEncontrado= Label(frameCliEncontrado,text="Deuda Total",bg='#008D34', font=HelvfontLabel)
			lblDeudaTotalEncontrado.grid(row=3,column=0,padx=5,pady=5,sticky=tk.W)			
			txtNombreEncontrado = Entry(frameCliEncontrado,textvariable=nn, font=HelvfontLabel)
			txtNombreEncontrado.grid(row=0,column=1,padx=5,pady=5)
			txtApellidoEncontrado = Entry(frameCliEncontrado,textvariable=aa, font=HelvfontLabel)
			txtApellidoEncontrado.grid(row=1,column=1,padx=5,pady=5)
			txtTelefonoEncontrado = Entry(frameCliEncontrado,textvariable=tt, font=HelvfontLabel)
			txtTelefonoEncontrado.grid(row=2,column=1,padx=5,pady=5)
			txtDeudaTotalEncontrado = Entry(frameCliEncontrado,textvariable=dd, font=HelvfontLabel)
			txtDeudaTotalEncontrado.grid(row=3,column=1,padx=5,pady=5)
			
			#Estas cuatro lineas de abajo muestran en los campos de texto la informacion sacada de la tabla clientes.
			txtNombreEncontrado.insert(0,nn)
			txtApellidoEncontrado.insert(0,aa)
			txtTelefonoEncontrado.insert(0,tt)
			txtDeudaTotalEncontrado.insert(0,dd)
			


			#-- borra el dato seleccionado del listbox y de la base de datos bdasher1 de la tabla deuda
			def borrarDatos():
				cursor=con.cursor()
				
				
				
				# curselection() da una tupla con la posicion del elemento en el listbox
				pos=lstMontoDetalle.curselection()
				
				
				# get(pos) obtiene el elemento que esta en la posicion (pos) del listbox
				#elem=lstMontoDetalle.get(pos)
				#print(elem)
				
				

				
				
				#Va todo dentro del if. por si no hay elemento seleccionado del listbox y se presiona el boton pago.
				
				
				if(pos==()):
					messagebox.showerror("Error","Debe seleccionar un elemento!!!")
				else:
					f=lstFechaDetalle.get(pos)
					m=lstMontoDetalle.get(pos)
					

					#String recortado donde solo esta la fecha en tipo string ddmmyyyy (sin el -) es necesario para usar strptime
					strListaFecha2 = f.replace("-", "")
					#Aca esta la fecha pero convertida a formato date
					#	que luego se usara para comparar en la consulta a la base de datos.
					dateListaFecha=datetime.strptime(strListaFecha2, "%d%m%Y").date()
					
					
					
					#Aca ejecuto el metodo guardarPago() para que se guarde el pago en la tabla pagos antes de ser borrada.
					#	le pongo el if por si se cambio la fecha.
					auxBoolean = messagebox.askyesno(message="¿¿¿Cambiar fecha????", title="Opcion")
					if(auxBoolean):
						fechaCambiada = datetime.now()
						#Creo una ventana nueva para que el usuario agregue la fecha nueva.
						ventanaCambiarFecha=tk.Toplevel()
						ventanaCambiarFecha.title("Cambiar fecha de pago")
						ventanaCambiarFecha.geometry('470x420+350+130')
						ventanaCambiarFecha.configure(background='#008D34')	
						fC = tk.StringVar()
						lblFechaCambiada= Label(ventanaCambiarFecha,text="Ingrese Fecha Nueva",bg='#008D34')
						lblFechaCambiada.grid(row=0,column=0,padx=5,pady=5)
						txtFechaCambiada = Entry(ventanaCambiarFecha,textvariable=fC)
						txtFechaCambiada.grid(row=0,column=1,padx=5,pady=5)
						txtFechaCambiada.focus()

						def aceptarFechaNueva():
							fechaCambiada=datetime.strptime(str(fC.get()), "%d%m%Y").date()
							guardarPagoFechaCambiada(idCli,dateListaFecha,m,fechaCambiada)
							txtFechaCambiada.delete(0, END)

						botonOk=Button(ventanaCambiarFecha,bg="#D3FFE3",activeforeground="#ffffff",activebackground="#40C16F",text="*Ok!",font=HelvfontBoton,command=aceptarFechaNueva)
						botonOk.grid(row=1,column=0,padx=5,pady=5,sticky=tk.W)
					else:
						guardarPago(idCli,dateListaFecha,m)
						

					
					# Borra de la tabla deuda los registros que coincidan en esos tres campos. (idclientes,fecha,monto)
					sqlBorrar="delete from deuda where idclientes = %s and fecha= %s and monto=%s;"
					cursor.execute(sqlBorrar,(idCli,dateListaFecha,m,))
					#Esto selecciona elemento del listbox lstDeuda
					datoSelec=lstMontoDetalle.curselection()
					#Este if lo agrego porque si no hay un elemento seleccionado del listbox va a dar error.
					#	ademas el con.commit() lo agrego dentro del if para que guarde los cambios en la base de datos si
					#	no hay ningun error. En caso contrario no se guarda nada. (seria como un tipo de excepcion casera! :))
					if (datoSelec==()):
						messagebox.showerror("Error","Debe seleccionar un elemento!!!")
					else:
						lstMontoDetalle.delete(datoSelec)
						lstFechaDetalle.delete(datoSelec)
						con.commit() #esta linea es para guardar cambios en la base de datos.
					
									

					# estas tres lineas de abajo actualizan el entry de deuda total.
					dd3=calcularDeuda(idCli)
					txtDeudaTotalEncontrado.delete(0, END)
					txtDeudaTotalEncontrado.insert(0,dd3)

					actualizarLstDetallesGeneral2(lstDetallesGeneral,lstDetallesGeneral2,lstDetallesGeneral3,lstDetallesGeneral4,lstDetallesGeneral5) #Actualiza lstDetallesGeneral (metodo de metodos.py)
				
				
			def abrirVentanaDetalles():
				ventanaDetalles=tk.Toplevel()
				ventanaDetalles.title("* Detalles *")
				ventanaDetalles.geometry('600x420+350+130')
				ventanaDetalles.configure(background='#008D34')	

				cursor=con.cursor()
				
				#-- Frames --
				frmNombre = Frame(ventanaDetalles,bg='#008D34')
				frmNombre.grid(row=0,column=0,pady=10)

				frmApellido = Frame(ventanaDetalles,bg='#008D34')
				frmApellido.grid(row=0,column=1,pady=10)

				frmFecha = Frame(ventanaDetalles,bg='#008D34')
				frmFecha.grid(row=0,column=2,pady=10)

				frmMonto = Frame(ventanaDetalles,bg='#008D34')
				frmMonto.grid(row=0,column=3,pady=10)

				frmReceta = Frame(ventanaDetalles,bg='#008D34')
				frmReceta.grid(row=0,column=4,pady=10)




				# --- Labels ---
				lblNombre=Label(frmNombre, text="Nombre",background='#008D34',font=Helvfont)
				lblNombre.pack(side=TOP)

				lblApellido=Label(frmApellido, text="Apellido",background='#008D34',font=Helvfont)
				lblApellido.pack(side=TOP)

				lblFecha=Label(frmFecha, text="Fecha",background='#008D34',font=Helvfont)
				lblFecha.pack(side=TOP)

				lblMonto=Label(frmMonto, text="Monto",background='#008D34',font=Helvfont)
				lblMonto.pack(side=TOP)

				lblReceta=Label(frmReceta,text="Receta",background='#008D34',font=Helvfont)
				lblReceta.pack(side=TOP)


				# creo un scrollbar y lo coloco en el frame frmReceta
				scrollbarDetalles=Scrollbar(frmReceta) 
				scrollbarDetalles.pack(side=RIGHT,fill=Y)


				# creo los listbox y los pongo en sus frames 
				lstNombre=Listbox(frmNombre,activestyle=tk.NONE,bg='#000000',fg='#ffffff',width=20,height=20, exportselection=False,selectmode=BROWSE,yscrollcommand=scrollbarDetalles.set)
				lstNombre.pack(side=LEFT,fill=BOTH)

				lstApellido=Listbox(frmApellido,activestyle=tk.NONE,bg='#000000',fg='#ffffff',width=20,height=20, exportselection=False,selectmode=BROWSE,yscrollcommand=scrollbarDetalles.set)
				lstApellido.pack(side=LEFT,fill=BOTH)

				lstFecha=Listbox(frmFecha,activestyle=tk.NONE,bg='#000000',fg='#ffffff',width=12,height=20, exportselection=False,selectmode=BROWSE,yscrollcommand=scrollbarDetalles.set)
				lstFecha.pack(side=LEFT,fill=BOTH)

				lstMonto=Listbox(frmMonto,activestyle=tk.NONE,bg='#000000',fg='#ffffff',width=10,height=20, exportselection=False,selectmode=BROWSE,yscrollcommand=scrollbarDetalles.set)
				lstMonto.pack(side=LEFT,fill=BOTH)

				lstReceta=Listbox(frmReceta,activestyle=tk.NONE,bg='#000000',fg='#ffffff',width=30,height=20, exportselection=False,selectmode=BROWSE,yscrollcommand=scrollbarDetalles.set)
				lstReceta.pack(side=LEFT,fill=BOTH)

				

			

				# le asigno el scrollbar a los listbox
				exportselection=False
				# Conecto los cinco listbox con la acción yview 
				def yview(*args):
					lstNombre.yview(*args)
					lstApellido.yview(*args)
					lstFecha.yview(*args)
					lstMonto.yview(*args)
					lstReceta.yview(*args)

				scrollbarDetalles.config(command=yview)  # Asocia el command a la funcion yview(*args)


				




				#Conecta a la base de datos con las tablas clientes y deuda juntas.
				cursor.execute("select * from clientes inner join deuda on clientes.idclientes=deuda.idclientes where clientes.idclientes = %s;",(indice,))

	
				#-999- este while lo que hace es 
				tupDeudaDetalle = cursor.fetchone()
				auxDetalle=True
				
				
			
				while (auxDetalle and tupDeudaDetalle!=None): #la condicion tupDeudaDetalle!=None la pongo por si no tiene deuda. para que no de error.
					nom=str(tupDeudaDetalle[1])#lo convierto a string porque sino no me deja mostrarlo en el listbox
					ape=str(tupDeudaDetalle[2])
					fecha=str(tupDeudaDetalle[5]) 
					monto=str(tupDeudaDetalle[7])
					receta=str(tupDeudaDetalle[8])
					f=metodos.ordenarFechaParaCliente(fecha)

					lstNombre.insert(END,nom)
					lstApellido.insert(END,ape)
					lstFecha.insert(END,f)
					lstMonto.insert(END,monto)
					lstReceta.insert(END,receta)


					tupDeudaDetalle=cursor.fetchone()		
					auxDetalle=tupDeudaDetalle
				#-999-


			
			
			def abrirVentanaSuma():
				ventanaSuma=tk.Toplevel()
				ventanaSuma.title("Nueva Compra")
				#----------------Ancho x Alto - Horizontal + Vertical
				ventanaSuma.geometry('320x200+210+130')
				ventanaSuma.configure(background='#008D34')
				s = tk.DoubleVar() #variable asociada al Entry txtSuma
				r = tk.StringVar() #variable asociada al Entry txtReceta
				fechaSuma = tk.StringVar() #variable asociada al Entry txtReceta
				lblSuma= Label(ventanaSuma,text="Ingrese Deuda Nueva",bg='#008D34')
				lblSuma.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
				lblReceta= Label(ventanaSuma,text="Receta",bg='#008D34')
				lblReceta.grid(row=1,column=0,padx=5,pady=5,sticky=tk.W)
				lblFecha= Label(ventanaSuma,text="Cambiar fecha",bg='#008D34')
				lblFecha.grid(row=2,column=0,padx=5,pady=5,sticky=tk.W)
				txtSuma = Entry(ventanaSuma,textvariable=s)
				txtSuma.grid(row=0,column=1,padx=5,pady=5)
				txtReceta = Entry(ventanaSuma,textvariable=r)
				txtReceta.grid(row=1,column=1,padx=5,pady=5)
				txtFecha = Entry(ventanaSuma,textvariable=fechaSuma)
				txtFecha.grid(row=2,column=1,padx=5,pady=5)
				lblNota = Label(ventanaSuma,text="En caso de cambiar la fecha, debe ser del formato ddmmaaaa",bg='#008D34')
				lblNota.grid(row=6,column=0,padx=5,pady=5,columnspan=3)



				#--- 
				def onEnterOk(event):  
   					sumarDatos()
    
				#--- Aca se asocia el evento Return al Entry txtNombre
				#    	para que al dar enter ejecute la funcion onEnterBuscarCliente
				txtSuma.bind('<Return>', onEnterOk)
				txtReceta.bind('<Return>', onEnterOk)
				txtFecha.bind('<Return>', onEnterOk)






				def sumarDatos():				
					cursor=con.cursor()					
					montoASumar=s.get() #valor obtenido del entry txtSuma de la ventana ventanaSuma
					nombre=nn
					apellido=aa


					if len(str(fechaSuma.get()))!=0:
						ahora=datetime.strptime(str(fechaSuma.get()), "%d%m%Y").date()
					else:	
						ahora = datetime.now() #carga en ahora la fecha actual.				
					det=r.get() #Detalle.
					try:
						sqlDate="INSERT INTO deuda(iddeuda,fecha,idclientes,monto,detalle) VALUES (%s,%s,%s,%s,%s)" #inserta en la tabla deuda la fecha de hoy.
						cursor.execute(sqlDate,(0,ahora,idCli,montoASumar,det))				
					except mysql.connector.Error as err:
  						print("Something went wrong: {}".format(err))  			
					con.commit()
					cursor.close()
					
					
					

					año=str(ahora.year)#lo convierto a string porque sino no me deja mostrarlo en el listbox
					mes=str(ahora.month)
					dia=str(ahora.day)
					
					strMontoASumar=str(montoASumar)#lo convierto a string porque sino no me deja mostrarlo en el listbox
				
				

	
					lstMontoDetalle.insert(END,strMontoASumar)


					#Estos if son para corregir lo impreso en el listbox lstFechaDetalle ya que si el mes o el dia es del 1 al 9 lo va a imprimir
					#	sin el cero adelante y va a generar conflictos al momento de borrar. es solo correccion.
					
					if int(mes)<10:
						if int(dia)<10:
							lstFechaDetalle.insert(END,"0"+dia+"-0"+mes+"-"+año)
						else:	
							lstFechaDetalle.insert(END,dia+"-0"+mes+"-"+año)
					else:
						if int(dia)<10:
							lstFechaDetalle.insert(END,"0"+dia+"-"+mes+"-"+año)
						else:
							lstFechaDetalle.insert(END,dia+"-"+mes+"-"+año)
					

					#estas 3 lineas de abajo son para actualizar el entry de la deuda total.
					dd2=calcularDeuda(indice)
					txtDeudaTotalEncontrado.delete(0, END)
					txtDeudaTotalEncontrado.insert(0,dd2)

					actualizarLstDetallesGeneral2(lstDetallesGeneral,lstDetallesGeneral2,lstDetallesGeneral3,lstDetallesGeneral4,lstDetallesGeneral5) #Actualiza lstDetallesGeneral (metodo de metodos.py)





    				#vacia campos de texto.
					txtSuma.delete(0, END)
					txtReceta.delete(0, END)
					txtFecha.delete(0, END)	


    



				botonOk=Button(ventanaSuma,bg="#D3FFE3",activeforeground="#ffffff",activebackground="#40C16F",text="Ok!-!",font=HelvfontBoton,command=sumarDatos)
				botonOk.grid(row=5,column=0,padx=5,pady=5,sticky=tk.W)
				



			

			botonBorrar=Button(frameCliEncontradoB,bg="#D3FFE3",activeforeground="#ffffff",activebackground="#40C16F",text="Pagó",font=HelvfontBoton,command=borrarDatos)
			botonBorrar.grid(row=0,column=0,padx=5,pady=5)

			botonSumar=Button(frameCliEncontradoB,bg="#D3FFE3",activeforeground="#ffffff",activebackground="#40C16F",text="Compró",font=HelvfontBoton,command=abrirVentanaSuma)
			botonSumar.grid(row=0,column=1,padx=5,pady=5)

			botonDetalles=Button(frameCliEncontradoB,bg="#D3FFE3",activeforeground="#ffffff",activebackground="#40C16F",text="Detalles 3",font=HelvfontBoton,command=abrirVentanaDetalles)
			botonDetalles.grid(row=0,column=2,padx=5,pady=10)	

			# elimina el cliente seleccionado. lo ejecuta el botonEliminarCliente
			def eliminarCliente():
				cursor=con.cursor()
				#-- Variable de tipo booleana que almacena el resultado del askyesno
				#		si el usuario apreta si da verdadero sino da falso.
				auxBoolean = messagebox.askyesno(message="Cuidado!!!!!, está por borrar un cliente, ¿Desea continuar?", title="Título")
				#-- Si dio verdadero elimina al cliente. Sino vuelve a la ventana anterior.
				if (auxBoolean):
					n=nombreBuscarCliente.get()
					a=apellidoBuscarCliente.get()
					cursor.execute("delete from clientes where nombre=%s and apellido=%s;",(n,a,))
					messagebox.showinfo("OK!!!","Listo!!!, Cliente borrado correctamente.")
					cursor.close()
					con.commit() #guarda cambios en la base de datos.
					ventanaClienteEncontrado.destroy() #cierra ventana ventanaClienteEncontrado
					actualizarLstDetallesGeneral2(lstDetallesGeneral,lstDetallesGeneral2,lstDetallesGeneral3,lstDetallesGeneral4,lstDetallesGeneral5) #actualiza (lstDetallesGeneral) de la ventana principal.



			botonEliminarCliente=Button(frameCliEncontradoB,width=18,height=1,bg="#D3FFE3",activeforeground="#ffffff",activebackground="#40C16F",text="- Eliminar Cliente -",font=HelvfontBoton14, command=eliminarCliente)
			botonEliminarCliente.grid(row=1,column=0,columnspan=3,padx=5,pady=5)	


	#--- Esta funcion busca en la base de datos un cliente. 
	def onEnterBuscarCliente(event):  
   		buscarCliente()
    
	#--- Aca se asocia el evento Return al Entry txtNombre
	#    	para que al dar enter ejecute la funcion onEnterBuscarCliente
	txtNombreBuscar.bind('<Return>', onEnterBuscarCliente)
	txtApellidoBuscar.bind('<Return>', onEnterBuscarCliente)


	botonSiguiente=Button(ventanaBuscarClientes,bg="#D3FFE3",activeforeground="#ffffff",activebackground="#40C16F",text="Buscar cliente",font=HelvfontBoton,command=buscarCliente)
	botonSiguiente.grid(row=2,column=0,padx=5,pady=15)



#---Esta funcion crea la ventanaClientes
def abrirVentanaClientes():
	ventanaClientes=tk.Toplevel()
	ventanaClientes.title("Clientes")
	#----------------Ancho x Alto - Horizontal + Vertical
	ventanaClientes.geometry('220x200+40+100')
	ventanaClientes.configure(background='#008D34')

	#--- Creacion de Radiobutton
	#--- La funcion estado abre la ventana correspondiente segun la opcion del radiobutton
	def estado():
		if (selec.get() == 1):
			abrirVentanaNuevoClientes()
			ventanaClientes.destroy()
		elif (selec.get() == 2):
			abrirVentanaBuscarClientes()	
			ventanaClientes.destroy()
		

	selec=IntVar()
	

	rbNuevo = Radiobutton(ventanaClientes,activebackground="#008D34",text="Nuevo",bg='#008D34',font=Helvfont,value=1,variable=selec)
	rbNuevo.grid(row=0,column=0,padx=5,pady=5, sticky=tk.W)
	rbEditar = Radiobutton(ventanaClientes,activebackground="#008D34",text="Buscar",bg='#008D34',font=Helvfont,value=2,variable=selec)
	rbEditar.grid(row=1,column=0,padx=5,pady=5, sticky=tk.W)
	
	


	botonSiguiente=Button(ventanaClientes,bg="#D3FFE3",activeforeground="#ffffff",activebackground="#40C16F",text=".Siguiente",font=HelvfontBoton,command=estado)
	botonSiguiente.grid(row=4,column=0,padx=5,pady=15)

#--- 105 Clientes

#Esta funcion la implemente para ayudar a la memoria del usuario, por si se olvida como se llama algun cliente.
def abrirVentanaListarClientes():
	VentanaListarClientes=tk.Toplevel()
	VentanaListarClientes.title("Lista de Clientes")
#----------------Ancho x Alto - Horizontal + Vertical
	VentanaListarClientes.geometry('280x400+350+130')
	VentanaListarClientes.configure(background='#008D34')	

	
	cursor=con.cursor()
	
	#-- creo los frames y los coloco en la ventanaClienteEncontrado
	frmNombre = Frame(VentanaListarClientes)
	frmNombre.grid(row=0,column=0,pady=10)

	frmApellido = Frame(VentanaListarClientes)
	frmApellido.grid(row=0,column=1,pady=10)


	
	
	#Esta funcion es para sincronizar los listbox en su seleccion
	def seleccion(event):   #El parametro event no se para que sirve pero ni no esta da error.			
		itemDeselec = lstApellido.curselection()	
		#Si habia elemento seleccionado en lstApellido entonces este if se cumple y desselecciona	
		if (len(itemDeselec)!=0):
			lstApellido.selection_clear(itemDeselec)
		#copia el elemento seleccionado en lstNombre en itemABorrar
		itemABorrar = lstNombre.curselection() 
		lstApellido.select_set(itemABorrar)
		
		
		
		
		


	# creo un scrollbar 
	scrollbarListarClientes=Scrollbar(frmApellido) 
	scrollbarListarClientes.pack(side=RIGHT,fill=Y)

	# creo los listbox para nombre y apellido y los pongo en los frames
	lstNombre=Listbox(frmNombre,activestyle=tk.NONE,bg='#000000',fg='#ffffff',height=20,width=20,exportselection=False,selectmode=BROWSE,yscrollcommand=scrollbarListarClientes.set)
	lstNombre.pack(side=LEFT,fill=BOTH)

	#Asocio el evento ListboxSelect (elemento seleccionado) con la funcion seleccion en lstApellido
	lstNombre.bind('<<ListboxSelect>>',seleccion)

	lstApellido=Listbox(frmApellido,activestyle=tk.NONE,bg='#000000',fg='#ffffff',height=20,width=20,exportselection=False,selectmode=BROWSE,yscrollcommand=scrollbarListarClientes.set)
	lstApellido.pack(side=LEFT,fill=BOTH)

	# Conecto los tres listbox con la acción yview 
	def yview(*args):
		lstNombre.yview(*args)
		lstApellido.yview(*args)
		
	scrollbarListarClientes.config(command=yview)  # Asocia el command a la funcion yview(*args)


	
	cursor.execute("SELECT * FROM clientes ORDER BY nombre ASC ") #selecciona todos los clientes por nombre ordenado alfabeticamente.
				
	

	#-999- este while lo que hace es insertar en la lista lstDeuda los campos fecha y monto asociados al cliente.
	tupListarClientes = cursor.fetchone()
	auxDetalle=True	
	
	while (auxDetalle and tupListarClientes!=None): #la condicion tupListarClientes!=None la pongo por si no tiene deuda. para que no de error.
		listarClientesNombre=str(tupListarClientes[1]) #lo convierto a string porque sino no me deja mostrarlo en el listbox
		listarClientesApellido=str(tupListarClientes[2])
		lstNombre.insert(END,listarClientesNombre)
		lstApellido.insert(END,listarClientesApellido)
		tupListarClientes=cursor.fetchone()		
		auxDetalle=tupListarClientes
	#-999-
	cursor.close()



	






#                    *************** VENTANA PRINCIPAL ***************


#frame1 es para poner los botones de la ventana principal (ventana)
#---------------------------Ancho x Alto
frame1 = Frame(ventana,height=100,width=400,bg='#008D34')
frame1.grid(row=0,column=0,sticky=tk.N,pady=30,padx=10)

#frames es para poner los listbox 
#-------------------------Ancho x Alto
frame2 = Frame(ventana,height=100,width=100,bg='#008D34')
frame2.grid(row=0,column=1,pady=10)

#---------------------------Ancho x Alto
frame3 = Frame(ventana,height=100,width=100,bg='#008D34')
frame3.grid(row=0,column=3,pady=10)

frame4 = Frame(ventana,height=100,width=100,bg='#008D34')
frame4.grid(row=0,column=4,pady=10)

frame5 = Frame(ventana,height=100,width=100,bg='#008D34')
frame5.grid(row=0,column=5,pady=10)

frame6 = Frame(ventana,height=100,width=100,bg='#008D34')
frame6.grid(row=0,column=6,pady=10)

lblNombre=Label(frame2, text="Nombre",background='#008D34',font=Helvfont)
lblNombre.pack(side=TOP)

lblNombre=Label(frame3, text="Apellido",background='#008D34',font=Helvfont)
lblNombre.pack(side=TOP)

lblNombre=Label(frame4, text="Fecha",background='#008D34',font=Helvfont)
lblNombre.pack(side=TOP)

lblNombre=Label(frame5, text="Monto",background='#008D34',font=Helvfont)
lblNombre.pack(side=TOP)

lblNombre=Label(frame6,text="Receta",background='#008D34',font=Helvfont)
lblNombre.pack(side=TOP)




exportselection=False


# creo un scrollbar y lo coloco en el frame frame6
scrollbarDetallesGeneral=Scrollbar(frame6) 
scrollbarDetallesGeneral.pack(side=RIGHT,fill=Y)

# creo un listbox y lo pongo en el frame frame2
#---------------------------------Ancho x Alto
lstDetallesGeneral=Listbox(frame2,activestyle=tk.NONE,borderwidth=0,bg='#000000',fg='#ffffff',width=20,height=27, exportselection=False, selectmode=tk.BROWSE,yscrollcommand=scrollbarDetallesGeneral.set)
lstDetallesGeneral.pack(side=LEFT,fill=BOTH)
# le asigno el scrollbar a el listbox lstDetallesGeneral
lstDetallesGeneral2=Listbox(frame3,activestyle=tk.NONE,borderwidth=0,bg='#000000',fg='#ffffff',width=20,height=27, exportselection=False, selectmode=tk.BROWSE,yscrollcommand=scrollbarDetallesGeneral.set)
lstDetallesGeneral2.pack(side=LEFT,fill=BOTH)

lstDetallesGeneral3=Listbox(frame4,activestyle=tk.NONE,borderwidth=0,bg='#000000',fg='#ffffff',width=15,height=27, exportselection=False, selectmode=tk.BROWSE,yscrollcommand=scrollbarDetallesGeneral.set)
lstDetallesGeneral3.pack(side=LEFT,fill=BOTH)

lstDetallesGeneral4=Listbox(frame5,activestyle=tk.NONE,borderwidth=0,bg='#000000',fg='#ffffff',width=10,height=27, exportselection=False, selectmode=tk.BROWSE,yscrollcommand=scrollbarDetallesGeneral.set)
lstDetallesGeneral4.pack(side=LEFT,fill=BOTH)

lstDetallesGeneral5=Listbox(frame6,activestyle=tk.NONE,borderwidth=0,bg='#000000',fg='#ffffff',width=45,height=27, exportselection=False, selectmode=tk.BROWSE,yscrollcommand=scrollbarDetallesGeneral.set)
lstDetallesGeneral5.pack(side=LEFT,fill=BOTH)

# Conecto los tres listbox con la acción yview 
def yview(*args):
	lstDetallesGeneral.yview(*args)
	lstDetallesGeneral2.yview(*args)
	lstDetallesGeneral3.yview(*args)
	lstDetallesGeneral4.yview(*args)
	lstDetallesGeneral5.yview(*args)

scrollbarDetallesGeneral.config(command=yview)  # Asocia el command a la funcion yview(*args)

actualizarLstDetallesGeneral2(lstDetallesGeneral,lstDetallesGeneral2,lstDetallesGeneral3,lstDetallesGeneral4,lstDetallesGeneral5)







# *** Ventana principal (hasta aca)***


def abrirVentanaIngresos():
	VentanaIngresos=tk.Toplevel()
	VentanaIngresos.title("Ingresos")
	#----------------Ancho x Alto - Horizontal + Vertical
	VentanaIngresos.geometry('250x220+480+130')
	VentanaIngresos.configure(background='#008D34')
	ing = tk.DoubleVar()
	lblIngresos=Label(VentanaIngresos, text="Ingresos",background='#008D34',font=Helvfont)
	lblIngresos.grid(row=0,column=1,padx=5,pady=5)
	lblEspacio1=Label(VentanaIngresos, text="          ",background='#008D34',font=Helvfont)
	lblEspacio1.grid(row=1,column=0,padx=5,pady=5)
	txtIngresos=Entry(VentanaIngresos,textvariable=ing)
	txtIngresos.grid(row=1,column=1,padx=5,pady=5)
	lblEspacio2=Label(VentanaIngresos, text="",background='#008D34',font=Helvfont)
	lblEspacio2.grid(row=2,column=0,padx=5,pady=5)
	lblEspacio3=Label(VentanaIngresos, text="",background='#008D34',font=Helvfont)
	lblEspacio3.grid(row=4,column=0,padx=5,pady=5)
	lblExplicacion=Label(VentanaIngresos, text="    Ingrese el monto a SUMAR a su cuenta",background='#008D34')
	lblExplicacion.grid(row=5,column=0,padx=5,pady=5,columnspan=4)
	
	def sumarIngreso(i):
		valorASumar=i.get() # Se usa el get porque le estamos pasando por parametro int, que es de tipo DoubleVar().
		#con=mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='bdasher1')
		cursor=con.cursor()
		sqlIngreso="INSERT INTO ingresos(idingresos,monto) VALUES (%s,%s)" 
		cursor.execute(sqlIngreso,(0,ing.get()))
		con.commit() # eg  monto egreso.
		cursor.close()
		txtIngresos.delete(0, END) # Borra los datos escritos en el entry txtIngresos para que quede vacio
	

	#--- Esta funcion suma a la base de datos un ingreso nuevo.
	def onEnterIngreso(event):  
   		sumarIngreso(ing)
    
	#--- Aca se asocia el evento Return al Entry txtIngresos
	#    	para que al dar enter ejecute la funcion onEnterIngreso
	txtIngresos.bind('<Return>', onEnterIngreso) 



	btnSumarIngreso=Button(VentanaIngresos,bg="#D3FFE3",activeforeground="#ffffff",activebackground="#40C16F",text="           OK             ",font=HelvfontBoton,command = lambda: sumarIngreso(ing))
	btnSumarIngreso.grid(row=3,column=1,padx=5,pady=5,sticky=tk.W)



def abrirVentanaEgresos():
	VentanaEgresos=tk.Toplevel()
	VentanaEgresos.title("Egresos")
	#----------------Ancho x Alto - Horizontal + Vertical
	VentanaEgresos.geometry('250x220+480+130')
	VentanaEgresos.configure(background='#008D34')
	eg = tk.DoubleVar()
	lblIngresos=Label(VentanaEgresos, text="Egresos",background='#008D34',font=Helvfont)
	lblIngresos.grid(row=0,column=1,padx=5,pady=5)
	lblEspacio1=Label(VentanaEgresos, text="          ",background='#008D34',font=Helvfont)
	lblEspacio1.grid(row=1,column=0,padx=5,pady=5)
	txtEgresos=Entry(VentanaEgresos,textvariable=eg)
	txtEgresos.grid(row=1,column=1,padx=5,pady=5)
	

	lblEspacio2=Label(VentanaEgresos, text="",background='#008D34',font=Helvfont)
	lblEspacio2.grid(row=2,column=0,padx=5,pady=5)
	lblEspacio3=Label(VentanaEgresos, text="",background='#008D34',font=Helvfont)
	lblEspacio3.grid(row=4,column=0,padx=5,pady=5)
	lblExplicacion=Label(VentanaEgresos, text="   Ingrese el monto a RESTAR a su cuenta",background='#008D34')
	lblExplicacion.grid(row=5,column=0,padx=5,pady=5,columnspan=4)
	def sumarEgreso(e):
		valorASumar=e.get() # Se usa el get porque le estamos pasando por parametro int, que es de tipo DoubleVar().
		#con=mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='bdasher1')
		cursor=con.cursor()
		sqlEgreso="INSERT INTO egresos(idegresos,monto) VALUES (%s,%s)" 
		cursor.execute(sqlEgreso,(0,eg.get()))
		con.commit() # eg  monto egreso.
		cursor.close()
		txtEgresos.delete(0, END) # Borra los datos escritos en el entry para que quede vacio


	#--- Esta funcion suma a la base de datos un gasto nuevo.
	def onEnterEgreso(event):  
   		sumarEgreso(eg)
 
	#--- Aca se asocia el evento Return al Entry txtEgresos
	#    	para que al dar enter ejecute la funcion onEnterEgreso
	txtEgresos.bind('<Return>', onEnterEgreso) 

	btnSumarEgreso=Button(VentanaEgresos,bg="#D3FFE3",activeforeground="#ffffff",activebackground="#40C16F",text="           OK             ",font=HelvfontBoton,command = lambda: sumarEgreso(eg))
	btnSumarEgreso.grid(row=3,column=1,padx=5,pady=5,sticky=tk.W)



# Al presionar salir hace todos los backup y luego cierra el programa.
def salir():
	backupTablaPagos()  # Hace un backup de todo lo que los clientes ya pagaron y su fecha.
	backupDeudasClientes() # Hace un backup de todas las deudas que tienen los clientes.
	backupTablaClientes() # Hace un backup de todos los datos de los clientes.
	ventana.quit()

#---------- Menu -----------
barraMenu = Menu(ventana)
menuInicio = Menu(barraMenu)
menuInicio.add_command(label="Clientes",command=abrirVentanaClientes)
menuInicio.add_command(label="Listar Clientes",command=abrirVentanaListarClientes)
menuInicio.add_separator()
menuInicio.add_command(label="Salir",command=salir)
menuContabilidad = Menu(barraMenu)
menuContabilidad.add_command(label="Ingresos",command=abrirVentanaIngresos)
menuContabilidad.add_command(label="Gastos",command=abrirVentanaEgresos)
menuBackup = Menu(barraMenu)
menuBackup.add_command(label="Backup Deuda Clientes",command=backupDeudasClientes)



barraMenu.add_cascade(label="Inicio",menu=menuInicio)
barraMenu.add_cascade(label="Contabilidad",menu=menuContabilidad)
barraMenu.add_cascade(label="Backup",menu=menuBackup)
ventana.config(menu=barraMenu)
	

#-----------BOTONES DE LA VENTANA PRINCIPAL----------- 
# activeforeground="#ffffff"  es para que la letra al presionar el boton se ponga blanca
# activebackground="#40C16F"  es para que el boton al ser presionado se ponga del color #40C16F


botonIngredienteNuevo=Button(frame1,bg="#D3FFE3",activeforeground="#ffffff",activebackground="#40C16F",width=15,height=1,text="Nuevo Ingrediente",font=HelvfontBoton, background='azure2',command=abrirVentanaIngredienteNuevo)
botonIngredienteNuevo.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)

botonBorrarIngrediente=Button(frame1,bg="#D3FFE3",activeforeground="#ffffff",activebackground="#40C16F",width=15,height=1,text="Borrar Ingrediente",font=HelvfontBoton, background='azure2',command=abrirVentanaBorrarIngrediente)
botonBorrarIngrediente.grid(row=1,column=0,padx=5,pady=5,sticky=tk.W)

botonAgregar=Button(frame1,bg="#D3FFE3",activeforeground="#ffffff",activebackground="#40C16F",width=15,height=1,text="Nueva Receta",font=HelvfontBoton, background='azure2', command=abrirVentanaNuevaReceta)
botonAgregar.grid(row=2,column=0,padx=5,pady=5,sticky=tk.W)

botonBorrar=Button(frame1,bg="#D3FFE3",activeforeground="#ffffff",activebackground="#40C16F",width=15,height=1,text="Borrar receta",font=HelvfontBoton, background='azure2',command=abrirVentanaBorraReceta)
botonBorrar.grid(row=3,column=0,padx=5,pady=5,sticky=tk.W)

botonComprar=Button(frame1,bg="#D3FFE3",activeforeground="#ffffff",activebackground="#40C16F",width=15,height=1,text="Hacer compras  ",font=HelvfontBoton, background='azure2', command=abrirVentanaCompras)
botonComprar.grid(row=4,column=0,padx=5,pady=5,sticky=tk.W)



#---100 Estas lineas son para que al presionar la cruz roja de la ventana principal, haga esos backup
#			antes de cerrar el programa.
def on_closing():
	backupTablaPagos()  # Hace un backup de todo lo que los clientes ya pagaron y su fecha.
	backupDeudasClientes() # Hace un backup de todas las deudas que tienen los clientes.
	backupTablaClientes() # Hace un backup de todos los datos de los clientes.
	ventana.quit()

ventana.protocol("WM_DELETE_WINDOW", on_closing)
#---100 hasta aca

ventana.mainloop()