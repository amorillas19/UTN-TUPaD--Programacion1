#Ejercicio5

lista_estudiantes=["Antonio", "Benjamin", "Carlos", "Damian", "Enzo", "Fausto", "German", "Hector"]

eleccion=str(input("Desea agregar o eliminar un estudiante"))
eleccion=eleccion.lower()

if eleccion=="agregar":
    aux_new=str(input("Indique el nombre del estudiante a agregar: "))
    lista_estudiantes.append(aux_new)
elif eleccion=="eliminar":
    aux_remove=str(input("Indique el nombre del estudiante que desea remover: "))
    lista_estudiantes.
else:
    print("La opcion es incorrecta")
