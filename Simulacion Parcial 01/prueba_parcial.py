lista_libros=[]
lista_ejemplares=[]

opcion_usuario=0

while(opcion_usuario!=10):
    print("---------------")
    print("MENU:")
    print("1- Ingresar nombre del titulo")
    print("2- Ingresar cantidad de ejemplares del titulo")
    print("3- Mostrar catalogo de libros")
    print("4- Ingrese el libro a buscar")
    print("5- Listar libros con copias disponibles")
    print("6- Agregar titulo y sus copias")
    print("7- Ver titulos agotados")
    print("8- Actualizar ejemplares")
    print("9- Salir")
    opcion_usuario=input("Ingrese la opcion que desea utilizar: ")
    
    while(not(opcion_usuario.isdigit())):
          print("La opcion ingresada no es un numero")
          opcion_usuario=input("Ingrese la opcion que desea utilizar: ")

    opcion_usuario=int(opcion_usuario)

    
    if(opcion_usuario==1):
        aux_titulo=input("Por favor ingrese el nombre de la obra: ")
        aux_titulo=aux_titulo.lower()

        check_validacion=True

        for i in range(0, len(lista_libros)):
            if(aux_titulo==lista_libros[i]):
                check_validacion=False
            elif(aux_titulo==""):
                check_validacion=False

        if(check_validacion):
            print("El libro ha sido agregado a la lista")
            lista_libros.append(aux_titulo)
        else:
            print("El libro NO ha sido agregado a la lista")

    elif(opcion_usuario==2):
        aux_cantidad=int(input("Ingrese la cantidad de ejemplares: "))
        lista_ejemplares.append(aux_cantidad)

    elif(opcion_usuario==3):
        if(len(lista_ejemplares)==len(lista_libros)):
            for i in range(0, len(lista_libros)):
                print (lista_libros[i], ": ", lista_ejemplares[i], " copias")
            else:
                print("Las listas no son iguales")
        

    elif(opcion_usuario==4):
        aux_busqueda=(input("Ingrese el libro a buscar:"))
        aux_busqueda=aux_busqueda.lower()
        for i in range(0, len(lista_libros)):
            if(aux_busqueda==lista_libros[i]):
                print(lista_ejemplares[i], " copias disponibles")
            else:
                print("No esta en la lista")

    elif(opcion_usuario==5):
        for i in range(0, len(lista_ejemplares)):
                if(lista_ejemplares[i]>0):
                    print(lista_libros[i], "tiene stock")
                else:
                     print("NO tiene stock")

    elif(opcion_usuario==6):
        aux_nombre=input("Ingrese nombre de la obra: ")
        aux_ejemplares=int(input("Ingrese cantidad de ejemplares: "))
        lista_libros.append(aux_nombre)
        lista_ejemplares.append(aux_ejemplares)

    elif(opcion_usuario==7):
        for i in range(0, len(lista_ejemplares)):
            if(lista_ejemplares[i]==0):
                print(lista_libros[i], "NO tiene stock")

    elif(opcion_usuario==8):
        print("Que opcion desea utilizar?")
        print("A - Prestamo")
        print("B - Devolucion")
        opcion_prestamos=input("Que opcion desea utilizar?")
        opcion_prestamos=opcion_prestamos.lower()

        if(opcion_prestamos=="a"):
            aux_reemplazo=input("Que libro desea llevar en prestamo? ")
            aux_reemplazo=aux_reemplazo.lower()
            for i in range(0, len(lista_libros)):
                if(aux_reemplazo==lista_libros[i]):
                    if(lista_ejemplares[i]>0):
                        print("Se saca el libro")
                        print("-----------------")
                        lista_ejemplares[i]=lista_ejemplares[i]-1
                        print("Ahora quedan ", lista_ejemplares[i], " copias")
                    elif(lista_ejemplares[i]==0):
                        print("No quedan suficientes libros para prestar")              
        elif(opcion_prestamos=="b"):
            aux_reemplazo=input("Que libro desea devolver? ")
            aux_reemplazo=aux_reemplazo.lower()

            for i in range(0, len(lista_libros)):

                print("pasa por el bucle")
                
                if(aux_reemplazo==lista_libros[i]):
                    print("Se devuelve el libro")
                    print("-----------------")
                    lista_ejemplares[i]=lista_ejemplares[i]+1
                    print("Ahora quedan ", lista_ejemplares[i], " copias")
        else:
            print("Opcion incorrecta")
            break


    elif(opcion_usuario==9):
        print("Gracias")
        break

    else:
        print("No es una opcion valida")
    

