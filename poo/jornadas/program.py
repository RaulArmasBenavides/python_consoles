#Librerías de Python 
import ipywidgets as widgets
import pandas as pd
import matplotlib.pyplot as plt

#Creamos la clase operario para registrar los datos de cada trabajador
class Operario:
  nombre=""
  codigo=""
  categoria=""
  Nestilo=""
  Htrabajadas=0.0
  Hproducidas=0.0
  eficiencia = 0.0

#Método constructor para la clase operario
  def __init__(self, nombre,codigo, categoria, Nestilo, Htrabajadas,Hproducidas):
    
    self.nombre = nombre
    self.codigo = codigo
    self.categoria = categoria
    self.Nestilo = Nestilo
    self.Htrabajadas = Htrabajadas
    self.Hproducidas = Hproducidas

#Método para calcular la eficiencia
  def calcularEficiencia(self):
    return self.Hproducidas/self.Htrabajadas # * (100%)#

#Método destructor
  def __del__(self):
    self.nombre = ""
    self.codigo= ""
    self.categoria = ""
    self.Nestilo = ""
    self.Htrabajadas= 0.0
    self.Hproducidas = 0.0
    
#Clase Interface de usuario (Boundary)
class IUOperario:
  #Atributos
  file = open("Logo.jpg", "rb")
  image = file.read()
  imgLogo = widgets.Image(value=image,format='jpg',width=100,height=120)
  htmlTitulo = widgets.HTML(value="<h1>Sistema de eficiencias</h1>")
  hboxTitulo = widgets.HBox([imgLogo, htmlTitulo])
  lblMensajes = widgets.Label(value="")
  txtNombre = widgets.Text(placeholder='Nombre', description='Nombre:', disabled=False) 
  txtCodigo = widgets.Text(placeholder='Codigo', description='Codigo:', disabled=False)  
  txtCategoria = widgets.Text(placeholder='Categoria', description='Categoria:', disabled=False)  
  txtEstilo= widgets.Text(placeholder='Estilo', description='Estilo:', disabled=False) 
  txtHorastrabajadas = widgets.BoundedFloatText(min=0.0,  description='H.trabajadas:', disabled=False)
  txtHorasproducidas= widgets.BoundedFloatText(min=0.0,  description='H.producidas:', disabled=False)
  btnRegistrar = widgets.Button(description='Registrar', button_style='info',tooltip='Actualizar registro en edicion', disabled=False)
  btnListar = widgets.Button(description='Listar', button_style='info',tooltip='Actualizar refistro en edicion', disabled=False)
  btnChart = widgets.Button(description='Estadísticas', button_style='info',tooltip='Actualizar estadísticas', disabled=False)
  toolbar = widgets.HBox([btnRegistrar, btnListar,btnChart])

  #Definimos una lista de operarios
  global lista_operarios
  lista_operarios = list()

  #Metodos para clase IUOperario
  def __init__(self):
    self.btnRegistrar.on_click(self.onRegistrarClick)
    self.btnListar.on_click(self.onListarClick)
    self.btnChart.on_click(self.onGraficoBarrasClick)
    self.show()
  
  #Método para limpiar las casillas luego de cada registro
  def LimpiarControles(self):
     self.txtNombre.value= ""
     self.txtCodigo.value=""
     self.txtCategoria.value=""
     self.txtEstilo.value=""
     self.txtHorastrabajadas.value="0"
     self.txtHorasproducidas.value="0"   
    
  #Método para registrar con el botón
  def onRegistrarClick(self, button):
    operario = Operario(self.txtNombre.value,
                        self.txtCodigo.value,
                        self.txtCategoria.value,
                        self.txtEstilo.value,
                        self.txtHorastrabajadas.value,
                        self.txtHorasproducidas.value,
                        )      
    operario.eficiencia= operario.calcularEficiencia()
    lista_operarios.append(operario)   
    print("Se registró exitosamente.")               
    self.LimpiarControles()

  #Método para mostrar las eficiencias de cada trabajador
  def GraficoBarras(self,lista_operarios):
      ## Declaramos valores para el eje x
      lsnombres = [o.nombre for o in lista_operarios]
      lsefi = [o.eficiencia for o in lista_operarios]
      eje_x = lsnombres 
       
      ## Declaramos valores para el eje y
      eje_y = lsefi #eficiencias
      
      ## Creamos Gráfica
      plt.bar(eje_x, eje_y)
      
      ## Legenda en el eje y
      plt.ylabel('Eficiencia')
      
      ## Legenda en el eje x
      plt.xlabel('Operarios')
      
      ## Título de Gráfica
      plt.title('Eficiencia de operarios - TOPITOP')
      
      ## Mostramos Gráfica
      plt.show()

  #Método para listar en el archivo de excel 
  def onListarClick(self, button):
    administrador = AdministradorOperarios("Operarios.xlsx", "Sheet1")
    administrador.listar(lista_operarios)


  def onGraficoBarrasClick(self, button):
       self.GraficoBarras(lista_operarios)

  def show(self):
    display (self.hboxTitulo,self.lblMensajes,self.txtNombre, self.txtCodigo, 
             self.txtCategoria, self.txtEstilo, self.txtHorastrabajadas, 
             self.txtHorasproducidas, self.toolbar )
    
#Clase Controladora (Control)
class AdministradorOperarios:
  #Atributos
  dfOperarios = None
  archivo = ""
  hoja = ""
  # Metodo constructor
  def __init__(self, archivo, hoja):
    self.archivo = archivo
    self.hoja = hoja
    self.dfOperarios = pd.read_excel(io=archivo, sheet_name=hoja)

  # Métodos de comportamiento
  def registrar(self, operario):
    ultimaFila = self.dfOperarios.shape[0]
    self.dfOperarios.loc[ultimaFila] = operario.filaExcel()
    self.dfOperarios.to_excel(self.archivo, self.hoja, index=False)

  def listar(self,list_operarios):
    dfOperarios = pd.DataFrame((o.__dict__ for o in list_operarios), columns = ['nombre' , 'codigo', 'categoria', 'Nestilo' , 'Htrabajadas' , 'Hproducidas', 'eficiencia'])
    print(dfOperarios)
    dfOperarios.to_excel(self.archivo)
    #print(self.dfOperarios)


#Programa principal
formOperario = IUOperario()
