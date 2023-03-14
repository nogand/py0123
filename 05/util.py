#!/usr/bin/env python
# coding: utf-8

# Funciones útiles para aprovechar en otros programas

def pedir_entero(titulo):
    seguir=True
    while seguir :
        numero=input(titulo)
        if numero.isnumeric() :
            seguir=False
        else :
            print("Error. Por favor ingrese un número entero.")
    return int(numero)

def pedir_flotante(titulo):
    numero=input(titulo)
    try :
        numero=float(numero)
        return numero
    except :
        print("Error. Por favor ingrese un número de punto flotante.")
        return pedir_flotante(titulo)
