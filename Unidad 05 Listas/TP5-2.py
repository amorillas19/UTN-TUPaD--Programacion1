#Ejercicio 1

lista_estudiantes=[9,4,7,8,9,6,4,10,2,7]

'''Lista completa'''
print(lista_estudiantes)

'''Promedio'''
aux=0
for i in range (0,10):
    aux+=lista_estudiantes[i]
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

#Ejercicio 4

lista_repetidos=[1,3,5,3,7,1,9,5,3]
lista_sin_repetir=[]

for i in range(len(lista_repetidos)):
    if (not(lista_repetidos[i] in lista_sin_repetir)):
        lista_sin_repetir.append(lista_repetidos[i])

print(lista_sin_repetir)

#Ejercicio 5

lista_estudiantes=["Antonio", "Benjamin", "Carlos", "Damian", "Enzo", "Fausto", "German", "Hector"]

eleccion=str(input("Desea agregar o eliminar un estudiante: "))
eleccion=eleccion.lower()

if eleccion=="agregar":
    aux_new=str(input("Indique el nombre del estudiante a agregar: "))
    lista_estudiantes.append(aux_new)
elif eleccion=="eliminar":
    aux_remove=str(input("Indique el nombre del estudiante que desea remover: "))
    lista_estudiantes.remove(aux_remove)
else:
    print("La opcion es incorrecta")

print(lista_estudiantes)

#Ejercicio 6

ejemplo=[1,2,3,4,5,6,7]


for i in range((len(ejemplo)-1), 0, -1):
    aux=ejemplo[i]
    ejemplo[i]=ejemplo[i-1]
    ejemplo[i-1]=aux
    
ejemplo[0]=aux

print(ejemplo)

#Ejercicio7

temperaturas=[[5,12], [6,15], [3,20],[7,14],[10,30],[1,35],[1,15]]
suma_minimas=0
suma_maximas=0
amplitud_termica=0
dia_amplitud=0


for i in range (len(temperaturas)):
    suma_minimas+=temperaturas[i][0]
    suma_maximas+=temperaturas[i][1]

print("El promedio de temperaturas minimas es: ", suma_minimas/(len(temperaturas)))
print("El promedio de temperaturas maximas es: ",suma_maximas/(len(temperaturas)))

for i in range (len(temperaturas)):
    aux_amplitud=temperaturas[i][1]-temperaturas[i][0]
    if aux_amplitud>amplitud_termica:
        amplitud_termica=aux_amplitud
        dia_amplitud=i+1

print("El dia con mayor amplitud termina fue el día: ", dia_amplitud)
print("La amplitud termica fue de ", amplitud_termica, " grados")    

#Ejercicio8

notas_estudiantes=[[7,9,3],[8,10,8],[5,3,1],[1,4,2],[7,7,8]]
promedio_estudiantes=[]
promedio_materia=[]


for i in range(len(notas_estudiantes)):
    aux_sumatoria=0
    for j in range(3):
        aux_sumatoria+=notas_estudiantes[i][j]
        
    aux_sumatoria/=3    
    promedio_estudiantes.append(aux_sumatoria)

for i in range(len(promedio_estudiantes)):
    print("El promedio del estudiante N°", i+1, ": ", promedio_estudiantes[i])

for i in range(3):
    aux_materia=0
    for j in range(len(notas_estudiantes)):
        aux_materia+=notas_estudiantes[j][i]
    aux_materia/=5
    promedio_materia.append(aux_materia)


for i in range(len(promedio_materia)):
    print("El promedio de la materia N° ", i, "es de: ", promedio_materia[i])


#Ejercicio9

tablero_tateti=[["-","-","-"],["-","-","-"],["-","-","-"]]
contador_turnos=1

while(contador_turnos<10):
    
    if((contador_turnos%2)):
        jugador=1
        dibujo="x"
    else:
        jugador=2
        dibujo="0"

    print("Jugador N°", jugador)
    fila=int(input("Ingrese la fila: "))
    columna=int(input("Ingrese la columna: "))
    if(tablero_tateti[fila][columna]=="-"):
        tablero_tateti[fila][columna]=dibujo
        contador_turnos+=1
    else:
        print("La casilla ya está ocupada")

    print(tablero_tateti[0])
    print(tablero_tateti[1])
    print(tablero_tateti[2])

#Ejercicio10

ventas=[[10,20,30,40],
        [5,10,15,20],
        [10000,2,3,4],
        [2,4,6,8],
        [3,5,7,9],
        [8,7,6,5],
        [120,200,100,500]
        ]
venta_producto=[]
ventas_totales=0
indice_ventas_totales=0
venta_mayor=0
indice_venta_producto=0


for numero in range(0,4):
    aux_venta=0
    for i in range(len(ventas)):
        aux_venta+=ventas[i][numero]
    venta_producto.append(aux_venta)
print(venta_producto)

for i in range(len(ventas)):
    aux_totales=0
    for j in range(4):
        aux_totales+=ventas[i][j]
    if(aux_totales>ventas_totales):
        ventas_totales=aux_totales
        indice_ventas_totales=i
print("El dia con mayores ventas fue el dia n°", indice_ventas_totales+1, "donde se vendieron ", ventas_totales ," productos")

for i in range(len(venta_producto)):
    if(venta_producto[i]>venta_mayor):
        venta_mayor=venta_producto[i]
        indice_venta_producto=i
print("El mas vendido fue el producto N°", indice_venta_producto+1)
