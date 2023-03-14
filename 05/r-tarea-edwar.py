#!/usr/bin/env python
# coding: utf-8

# Solución basada en la respuesta de Edwar, disponible en:
# https://github.com/dbpeloy/python_greencore/blob/main/clase13marzo/intento-tarea-edwar.py
#

'''
Ciclo para contar del 1 al 100
Ejercicio de mate
Imprima los números del 1 al 100, agregando un caracter especial si el número es divisible entre 2, 3 o 5.

Ciclo para contar del 1 al 100

Intentando resolver
'''

def pedir_numero(titulo):
    numero=input(titulo)
    if numero.isnumeric() :
        return int(numero)
    else :
        print("Error. Por favor ingrese un número entero.")
        return pedir_numero(titulo)

 
# Pedir número inicial y final de la lista que se va a recorrer
inicio = pedir_numero("Ingrese el número inicial de la lista......: ")
fin = pedir_numero("Ingrese el número final de la lista........: ")

# Pedir los divisores
divisores=[]
while True :
    divactual=pedir_numero("Los divisores actuales son: "+str(divisores)+"\nIngrese el siguiente divisor, o cero para terminar...:")
    if divactual == 0 :
        if len(divisores) > 0 :
            break
        else :
            print("Error. Debe ingresar al menos un divisor.")
    else :
        divisores.append(divactual)

'''
divisor1 = int(input("Ingrese el primer número divisor...: "))
divisor2 = int(input("Ingrese el segundo número divisor..: "))
divisor3 = int(input("Ingrese el tercer número divisor...: "))


# Crear la lista de números
numeros = list(range(inicio, fin+1))

# Crear una nueva lista con los números divisibles por los tres divisores pero solo me saca los divisibles exactos
# por ejemplo haciendo una lista de 0 a 100 me dice que los números divisibles por 2 3 y 5 son: [30, 60, 90]
# aqui ==> de nuevo el AND y el OR me vacilaron ****
# divisibles = [num for num in numeros if num % divisor1 == 0 and num % divisor2 == 0 and num % divisor3 == 0]

# corregido a OR
divisibles = [num for num in numeros if num % divisor1 == 0 or num % divisor2 == 0 or num % divisor3 == 0]

# Imprimir los números divisibles encontrados
print("Los números divisibles por", divisor1, divisor2, "y", divisor3, "son:", divisibles)
'''

for i in range(inicio, fin+1) :
    print("El número actual es",i)
    for d in divisores :
        if i % d == 0 :
            print("{} es divisible por {}.".format(i,d))

# Falta 0 para Terminar