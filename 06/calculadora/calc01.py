#!/usr/bin/env python
# coding: utf-8
#
# Programa principal de calculadora

from libfunc import *

a=int(input("Ingrese el primer operando: "))
b=int(input("Ingrese el segundo operando: "))
oper=(input("Ingrese la operación (+, -, *, / o %): "))

if oper == '+' :
    print("El resultado de sumar {} y {} es: {}.".format(a,b,suma(a,b)))
if oper == '-' :
    print("El resultado de restar {} y {} es: {}.".format(a,b,rest(a,b)))
if oper == '*' :
    print("El resultado de multiplicar {} por {} es: {}.".format(a,b,mult(a,b)))
if oper == '/' :
    print("El resultado de dividir {} entre {} es: {}.".format(a,b,divi(a,b)))
if oper == '%' :
    print("El remanente de dividir {} entre {} es: {}.".format(a,b,modu(a,b)))
