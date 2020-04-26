# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 18:47:48 2020

@author: alexa
"""
## Integrantes Grupo 2: Artieda Josué, Bermúdez Giorgina, Grijalva Lizeth, Murgueitio Mateo.

##########Competencia:

### 1: Programa que reciba como elementos de entrada los valores
#totales resultantes de una compra estatal y que devuelva en la consola cual fue el valor ahorrado
#como consecuencia del no pago de IVA. El programa no debe terminar. De ser posible, el
#programa tambi´en debe ir acumulando el dinero ahorrado durante las transacciones (que pudieran
#ser por ejemplo... 1000).

import pandas as pd
column_names = ['Compra Nº','PVP Provedor', 'Dev IVA','Dev IVA Acum','PVP Acum']
Tabla = pd.DataFrame(columns = column_names)

def compras(valor,suma_h,suma_t):
    valor= float(valor)
    dev_iva=0
    dev_iva= valor-(valor/1.12)
    suma_compra= suma_t+valor
    suma_dev_iva= suma_h+dev_iva
    return dev_iva, suma_dev_iva, suma_compra
  
n=0
dev=0
suma=0
suma_1=0
v=0
while n<13:
    n+=1
    v= input("Digite el valor de la compra, o digite salir, para terminar el programa: ")
    if v=="salir":
        break
        
    else:
        #compras(v,suma)
        dev,suma, suma_1=compras(v,suma,suma_1)
        print("Compra Actual: ", v) 
        print("Devolución Unitaria del IVA:",dev)
        print("Devolución Acumulada del IVA", suma)
        print("Compras Totales:", suma_1)
        Tabla= Tabla.append({'Compra Nº': n,'PVP Provedor': v, 'Dev IVA':dev ,'Dev IVA Acum': suma,'PVP Acum':suma_1},ignore_index=True)
        print(Tabla)
        continue


### 2: Escribir un c´odigo en python que devuelva la predicci´on para infectados del d´ıa de hoy, con al
#menos tres modelos distintos (esto es tomando d´ıas distintos para escoger los par´ametros) y que al
#terminar de correr imprima en consola algo como: la predicci´on con el modelo de d´ıas X1 y Y1 de
#Marzo es de XXXX, por otro lado, tomando el modelo de d´ıas X2 y Y2 la predicci´on es de XXXX,
#finalmente considerando el modelo de d´ıas X3 y Y3 la predicci´on es de XXXX.

import pandas as pd

print("Los datos reales de propagación del virus, son los siguientes:")
Genero_Percep = pd.DataFrame({
"Fecha": ["10 Marzo", "12 Marzo","14 Marzo", "16 Marzo","18 Marzo", "20 Marzo","22 Marzo", "24 Marzo", "26 Marzo"],
"Números": [17,19,28,58,168,426,789,1082,1403]})

print(Genero_Percep)
print("Con base en estos datos:")

##### Predicción
## Definición de variables

def beta(y1,y2,x1,x2):
    b=0
    b=(y2/y1)**(1/(x2-x1))
    return b
def alpha(beta,y1,x1):
    a=0
    a=(y1/(beta**x1))
    return a
 
#Modelo 1
def model1(día):
    día= int(día)
    y=0
    y1=17
    x1=10
    y2=1403
    x2=26
    beta1= beta(y1,y2,x1,x2)
    alpha1= alpha(beta1,y1,x1)
    print("b:",beta1)
    print("A:",alpha1)
    y=(alpha1*((beta1)**(día)))
    return y
#Modelo 2
def model2(día):
    día= int(día)
    y=0
    y1=17
    x1=10
    y2=58
    x2=16
    beta1= beta(y1,y2,x1,x2)
    alpha1= alpha(beta1,y1,x1)
    print("b:",beta1)
    print("A:",alpha1)
    y=(alpha1*((beta1)**(día)))
    return y
#Modelo 3
def model3(día):
    día= int(día)
    y=0
    y1=426
    x1=20
    y2=1403
    x2=26
    beta1= beta(y1,y2,x1,x2)
    alpha1= alpha(beta1,y1,x1)
    print("b:",beta1)
    print("A:",alpha1)
    y=(alpha1*((beta1)**(día)))
    return y

### Ejecución Modelos
#Modelo1
día= input("Para generar una predicción digite un día: ")
pre= model1(día)
día= str(día)
pre=str(pre)
print("Predicción para "+ día + " es: de " + pre ," infectados." )
#Modelo 2
día= input("Para generar una predicción digite un día: ")
pre= model2(día)
día= str(día)
pre=str(pre)
print("Predicción para "+ día + " es: de " + pre ," infectados.")
#Modelo 3
día= input("Para generar una predicción digite un día: ")
pre= model3(día)
dia= str(día)
pre=str(pre)
print("Predicción para "+ día + " es: de " + pre ," infectados.")


