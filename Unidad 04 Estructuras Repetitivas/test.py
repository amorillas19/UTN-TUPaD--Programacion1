numero_usuario=int(input("Por favor ingrese un numero entero para comenzar la suma. Ingrese 0 para finalizar: "))
suma_total=numero_usuario

while (numero_usuario != 0):
    numero_usuario=int(input("Por favor ingrese un numero entero para agregar a la suma. Ingrese 0 para finalizar: "))
    suma_total=suma_total+numero_usuario


print("La suma total de los enteros ingresados es: " , suma_total)