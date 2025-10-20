#Ejercicio 1/2

lista_productos = []

with open ("ejer1-productos.txt", "r") as archivo:
    lista_productos = archivo.readlines()
    for linea in lista_productos:
        linea = linea.strip()
        linea = linea.split(",")
        print (f"Producto: {linea[0].capitalize()} / Precio: ${linea[1]} / Cantidad: {linea[2]}")

 #Ejercicio 3
 
with open ("ejer1-productos.txt", "a") as archivo:
    producto :str = input("Ingrese el producto: ").capitalize()
    precio :str = input("Ingrese el precio")
    cantidad :str = input("Ingrese la cantidad")
    archivo.write(f"{producto},{precio},{cantidad}\n")