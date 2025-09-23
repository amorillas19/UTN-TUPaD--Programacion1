#Ejercicio 1

lista_estudiantes=[6,4,7,8,9,6,4,10,2,7]

'''Lista completa'''
print(lista_estudiantes)

'''Promedio'''
for i in range (0,11):
    aux+=i
aux_promedio=aux/len(lista_estudiantes)

print(aux_promedio)

'''Nota Alta y baja'''

nota_baja=lista_estudiantes[0]
nota_alta=lista_estudiantes[0]

for i in range(0,10):
    if lista_estudiantes[i]>nota_alta:
        nota_alta=lista_estudiantes[i]
    if lista_estudiantes[i]<nota_baja:
        nota_baja=lista_estudiantes[i]

print("La nota mas baja es de: ", nota_baja)
print("La nota mas alta es de: ", nota_alta)

#Ejercicio 2

lista_productos=[]

for i in range(0,5):
    aux=input("Ingrese el nombre del producto que desea ingresar: ")
    lista_productos.append(aux)

'''Mostrar alfabeticamente'''
lista_productos.sort()

'''Eliminar, actualizar, y mostrar lista'''
aux_deleter=input("Que producto de la lista desea eliminar? ")
index=lista_productos.index(aux_deleter)
lista_productos.pop(index)
for i in range(0,len(lista_productos)):
    print(lista_productos[i])


#Ejercicio 3

import random

lista_numeros_azar=[]
lista_numeros_par=[]
lista_numeros_impar=[]

for i in range(0,16):
    lista_numeros_azar[i]=random.randint(1,100)

for i in range(0,16):
    if (lista_numeros_azar[i] % 2 == 0):
        lista_numeros_par.append(lista_numeros_azar[i])
    else:
        lista_numeros_impar.append(lista_numeros_azar[i])

print ("Lista AZAR")
print(lista_numeros_azar)
print ("Lista PAR")
print(lista_numeros_par)
print ("Lista IMPAR")
print(lista_numeros_impar)

#Ejercicio4

lista_repetidos=[1,3,5,3,7,1,9,5,3]
lista_sin_repetir=[]

for i in range(len(lista_repetidos)):
    if (not(lista_repetidos[i] in lista_sin_repetir)):
        lista_sin_repetir.append(lista_repetidos[i])

print(lista_sin_repetir)

