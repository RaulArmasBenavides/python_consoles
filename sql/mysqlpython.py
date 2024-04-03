import mysql.connector

mydb = mysql.connector.connect(host="localhost", username ="root", password ="", database = "dbsegur")

#cursor =  mydb.cursor()
#cursor.execute('SELECT * FROM area')
#area = cursor.fetchone()
#areas = cursor.fetchall()
#print(areas)
#mydb.close()


def agregar_area():
    area = input("Nombre del área nueva que desea ingresar: ")
    cursor = mydb.cursor()
    try:
        # Usar parámetros en lugar de formato de cadena para prevenir inyección SQL
        cursor.execute("INSERT INTO area(nombre) VALUES (%s)", (area,))
        print("Área registrada correctamente")
    except Exception as e:
        print("Hubo un error al insertar registro en la tabla área:", e)
    finally:
        mydb.commit()
        cursor.close() 
	
#Menù 
if __name__ == "__main__":
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
      