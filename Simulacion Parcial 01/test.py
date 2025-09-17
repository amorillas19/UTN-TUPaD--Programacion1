lista_libros=["primero", "segundo", "tercero", "cuarto"]
lista_ejemplares=[1, 3, 0, 15]

opcion_usuario=0

while(opcion_usuario!=10):
    print("---------------")
    print("MENU:")
    print("1- Ingresar nombre del titulo")
    print("2- Ingresar cantidad de ejemplares del titulo")
    print("3- Imprimir")
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
                print(lista_libros)
                print(lista_ejemplares)

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
            print("llega a entrar al bucle")
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

    else:
        print("No es una opcion valida")
