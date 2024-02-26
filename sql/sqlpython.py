import pyodbc 


def EstablecerConexion():
    try:

        #available_drivers = pyodbc.drivers()
        #print("Drivers ODBC disponibles:", available_drivers)
        cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=localhost;"
                      "Database=NWIN;"
                      "Trusted_Connection=yes;")
        return cnxn.cursor()
    except Exception as e: 
        print("Error en la conexión")
        print( e)
    finally:
        print("Proceso finalizado")


# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
#server = 'tcp:myserver.database.windows.net' 
#database = 'mydb' 
#username = 'myusername' 
#password = 'mypassword' 

#cursor = cnxn.cursor()
cursor = EstablecerConexion()

cursor.execute('SELECT * FROM Clientes')

cliente = cursor.fetchone()
clientes = cursor.fetchall()

print(cliente)
print(clientes)


#for row in cursor:
 ##   print('row = %r' % (row,))


cursor.close()

print("-------------------")
#https://stackoverflow.com/questions/33725862/connecting-to-microsoft-sql-server-using-python/33727190