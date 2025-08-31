
#Ejercicio 1
print("Hola Mundo!")

#Ejercicio 2
nombre=input("Como te llamás?")
print("Hola", nombre)

#Ejercicio 3
nombre=input("Nombre?")
apellido=input("Apellido?")
edad=int(input("edad?"))
residencia=input("Lugar de residencia?")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Ejercicio 4
import math
pi_value=math.pi

radio=int(input("Radio del circulo?"))
area= pi_value * (radio**2)
perimetro=2*pi_value*radio
print(f"El area es de {area} cm y el perimetro es de {perimetro} cm")

#Ejercicio 5
segundo=int(input("Cuantos segundos"))
print("Equivale a", ((segundo/60)/60), "horas")

#siempre es buena practica agregar los :type a la definicion de variables
#numero: int=int(input())

#Ejercicio 6
numero=int(input("numero para escribir la tabla de multiplicacion?"))
print(numero, "* 1 =", numero*1)
print(numero, "* 2 =", numero*2)
print(numero, "* 3 =", numero*3)
print(numero, "* 4 =", numero*4)
print(numero, "* 5 =", numero*5)
print(numero, "* 6 =", numero*6)
print(numero, "* 7 =", numero*7)
print(numero, "* 8 =", numero*8)
print(numero, "* 9 =", numero*9)
print(numero, "* 10 =", numero*10)

#Ejercicio 7
num1=int(0)
num2=int(0)

while num1<=0 or num2<=0:
    num1 :int =int(input("num1: "))
    num2 :int =int(input("num2: "))

print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)

#Ejercicio 8
altura= float(input("ingrese su altura en CM: "))
altura=altura/100
print(altura)
peso :int = int(input("ingrese su peso: "))
imc = float(peso/(altura**2))

print(f"El indice de masa corporal es {imc}")

#Ejercicio 9

celsius=int(input("celsius: "))
fahrenheit=int((celsius*1.8)+32)
print("Los grados en fahrenheit son: ", fahrenheit)


#Ejercicio 10

num1=int(input("num1: "))
num2=int(input("num2: "))
num3=int(input("num3: "))
promedio=((num1+num2+num3)*3)

print("El promedio de dichos numeros es: ", promedio)