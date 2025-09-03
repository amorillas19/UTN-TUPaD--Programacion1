#Ejercicio 1

for i in range (0,101):
    print (i)

#Ejercicio 2

numero_usuario=int(input("Ingrese un numero"))
numero_usuario=abs(numero_usuario)
contador=0

while(numero_usuario>0):
    numero_usuario=numero_usuario//10
    contador=contador+1

print(f"El numero {numero_usuario} tiene {contador} digitos")

#Ejercicio 3
numero_1=int(input("Ingrese el primer numero"))
numero_2=int(input("Ingrese el segundo numero"))

for i in range(numero_1, numero_2):
    print(i)

#Ejercicio 4

numero_usuario=int(input("Ingrese el numero para agregar. (Ingrese 0 para finalizar): "))
suma_total=0
while(numero_usuario!=0):
    suma_total=suma_total+numero_usuario
    numero_usuario=int(input("Ingrese el numero para agregar. (Ingrese 0 para finalizar): "))

print(f"La suma acumulada de los numeros ingresados es: {suma_total}")

#Ejercicio 5

import random
numero_adivinar=random.randint(0,9)
contador=1

numero_usuario=int(input("Adivina el numero: "))
while(numero_usuario!=numero_adivinar):
    print("Numero incorrecto.")
    contador=contador+1
    numero_usuario=int(input("Adivina el numero: "))
print("Felicitaciones. Has adivinado el numero.")
print(f"Te ha tomado {contador} intento(s).")

#Ejercicio 6

for i in range (100, -1, -2):
    print(i)


#Ejercicio 7

numero_usuario=int(input("Ingrese un numero entero valido"))
for i in range (0, numero_usuario+1):
    print(i)

#Ejercicio 8

contadorIntentos=0
contadorPar=0
contadorImpar=0
contadorPositivo=0
contadorNegativo=0


while(contadorIntentos<100):
    numero_usuario=int(input("Ingrese el numero"))
    if(numero_usuario%2==0):
        contadorPar+=1
    else:
        contadorImpar+=1

    if(numero_usuario>0):
        contadorPositivo+=1
    else:
        contadorNegativo+=1

    contadorIntentos+=1

print("Hay ", contadorPositivo, " numeros positivos")
print("Hay ", contadorNegativo, " numeros negativos")  
print("Hay ", contadorPar, " numeros pares")  
print("Hay ", contadorImpar, " numeros impares")

#Ejercicio 9

#Ejercicio 9

contador_ingresos=0
numero_total=0

while(contador_ingresos<5):
    numero_usuario=int(input("Ingrese un numero: "))
    numero_total=numero_total+numero_usuario
    contador_ingresos+=1

print("La media de los valores ingresados es: ", (numero_total/contador_ingresos))  

#Ejercicio 10

numero_usuario=(int(input("Ingrese el numero, para invertir el orden de los digitos: ")))
numero_usuario=abs(numero_usuario)
numero_invertido=0

while(numero_usuario>0):
    digito=numero_usuario%10
    numero_invertido=(numero_invertido*10)+digito
    numero_usuario=numero_usuario//10

print(numero_invertido)

