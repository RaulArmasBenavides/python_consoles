import locale

def es_palindromo(cadena):
    # Eliminamos los espacios y convertimos a minúsculas para la comparación
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]


if __name__ == "__main__":
    # Establecer localización en español
    locale.setlocale(locale.LC_ALL, 'es')
    # Obtener la palabra del usuario
    palabra = str(input("Ingrese la palabra"))
    # Calcular la longitud de la palabra
    longitud = len(palabra)
    # Comprobar si la palabra es palíndroma
    if es_palindromo(palabra):
        print("La palabra es palíndroma")
    else:
        print("La palabra no es palíndroma")
