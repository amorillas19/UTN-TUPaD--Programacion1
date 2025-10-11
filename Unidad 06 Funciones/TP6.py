#Ejercicio 1

def imprimir_hola_mundo():
    print ("Hola mundo!")

imprimir_hola_mundo()

#Ejercicio 2

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")


nombre_usuario=input("Cual es su nombre?")
saludar_usuario(nombre_usuario)

#Ejercicio 3

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


nombre_usuario=input("Ingrese el nombre: ")
apellido_usuario=input("Ingrese el apellido: ")
edad=input("Ingrese la edad: ")

while(not(edad.isdigit())):
    print("No ingreso una edad valida. Por favor ingrese la edad: ")
    edad=input("Ingrese la edad")
edad=int(edad)

residencia=input("Ingrese residencia")

informacion_personal(nombre_usuario, apellido_usuario, edad, residencia)

#Ejercicio 4

import math

def calcular_area_circulo(radio):
    pi=math.pi
    area : float=float(pi*(radio**2))
    return area

def calcular_perimetro_circulo(radio):
    pi=math.pi
    perimetro :float=float(2*pi*radio)
    return perimetro


radio=input("Ingrese el radio: ")

if(not(radio.isdigit)):
    while(not(radio.isdigit)):
        radio=input("Ingrese el radio: ")
else:
    radio=float(radio)        

print(f"El area del circulo es de {calcular_area_circulo(radio)} cm")

print(f"El perimetro del circulo es de {calcular_perimetro_circulo(radio)} cm")

#Ejercicio 5

def segundos_a_horas(segundos):
    horas=float((segundos/60)/60)
    return horas

segundos=input("Cuantos segundos desea pasar a horas?")

if(not(segundos.isdigit)):
    while(not(segundos.isdigit)):
        segundos=input("Cuantos segundos desea pasar a horas? ")
else:
    segundos=float(segundos)   


print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos)} horas")

#Ejercicio 6

def tabla_multiplicar(numero):

    for i in range(11):
        print(f"{numero} * {i} = {(numero*i)}")


multiplicado=input("Ingrese el numero: ")

if(not(multiplicado.isdigit)):
    while(not(multiplicado.isdigit)):
        multiplicado=input("Lo ingresado no es valido. Ingrese el numero: ")
else:
    multiplicado=int(multiplicado)

tabla_multiplicar(multiplicado)   

#Ejercicio 7

def operaciones_basicas(a, b):
    tupla=((a+b),(a-b),(a*b),(a/b))
    return tupla


numero_1=input("Ingrese el numero 1: ")
if(not(numero_1.isdigit)):
    while(not(numero_1.isdigit)):
        numero_1=input("Lo ingresado no es valido. Ingrese el numero 1: ")
else:
    numero_1=int(numero_1)

numero_2=input("Ingrese el numero 2: ")
if(not(numero_2.isdigit)):
    while(not(numero_2.isdigit)):
        numero_2=input("Lo ingresado no es valido. Ingrese el numero 2: ")
else:
    numero_2=int(numero_2)

tupla_main=operaciones_basicas(numero_1, numero_2)

print(f"La suma de {numero_1} y {numero_2} es {tupla_main[0]}")
print(f"La resta de {numero_1} y {numero_2} es {tupla_main[1]}")
print(f"La multiplicacion de {numero_1} y {numero_2} es {tupla_main[2]}")
print(f"La division de {numero_1} y {numero_2} es {tupla_main[3]}")

#Ejercicio 8

def calcular_imc(peso, altura):
    imc=peso/altura**2
    imc=round(imc, 2)
    return imc


peso=input("Ingrese su peso")
if(not(peso.isdigit)):
    while(not(peso.isdigit)):
        peso=input("Lo ingresado no es valido. Ingrese el peso: ")
else:
    peso=float(peso)

altura=input("Ingrese su altura en centimetros")
if(not(altura.isdigit)):
    while(not(altura.isdigit)):
        altura=input("Lo ingresado no es valido. Ingrese su altura: ")
else:
    altura=float(altura)
    altura=altura/100    

print(calcular_imc(peso,altura))

#Ejercicio 9

def celsius_fahren(celsius):
    fahren=(celsius * 1.8) + 32
    return fahren

celsius=input("Ingrese su temperatura en grados celsius: ")
if(not(celsius.isdigit)):
    while(not(celsius.isdigit)):
        celsius=input("Lo ingresado no es valido. Ingrese la temperatura en grados Celsius: ")
else:
    celsius=int(celsius)

print(f"La temperatura en grados Fahrenheit es de {celsius_fahren(celsius)} grados")

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

