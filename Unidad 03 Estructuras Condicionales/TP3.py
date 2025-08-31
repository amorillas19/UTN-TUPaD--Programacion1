#Ejercicio 1

edad=int(input("Escriba la edad del usuario: "))
if (edad>=18):
    print("Usted es mayor de edad.")

#Ejercicio 2

nota_alumano=int(input("Ingrese su nota: "))
if(nota_alumano>=6):
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3

numero_par=int(input("Ingrese numero par: "))
if(numero_par % 2 == 0):
    print("Ha ingresadop un número par")
else:
    print ("Por favor, ingrese un número par")

#Ejercicio 4

edad=int(input("Ingrese su edad: "))
if(edad<12):
    print("Niño/a")
elif(edad>=12 and edad<18):
    print("Adolescente")
elif(edad>= 18 and edad<30):
    print("Adulto/a joven")
elif(edad>30):
    print("Adulto/a")

#Ejercicio 5

password=(input("Ingrese la contraseña:"))
if((len(password))>=8 and (len(password))<=14):
    print ("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6

import random
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1, 100) for i in range (50)]
print(mode(numeros_aleatorios))
print(median(numeros_aleatorios))
print(mean(numeros_aleatorios))

#Ejercicio 7

palabra_usuario=(input("Ingrese una frase o palabra: "))
palabra_usuario=palabra_usuario.lower()
ultimo_caracter=(len(palabra_usuario)-1)
if (palabra_usuario[ultimo_caracter] == "a"):
    print (palabra_usuario+"!")
elif(palabra_usuario[ultimo_caracter] == "e"):
    print (palabra_usuario+"!")
elif(palabra_usuario[ultimo_caracter] == "i"):
    print (palabra_usuario+"!")
elif(palabra_usuario[ultimo_caracter] == "o"):
    print (palabra_usuario+"!")
elif(palabra_usuario[ultimo_caracter] == "u"):
    print (palabra_usuario+"!")
else:
    print(palabra_usuario)

#Ejercicio 8

nombre=str(input("Ingrese su nombre"))
print("Menu de opciones")
print("1. Si quiere su nombre en mayúsculas")
print("2. Si quiere su nombre en minúsculas")
print("3. Si quiere su niombre con la primer letra mayúscula")
opcion=int(input("Ingrese la opcion deseada:"))

if(opcion==1):
    print(nombre.lower())
elif(opcion==2):
    print(nombre.upper())
elif(opcion==3):
    print(nombre.title())
else:
    print("La opcion ingresada no es correcta")


#Ejercicio 9

terremoto=float(input("ingrese la magnitud del terremoto: "))

if terremoto<3 and terremoto>0:
    print("muy leve")
elif terremoto>=3 and terremoto<4:
    print("leve")
elif terremoto>=4 and terremoto<5:
    print("moderado")
elif terremoto>=5 and terremoto<6:
    print("Fuerte")
elif terremoto>=6 and terremoto<7:
    print("Muy fuerte")
elif terremoto>7:
    print("extremo")
else:
    print("No es un valor que corresponde a la escala de Ritcher")


#Ejercicio 10

hemisferio:str=str(input("Ingrese en cual hemisterio se encuentra: "))
hemisferio=hemisferio.upper()
mes:int=int(input("Que mes del año es? "))
dia:int=int(input("Que día del año es? "))


if(mes==1):
    if(hemisferio=="N"):
        print("Invierno")
    elif(hemisferio=="S"):
        print("Verano")
elif(mes==2):
    if(hemisferio=="N"):
        print("Invierno")
    elif(hemisferio=="S"):
        print("Verano")
elif(mes==3):
    if(dia<=20):
        if(hemisferio=="N"):
            print("Invierno")
        if(hemisferio=="S"):
            print("Verano")
    elif(dia>=21):
        if(hemisferio=="N"):
            print("Primavera")
        if(hemisferio=="S"):
            print("Otoño")
if(mes==4):
    if(hemisferio=="N"):
        print("Primavera")
    elif(hemisferio=="S"):
        print("Otoño")
elif(mes==5):
    if(hemisferio=="N"):
        print("Primavera")
    elif(hemisferio=="S"):
        print("Otoño")
elif(mes==6):
    if(dia<=20):
        if(hemisferio=="N"):
            print("Primavera")
        if(hemisferio=="S"):
            print("Otoño")
    elif(dia>=21):
        if(hemisferio=="N"):
            print("Verano")
        if(hemisferio=="S"):
            print("Invierno")
if(mes==7):
    if(hemisferio=="N"):
        print("Verano")
    elif(hemisferio=="S"):
        print("Invierno")
elif(mes==8):
    if(hemisferio=="N"):
        print("Verano")
    elif(hemisferio=="S"):
        print("Invierno")
elif(mes==9):
    if(dia<=20):
        if(hemisferio=="N"):
            print("Verano")
        if(hemisferio=="S"):
            print("Invierno")
    elif(dia>=21):
        if(hemisferio=="N"):
            print("Otoño")
        if(hemisferio=="S"):
            print("Primavera")
if(mes==10):
    if(hemisferio=="N"):
        print("Otoño")
    elif(hemisferio=="S"):
        print("Primavera")
elif(mes==11):
    if(hemisferio=="N"):
        print("Otoño")
    elif(hemisferio=="S"):
        print("Primavera")
elif(mes==12):
    if(dia<=20):
        if(hemisferio=="N"):
            print("Otoño")
        if(hemisferio=="S"):
            print("Primavera")
    elif(dia>=21):
        if(hemisferio=="N"):
            print("Invierno")
        if(hemisferio=="S"):
            print("Verano")  