# Asignaciones de variables
A=2
B=2

# Condicion
if (A>B) :
    # Esto se ejecuta solamente si A es mayor que B
    print("A es mayor que B")
    A=A+1
else :
    if (A<B) :
        print("A es menor que B")
        A=float(A/B)
    else :
        print("A y B son iguales!")

# Imprimimos resultados
print("A vale",A," y B vale",B)
