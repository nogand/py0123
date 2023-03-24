#!/usr/bin/env python
# coding: utf-8

''' 
La serie de Fibonacci tiene la siguiente forma:
1 1 2 3 5 8 13 21 ...

Los dos primeros términos son 1 y 1, y todos los demás son la suma de los dos términos anteriores.
'''

def fibo(n) :
    if n == 0 or n == 1 :
        return 1
    else :
        return fibo(n-1)+fibo(n-2)
