#!/usr/bin/env python
# coding: utf-8

from util import *

inicio = pedir_entero("Ingrese el número inicial de la lista......: ")
fin = pedir_entero("Ingrese el número final de la lista........: ")

# Pedir los divisores
divisores=[]
while True :
    divactual=pedir_entero("Los divisores actuales son: "+str(divisores)+"\nIngrese el siguiente divisor, o cero para terminar...:")
    if divactual == 0 :
        if len(divisores) > 0 :
            break
        else :
            print("Error. Debe ingresar al menos un divisor.")
    else :
        divisores.append(divactual)

columna=1
for i in range(inicio, fin+1) :
    divisible=False
    for d in divisores :
        if i % d == 0 :
            divisible=True
    if divisible :
        print('{:>5}'.format(i),"*", end=" ")
    else :
        print('{:>5}'.format(i)," ", end=" ")
    columna+=1
    if columna == 6 :
        print("")
        columna = 1
if columna > 1 :
    print("")

