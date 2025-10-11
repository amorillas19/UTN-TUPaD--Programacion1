#Ejercicio10

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