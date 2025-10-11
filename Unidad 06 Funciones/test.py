#Ejercicio 10

def calcular_promedio(a,b,c):

    promedio=(a+b+c)/3
    return promedio

numero_1=input("Ingrese el numero 1: ")
if(not(numero_1.isdigit)):
    while(not(numero_1.isdigit)):
        numero_1=input("Lo ingresado no es valido. Ingrese el numero 1: ")
else:
    numero_1=float(numero_1)

numero_2=input("Ingrese el numero 2: ")
if(not(numero_2.isdigit)):
    while(not(numero_2.isdigit)):
        numero_2=input("Lo ingresado no es valido. Ingrese el numero 2: ")
else:
    numero_2=float(numero_2)

numero_3=input("Ingrese el numero 3: ")
if(not(numero_3.isdigit)):
    while(not(numero_3.isdigit)):
        numero_3=input("Lo ingresado no es valido. Ingrese el numero 3: ")
else:
    numero_3=float(numero_3)

print(f"El promedio es de {calcular_promedio(numero_1, numero_2, numero_3)}")