numero_usuario=int(input("Ingrese un numero"))
contador=0

while(numero_usuario>0):
    numero_usuario=numero_usuario//10
    contador=contador+1

print(f"El numero tiene {contador} digitos")