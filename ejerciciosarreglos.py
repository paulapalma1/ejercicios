print("ejercicios con arreglos")
import numpy as np
import random as rd
'''arreglo1=np.arange(1,4)
print(arreglo1)
arreglo2=arreglo1[:].copy()
print(arreglo2)
arreglo2[0]=100
print(arreglo2)
print(arreglo1)
arreglo1=arreglo1*2
print(arreglo1)'''
arregloA=np.zeros(100, dtype=int) #inicializa el arreglo
print(arregloA)
for i in range(len(arregloA)):
    arregloA[i]=rd.randint(0,500)
print(arregloA)
for i in range(len(arregloA)):
    if arregloA[i]%2==0:
        print(arregloA[i])
        print("la posición es: ", i)
for i in range(len(arregloA)):
    if i%2==0:
        print(arregloA[i])
mayor=arregloA.max()
print("el mayor es:",mayor)