#Ejercicio 1

for i in range (0,101):
    print (i)

#Ejercicio 2

numero_usuario=int(input("Ingrese un numero"))
contador=0

while(numero_usuario>0):
    numero_usuario=numero_usuario/10
    contador=contador+1

print(f"El numero {numero_usuario} tiene {contador} digitos")