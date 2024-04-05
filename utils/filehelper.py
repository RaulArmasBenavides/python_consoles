def agregar_articulo(articulo):
    archivo_lista = open("utils\lista.txt","a")
    archivo_lista.write("{}\n".format(articulo))
    archivo_lista.close()



if __name__ =="__main__":
  agregar_articulo(input("Ingresar artículo al archivo txt"))