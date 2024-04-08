from os import path

def agregar_articulo(articulo):
    archivo_lista = open("utils\lista.txt","a")
    archivo_lista.write("{}\n".format(articulo))
    archivo_lista.close()

def escribir_archivo():
    archivo = open('texto.txt','w')
    archivo.write('Hola Mundo de Python')
    archivo.close()

def leer_archivo():
    if path.isfile('texto.txt'):
        archivo = open('texto.txt', 'r')
        #textos = archivo.read()
        textos = archivo.readlines()
        archivo.close()

        print(textos)
    else: 
        print('No existe el archivo')

def agregar_datos():
    if path.isfile('texto.txt'):
        archivo = open('texto.txt', 'a')
        archivo.write('\nHola Juan')
        archivo.close()

    else:
        print('No existe el archivo')

def modificar_datos():
    if path.isfile('texto.txt'):
        archivo = open('texto.txt', 'r+')
        texto = archivo.readlines()
        print(texto)
        texto[1] = 'Hola Alex Roel\n'
        #archivo.write('\nHola Juan')
        print(texto)
        archivo.seek(0)
        archivo.writelines(texto)
        archivo.close()
        print(texto)

    else:
        print('No existe el archivo')

def eliminar_datos():
    archivo = open('texto.txt', 'w')
    archivo.close()

if __name__ =="__main__":
  agregar_articulo(input("Ingresar artículo al archivo txt"))