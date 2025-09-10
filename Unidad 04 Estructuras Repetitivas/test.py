<<<<<<< HEAD
numero_usuario=int(input("Por favor ingrese un numero entero para comenzar la suma. Ingrese 0 para finalizar: "))
suma_total=numero_usuario

while (numero_usuario != 0):
    numero_usuario=int(input("Por favor ingrese un numero entero para agregar a la suma. Ingrese 0 para finalizar: "))
    suma_total=suma_total+numero_usuario


print("La suma total de los enteros ingresados es: " , suma_total)
=======
#Ejercicio 10

numero_usuario=(int(input("Ingrese el numero, para invertir el orden de los digitos: ")))
numero_usuario=abs(numero_usuario)
numero_invertido=0

while(numero_usuario>0):
    digito=numero_usuario%10
    numero_invertido=(numero_invertido*10)+digito
    numero_usuario=numero_usuario//10

print(numero_invertido)
>>>>>>> 493d8fdfb73a30f42980f723091a28fc020fd1fc
