#Ejercicio 1

for i in range (4, 101, 4):
    print (i)

#Ejercicio 2

lista=["hola", True, 5.3, 69, "a"]
print (lista[3])

#Ejercicio 3

lista2=[]
lista2.append("chau")
lista2.append("adios")
lista2.append("bye")

print(lista2)

#Ejercicio 4

animales=["perro", "gato", "conejo", "pez"]
animales[2]="loro"
animales[3]="oso"
print(animales)

#Ejercicio 5

numeros=[8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

#La funcion max(numeros) se encarga de recorrer la lista y buscar el numero de mayor valor
#Por lo tanto, si utilizamos la funcion remove, buscando el numero de mayor valor, lo va a remover de la lista
#En este caso, el numero 22 seria el removido

#Ejercicio 6

lista_6=[]
for i in range (10, 31, 5):
    lista_6.append(i)

print(lista_6[0], lista_6[1])

#Ejercicio 7
autos=["sedan", "polo", "suran", "gol"]
autos[1]="coupe"
autos[2]="descapotable"

#Ejercicio 8

dobles=[]
for i in range(5,16, 5):
    aux=i*2
    dobles.append(aux)

print(dobles)

#Ejercicio 9

compras=[["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1]="tallarines"
compras[0].remove("pan")

print(compras)


#Ejercicio 10

lista_anidada=[15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)