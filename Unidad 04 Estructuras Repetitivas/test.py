#Ejercicio 10

numero_usuario=(int(input("Ingrese el numero, para invertir el orden de los digitos: ")))
numero_usuario=abs(numero_usuario)
numero_invertido=0

while(numero_usuario>0):
    digito=numero_usuario%10
    numero_invertido=(numero_invertido*10)+digito
    numero_usuario=numero_usuario//10

print(numero_invertido)