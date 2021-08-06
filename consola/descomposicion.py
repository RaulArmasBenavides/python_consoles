"""  Crear un script llamado descomposición que realice
Debe tomar 1 argumneto que será un número positivo
En caso de no recibir argumento debe mostrar información acerca cómo utilziar script.
""" 

import sys



""" def Descomposicion (*args):
   try:
        result = 0
        # Iterating over the Python args tuple
        for x in args:
         result += x
   except Exception as e: 
        print("Hubo un error en la descomposición...Verificar")
        print( type(e).__name__)
   finally:
        print("Proceso finalizado")""" 

if len(sys.argv) == 2:
   numero = int(sys.argv[1])
   if numero <0 or numero > 9999:
   	 print("Error - Número es incorrecto")
   else:
   	 cadena = str(numero)
   	 longitud = len(cadena)

   	 for i in range(longitud):
   	 	#barrido inverso de cadenas 
   	 	print("{:04d}".format(int(cadena[longitud-1-i])*10**i))
else:
	print("Error Agumento incorrecto")
	print("Ejemplo : descomposicion.py [0-9999]")

