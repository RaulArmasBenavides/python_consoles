import pyodbc 


def EstablecerConexion():
    try:
        cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=localhost;"
                      "Database=sifco;"
                      "Trusted_Connection=yes;")
        return cnxn.cursor()
    except Exception as e: 
        print("Error en la conexión")
        print( type(e).__name__)
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

cursor.execute('SELECT * FROM supervisor.ubicacion')

ubicacion = cursor.fetchone()
ubicaciones = cursor.fetchall()

#print(ubicacion)
#print(ubicaciones)

print("-------------------")
for row in cursor:
    print('row = %r' % (row,))


cursor.close()
#https://stackoverflow.com/questions/33725862/connecting-to-microsoft-sql-server-using-python/33727190