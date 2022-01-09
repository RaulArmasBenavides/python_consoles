import mysql.connector

mydb = mysql.connector.connect(host="localhost", username ="root", password ="", database = "dbsegur")

#cursor =  mydb.cursor()
#cursor.execute('SELECT * FROM area')
#area = cursor.fetchone()
#areas = cursor.fetchall()
#print(areas)
#mydb.close()


def agregar_area():
   area = input("Nombre del área nueva que desea ingresar")
   cursor = mydb.cursor()
   try:
   		cursor.execute("insert into area(nombre) values ('{}')".format(area))
   except:
   		print("Hubo un error al insertar regsitro en la tabla area")
   else: 
   	    print("Área registrada correctamente")
   mydb.commit()
   mydb.close()

	


#Menù 
while True:
    print("Bienvenido al menù de la empresa ")
    opcion = input(" Introduce una opciòn:(1) Agregar un àrea")
    if opcion =="1":
    	agregar_area()
    elif opcion =="2":
    	print("Saliendo del programa")
    	break
    else:
    	print("opcion incorrecta")
   