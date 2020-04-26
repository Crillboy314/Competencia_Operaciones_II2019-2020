#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 16:06:45 2020

@author: luisquintero
"""

#Esta aplicacion fue disenada por los siguientes integrantes
# 00200703 Luis Quintero
# 00202954 Diego Lara
# 00200770 Jose Calderon 




 

import pandas as pd
import numpy as np
import random as rd 
import matplotlib.pyplot as plt

#mensaje de Bienvenida a la Aplicacion 
print ("Bienvenido persona que necesita saber un estimado de propagacion del Covid-19")

#Mostrar en pantalla la tabla con los valores reales, para que el usuario pueda escoger 2 dias libremente
print ("los datos del mes de marzo son los siguientes")
print (" 10 marzo    [17]")
print (" 12 marzo    [19]")
print (" 14 marzo    [28]")
print (" 16 marzo    [58]")
print (" 18 marzo    [168]")
print (" 20 marzo    [426]")
print (" 22 marzo    [789]")
print (" 24 marzo    [1082]")
print (" 26 marzo    [1403]")










#Creamos un excel con la tabla proporcionada para mejor manejo de datos, a continuacion la importacion de dicho excel


xls = pd.read_excel('Competencia_Datos.xlsx') 
data = pd.DataFrame(xls)
#Almacenamiento de cada una de las celdas del excel en python para poder operar con estos datos
A2 = data['Dias_Marzo'].tolist()[0]
A3 = data['Dias_Marzo'].tolist()[1]
A4 = data['Dias_Marzo'].tolist()[2]
A5 = data['Dias_Marzo'].tolist()[3]
A6 = data['Dias_Marzo'].tolist()[4]
A7 = data['Dias_Marzo'].tolist()[5]
A8 = data['Dias_Marzo'].tolist()[6]
A9 = data['Dias_Marzo'].tolist()[7]
A10 = data['Dias_Marzo'].tolist()[8]

#Estas variables se convertiran a integers para evitar problemas en los calculos siguientes
A2int = int(A2)
A3int = int(A3)
A4int = int(A4)
A5int = int(A5)
A6int = int(A6)
A7int = int(A7)
A8int = int(A8)
A9int = int(A9)
A10int = int(A10)


B2 = data['Infectados'].tolist()[0]
B3 = data['Infectados'].tolist()[1]
B4 = data['Infectados'].tolist()[2]
B5 = data['Infectados'].tolist()[3]
B6 = data['Infectados'].tolist()[4]
B7 = data['Infectados'].tolist()[5]
B8 = data['Infectados'].tolist()[6]
B9 = data['Infectados'].tolist()[7]
B10 = data['Infectados'].tolist()[8]


#Estas variables se convertiran a integers para evitar problemas en los calculos siguientes
B2int = int(B2)
B3int = int(B3)
B4int = int(B4)
B5int = int(B5)
B6int = int(B6)
B7int = int(B7)
B8int = int(B8)
B9int = int(B9)
B10int = int(B10)

#Preguntar al usuario que dias va a utilizar, especificando que ingrese solo numeros para que no haya errores
X = input("Que dia quieres utilizar como dato 1? (escribe solo el numero del dia) ")
Y = input("Que dia quieres utilizar como dato 2? ")
#Convertir a integers los inputs por consola para que no haya problemas de strings e integers
Xnum = int(X)
Ynum = int(Y)
#Realizar la prediccion con los modelos planteados en la hoja proporcionada
infectados = (Xnum*Ynum)
Prediccion = (infectados**2)


# LA RAZON DE UTILIZAR ESTAS SENTENCIAS IF PARA LA PREDICCION 
# se utilizaron estos ifs para que si el usuario ingresaba un dia no valido, saltara un anuncio de que hay un error y 
# se muestre un agradecimiento por usar el programa
# Se sobreentiende que el usuario al escribir bien la primera prediccion no necesitara de una comprobacion sobre dias para las predicciones 2 y 3 
#por tanto las prediciones 2 y 3 no utilizan SENTENCIAS IFS


if  Xnum == 10:  
        if Ynum == 12:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 14:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 16:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 18:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 20:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 22:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 24:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 26:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
                    
                            
elif Xnum == 12:     

        if Ynum == 10:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 14:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 16:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 18:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 20:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 22:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 24:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 26:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
       
elif Xnum == 14:     

        if Ynum == 10:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 12:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 16:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 18:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 20:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 22:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 24:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 26:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
elif Xnum == 12:     

        if Ynum == 10:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 14:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 16:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 18:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 20:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 22:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 24:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 26:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
elif Xnum == 16:     

        if Ynum == 10:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 14:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 12:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 18:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 20:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 22:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 24:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 26:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
elif Xnum == 18:     

        if Ynum == 10:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 14:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 16:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 12:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 20:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 22:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 24:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 26:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")

elif Xnum == 20:     

        if Ynum == 10:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 14:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 16:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 12:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 18:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 22:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 24:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 26:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")

elif Xnum == 22:     

        if Ynum == 10:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 14:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 16:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 18:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 20:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 12:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 24:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 26:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")

elif Xnum == 24:     

        if Ynum == 10:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 14:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 16:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 18:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 20:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 22:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 12:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 26:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")

elif Xnum == 26:     

        if Ynum == 10:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 14:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 16:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 12:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 28:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 22:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 24:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")
        elif Ynum == 18:
            print ("La prediccion para hoy con los dias", Xnum, "de marzo y ", Ynum, "de marzo es" ,  Prediccion , "Infectados")



else:
    print ("No escogiste dias validos, gracias por usar el programa")
#Preguntas 3 y 4, para definir un segundo modelo de operacion
print ( "Por Segunda vez, toma dos dias distintos por favor")
Z = input("Que dia quieres utilizar como dato 3? (escribe solo el numero del dia) ")
A = input("Que dia quieres utilizar como dato 4? ")

Anum = int(A)
Znum = int(Z)

infectados2 = (Anum*Znum)
Prediccion2 = (infectados2**2)


#preguntas 5 y 6, define el ultimo modelo en pantalla
print ( "Por Ultima vez, toma dos dias distintos por favor")
B = input("Que dia quieres utilizar como dato 5? (escribe solo el numero del dia) ")
C = input("Que dia quieres utilizar como dato 6? ")

Bnum = int(B)
Cnum = int(C)

infectados3 = (Bnum*Cnum)
Prediccion3 = (infectados3**2)

#Presentacion de toda la informacion en pantalla en un parrafo, con suficiente espacio entre oraciones para facilitar lectura
print ("Te presentaremos todo  en una linea final resumida")
print ("La prediccion con el modelo de dias", Xnum, " y dias", Ynum, " es ", Prediccion, "infectados", ",    por otro lado para el modelo con dias " , Znum, "y", Anum, "es de ", Prediccion2, "infectados",  ",   finalmente considerando el modelo de dias", Bnum, "Y", Cnum, " es de", Prediccion3, "Infectados")
#imprimir los distintos escenarios posibles basando en las combinaciones que tiene el usuario

       
       
      
