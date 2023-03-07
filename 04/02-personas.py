#!/usr/bin/env python
# coding: utf-8
personas = []
pactual = {}
print("Por favor ingrese los datos de una persona a la vez.\nDeje el nombre en blanco cuando no desee ingresar más personas.")
pactual["nombre"]=input("Nombre: ")
pactual["apellido"]=input("Apellido: ")
pactual["cedula"]=input("Cédula: ")
pactual["edad"]=int(input("Edad: "))
personas.append(pactual.copy())
while pactual["nombre"] != "" :
    pactual["nombre"]=input("Nombre: ")
    pactual["apellido"]=input("Apellido: ")
    pactual["cedula"]=input("Cédula: ")
    pactual["edad"]=int(input("Edad: "))
    personas.append(pactual.copy())
k=1
for persona in personas :
    print("La persona número",k,"es",persona["nombre"],persona["apellido"]+".\nTiene",persona["edad"],"años, y su cédula es",persona["cedula"]+".\n")
    k+=1
print("Fin del programa.")
