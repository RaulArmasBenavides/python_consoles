espar = lambda num: num%2 ==0 
print(espar(100000423428142149824821489219823414234214231423142))

suma = lambda x,y:x+y

print(suma(2,3)) 


numeros = [1,2,3,4,5]
#map selecciona una lista y evalua una lsita barriendo   -> param (MÉTODO LAMBDA, LISTA)
print(list(map(lambda num : num*2 , numeros)))