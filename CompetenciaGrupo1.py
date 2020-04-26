#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 17:24:47 2020

@author: sofia.gallegos
"""


#Creamos una def que nos ayuda a sacar el iba de un arreglo, primero suma y luego 
# a la suma la multiplica por 0.12 (iva)
def iva(a):
    suma = sum(a)
    multi = suma*0.12
    return(multi)

#Para poder guardar las transacciones totales  creo un arreglo vaico
    
transacciones=[]

#El while pregunta al usuario el total de la compra y luegoalmacena ese valor en 
# el arreglo vacio que cree antes
#Finalmente, presenta el valor del total 

while True:
    try:
        valortotal=float(input("Cuanto es el valor de la compra?"))
    except ValueError:
        print("Cantidad no valida")
        continue
    if valortotal<=0 :
        print("Cantidad no valida")
        continue
    transacciones.append(valortotal)
    print("El ahorro de tus transacciones es ", iva(transacciones))

#Se debe detener el while para continuar con el programa que preddice aproximadamente la propagación del virus.

#Valores de  días y número de infectados 
    
dias = [0, 2, 4, 6, 8, 10, 12, 14, 16]
infectados = [17, 19, 28, 58, 168, 426, 789, 1082, 1403]

#Creación de las funciones que definiran las preddiciones

def predicciones(x1, x2, y1, y2):
    b12 = pow((y2/y1),1/(x2-x1)) 
    A = y1/pow(b12,x1)
    return(b12, A)

#d es la variable que define el número de días de hoy día (01 de abril), el cual es 22

d = 22 
(b, A) = predicciones(dias[0], dias[1], infectados[0], infectados[1])
y = int(A*pow(b, d))
    
print ("La predicción es de {} con el modelo de días 10 y 12 de Marzo.".format(y))

d = 22 
(b, A) = predicciones(dias[2], dias[3], infectados[2], infectados[3])
y1 = int(A*pow(b, d))

print ("La predicción es de {} con el modelo de días 14 y 16 de Marzo.".format(y1))    

d = 22 
(b, A) = predicciones(dias[5], dias[6], infectados[5], infectados[6])
y2 = int(A*pow(b, d))

print ("La predicción es de {} con el modelo de días 20 y 22 de Marzo.".format(y2)) 
   

