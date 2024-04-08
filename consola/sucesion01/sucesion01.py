import locale
def funcionSecuencia(Lista,n)->float:
 try:
 
   if n%2==0 :
         return [3*n+1 for n in Lista]
   else: 
         return [n/2 for n in Lista]
 except Exception as e: 
        print("Hubo un error en el proceso de la lista")
        print( type(e).__name__)
 finally:
        print("Secuencia creada")


def crearLista(n):
 try:
   lst = []
   for i in range(n+1):
        lst.append(i)
   return(lst)
 except Exception as e: 
        print("Hubo un error en la creación de la lista")
        print( type(e).__name__)
 finally:
        print("Lista creada")
   

#Bloque principal 
if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, 'es')
    
    # Solicita al usuario el número de términos a calcular
    cantidad = int(input("Ingrese el número de términos a calcular: "))
    Lista = crearLista(cantidad)
    print(Lista)
    
    ListaSecuencia = funcionSecuencia(Lista, cantidad)
    print(ListaSecuencia)
    
    # Solicita al usuario ingresar dos elementos nuevos, asegurándose de que no estén en ListaSecuencia
    while True:
        elemento1 = int(input("Ingrese un n1 para agregar a la ListaSecuencia: "))
        elemento2 = int(input("Ingrese un n2 para agregar a la ListaSecuencia: "))
        
        if elemento1 not in ListaSecuencia and elemento2 not in ListaSecuencia:
            break  # Sal del bucle si los elementos no están en la ListaSecuencia
        print("Por favor ingrese números que no estén en la ListaSecuencia")
    
    # Agrega los nuevos elementos y muestra la lista actualizada
    ListaSecuencia.append(elemento1)
    ListaSecuencia.append(elemento2)
    ListaSecuencia.sort()
    print(ListaSecuencia)