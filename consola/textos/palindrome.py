import locale
if __name__ == "__main__":
    # Establecer localización en español
    locale.setlocale(locale.LC_ALL, 'es')

    # Inicializar variables
    cantidad = 0
    Lista = []
    ListaSecuencia = []

    # Obtener la palabra del usuario
    palabra = str(input("Ingrese la palabra"))

    # Calcular la longitud de la palabra
    longitud = len(palabra)

    # Invertir la palabra
    inversoNumero = ""
    for i in range(longitud):
        inversoNumero = inversoNumero + palabra[longitud-1-i]

    # Comprobar si la palabra es palíndroma
    if inversoNumero == palabra:
        print("La palabra es palíndroma")
    else:
        print("La palabra no es palíndroma")
