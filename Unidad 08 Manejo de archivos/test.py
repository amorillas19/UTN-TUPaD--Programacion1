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

#Ejercicio 4

lista_diccionario = []

for item in lista_productos:
    item=item.strip().split(",")
    producto_d={}
    producto_d["nombre"]=item[0]
    producto_d["precio"]=item[1]
    producto_d["cantidad"]=item[2]
    lista_diccionario.append(producto_d)

print(lista_diccionario)

#Ejercicio 5

nombre_buscar :str = input("Ingrese el nombre del producto a buscar: ")
flag :bool = False
 
for item in lista_diccionario:
    
    if  nombre_buscar == item["nombre"]:
        print (item)
        flag = True

if flag == False:
        print ("El item no está en la lista")   
     

#Ejercicio 6

with open ("ejer1-productos.txt", "w") as archivo:
     
    for item in lista_diccionario:
        archivo.write(f"{item["nombre"]},{item["precio"]},{item["cantidad"]}\n")