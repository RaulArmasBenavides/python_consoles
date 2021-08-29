espar = lambda num: num%2 ==0 
print(espar(100000423428142149824821489219823414234214231423142))

suma = lambda x,y:x+y

print(suma(2,3)) 


numeros = [1,2,3,4,5]
#map selecciona una lista y evalua una lsita barriendo   -> param (MÉTODO LAMBDA, LISTA)
print(list(map(lambda num : num*2 , numeros)))


#generarr una lista que contenga todos los números mútiples comunes de 2,3,4,8 entre 0 y 500 ( ambos incluidos)
# NO pueden contener numeros repetidos y estos deben estar ordenados de menor a mayor 
# Completa el ejercicio en una línea
multiples = [i for i in range(0, 501) if i%2 == 0 and i%3 == 0 and i%4 == 0 and i%8 == 0]