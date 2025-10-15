#Ejercicio 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melon': 3000, 'Uva':
1450}

precios_frutas['Naranja']=1200
precios_frutas['Manzana']=1500
precios_frutas['Pera']=2300

print("Ejercicio 1, lista original")
print(precios_frutas)
print("-------------------")

#Ejercicio 2

precios_frutas['Banana']=1300
precios_frutas['Manzana']=1700
precios_frutas['Melon']=2800

print("Ejercicio 2, lista modificada")
print(precios_frutas)
print("-------------------")

#Ejercicio 3
lista_llaves=precios_frutas.keys()

print("Ejercicio 3 Lista llaves")
print(lista_llaves)
print("-------------------")

#Ejercicio 4

diccionario_telefonos={}

while True:
    nombre=input("Ingrese el nombre: ")
    telefono=input("Ingrese el telefono: ")
    diccionario_telefonos[nombre]=telefono
    if (len(diccionario_telefonos)>4):
        break

nombre_busqueda=input("Ingrese el nombre de la persona que desea ubicar?")
if(diccionario_telefonos.get(nombre_busqueda)):
    print(f"El nombre {nombre_busqueda} tiene el telefono: {diccionario_telefonos[nombre_busqueda]}")
else:
    print(f"El nombre {nombre_busqueda} NO tiene telefono")

#Ejercicio 5

