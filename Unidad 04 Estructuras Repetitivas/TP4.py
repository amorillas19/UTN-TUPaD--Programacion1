#Ejercicio 1

for i in range (0,101):
    print (i)

#Ejercicio 2

numero_usuario=int(input("Ingrese un numero"))
contador=0

while(numero_usuario>0):
    numero_usuario=numero_usuario//10
    contador=contador+1

print(f"El numero tiene {contador} digitos")

#Ejercicio 3

numero_1=int(input("Ingrese el primer numero"))
numero_2=int(input("Ingrese el segundo numero"))

for i in range (numero_1, numero_2):
    numero_total=int(numero_total+i)

print(numero_total)

#Ejercicio 4

numero_usuario=int(input("Por favor ingrese un numero entero para comenzar la suma. Ingrese 0 para finalizar: "))
suma_total=numero_usuario

while (numero_usuario != 0):
    numero_usuario=int(input("Por favor ingrese un numero entero para agregar a la suma. Ingrese 0 para finalizar: "))
    suma_total=suma_total+numero_usuario


print("La suma total de los enteros ingresados es: " , suma_total)

#Ejercicio 5

import random

numero_adivinar=int(random.randint(0,9))
contador_intentos=int(0)
print(numero_adivinar)
numero_del_usuario=int(input("Ingrese el numero que intenta adivinar"))

while (numero_adivinar!=numero_del_usuario):
    print("Incorrecto. Pruebe otra vez.")
