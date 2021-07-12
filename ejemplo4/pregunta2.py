import numpy as np
import subprocess


#validaciones de los datos de ingreso
def ValidarEntero(n):
    try:
        n=int(n)
    except:
        n=ValidarEntero(input("Caracter no valido: "))
    return n

def ValidarDecimal(n):
    try:
        n=float(n)
    except:
        n=ValidarDecimal(input("Caracter no valido: "))
    return n

def ns(c):
    while c!=("s") and c!=("n"):
        print(chr(7));c=input("Escribe solo \'n\' o \'s\' según su opción: ")
    return(c)

def val(tp):
    while tp!="N" and tp!="M":
        tp=input("Introduzca \'N\' para dato numérico y \'M\' para matriz: ")
    return tp

#FUNCIÓN DE TIPO DE DATO
def dato():
    tipo_dato=val(input("Tipo de dato: "))
    if tipo_dato=="M":
        matr=crea_matriz(fil,col)
    else:
        matr=ValidarEntero(input("Introduce número: "))
    return matr

#FUNCIÓN PARA DEFINIR MATRIZ
def crea_matriz(fil,col)->[]:
    f=-1;c=-1
    e_fil=[]
    for f in range(fil):
        e_col=[]
        f+=1
        for c in range(col):
            c+=1
            valor=ValidarDecimal(input('Registrar el elemento (%d,%d): '%(f,c)))
            e_col.append(valor)
        e_fil.append(e_col)
        matri=np.array(e_fil,float)
    return matri


#FUNCIÓN PARA SUMAR MATRICES
def suma_matriz(A,B,col,fil):
 i=-1;j=-1 
 C=[]
 #Proceso
 for i in range(fil):
  for j in range(col):
   C.append( A[i][j] + B[i][j])
 print(C)

#FUNCIÓN PARA RESTAR MATRICES
def diferencia_matriz(A,B,col,fil):
 i=-1;j=-1 
 C=[]
 #Proceso
 for i in range(fil):
  for j in range(col):
   C.append( A[i][j] - B[i][j])
 print(C)
    


while True:
    print("          CALCULADORA DE MATRICES          ") 
    print("""************TABLA DE OPERADORES************
*******************************************
SUMA                           OPERADOR "+"
RESTA                          OPERADOR "-"
MULTIPLICACION                 OPERADOR "*"
FINALIZAR PROCESO              OPERADOR "C"
DATO MATRIZ                    OPERANDO "M"
DATO NÚMERO                    OPERANDO "N"
*******************************************
*******************************************""")
    
    fil=ValidarEntero(input("Indique número de filas: "))
    col=ValidarEntero(input("Indique número de columnas: "))
    e=fil
    f=-1;c=-1
    A=crea_matriz(fil,col)
    B=crea_matriz(fil,col)
    acum = []
    print("\n")
    print(A,"\n")
    print(B,"\n")
    while True:
        oper=input("Introduzca operador: ")
        while oper!="+" and oper!="-" and oper!="*" and oper!="C":
            oper=input("Introduzca un operador válido: ")
        if oper=="+":
            suma_matriz(A,B,fil,col)
            #matr=dato()
            #cum=acum+matr
        elif oper=="-":
        	diferencia_matriz(A,B,fil,col)
            #matr=dato()
            #acum=acum-matr
        elif oper=="*":
            tipo_dato=val(input("Tipo de dato: "))
            if tipo_dato=="M":
                fil=col
                #col=ValidarEntero(input("Introduce número de columnas: "))
                # matr=crea_matriz(fil,col)
                acum=np.dot(A,B)
                fil=e
            else:
                matr=ValidarEntero(input("Introduce número: "))
                acum=A*matr
                
        if oper!="C":
            print("\nRESULTADO")
            print(acum)


        else:
            break
        
    conti=ns(input("¿Reiniciar cálculos?:(n para finalizar) "))
    if conti=="n":
        break
    matr=0
    subprocess.call(["cmd.exe","/C","cls"])