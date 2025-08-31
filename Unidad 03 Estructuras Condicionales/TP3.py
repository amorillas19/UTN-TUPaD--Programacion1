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