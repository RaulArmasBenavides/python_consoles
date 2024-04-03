import sys

# La función Descomposicion parece no utilizarse según el script proporcionado.
# Asegúrate de ajustar su uso y definición según sea necesario.
def Descomposicion(*args):
    try:
        result = 0
        # Iterating over the Python args tuple
        for x in args:
            result += x
    except Exception as e:
        print("Hubo un error en la descomposición...Verificar")
        print(type(e).__name__)
    finally:
        print("Proceso finalizado")

if len(sys.argv) == 2:
    try:
        numero = int(sys.argv[1])
        if numero < 0 or numero > 9999:
            print("Error - Número es incorrecto")
        else:
            cadena = str(numero)
            longitud = len(cadena)

            for i in range(longitud):
                # Barrido inverso de cadenas
                print("{:04d}".format(int(cadena[longitud-1-i]) * 10**i))
    except ValueError:
        print("Error - Debe ingresar un número válido")
else:
    print("Error - Argumento incorrecto")
    print("Ejemplo: descomposicion.py [0-9999]")
