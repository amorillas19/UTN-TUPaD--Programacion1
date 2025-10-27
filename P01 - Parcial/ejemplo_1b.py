titulos=[]
ejemplares=[]

menu_mostrar=True

while (menu_mostrar):
    print("MENU")
    print('''
          1- Ingresar titulos
          2- Ingresar ejemplares
          3- Mostrar catalogo
          4- Consultar disponibilidad
          5- Listar agotados
          6- Agregar titulo y ejemplares
          7- Actualizar ejemplares(prestamo/devolucion)
          8- Salir del menu''')
    
    opcion_usuario=int(input("Ingrese que opcion desea utilizar: "))

    
    if(opcion_usuario==1):
        menu_agregar=True

        while(menu_agregar):
            aux_name=(input("Ingrese el nombre de la obra: "))
            if(not(aux_name=="")):
                titulos.append(aux_name)
                decision_usuario=(input("Desea agregar otro libro? S/N"))
                decision_usuario=decision_usuario.upper()
                if(decision_usuario=="N"):
                    menu_agregar=False
                    print("Gracias!")
            else:
                print("El titulo no es valido, o esta vacio")

    
    elif(opcion_usuario==2):
        for i in range(0, len(titulos)):
            check_cantidad=True
            while(check_cantidad):
                print ("El libro", titulos[i], "cuantos ejemplares tiene: ")
                aux_cantidad=int(input())
                if(aux_cantidad>=0):
                    check_cantidad=False
                    ejemplares.append(aux_cantidad)
                    print("Cantidad de ejemplares agregada!")
                else:
                    print("No ha ingresado un numero de ejemplares valido")
    
    elif(opcion_usuario==3):
        for i in range (0, len(titulos)):
            print (f"Libro: {titulos[i]}. {ejemplares[i]} ejemplares")
    
    elif(opcion_usuario==4):
        aux_busqueda=(input("Ingrese el titulo de la obra: "))
        if aux_busqueda in titulos:
            aux_indice=titulos.index(aux_busqueda)
            print(f"La obra {titulos[aux_indice]} posee {ejemplares[aux_indice]} ejemplares")
        else:
            print("La obra no existe en la biblioteca")
    
    elif(opcion_usuario==5):
        for i in range(0, len(titulos)):
            if(ejemplares[i]==0):
                print(f"El titulo {titulos[i]} no posee ejemplares")
    
    elif(opcion_usuario==6):
        aux_doble_name=(input("Ingrese el nombre de la obra: "))
        
        if aux_doble_name in titulos:
            print("El titulo ingresado ya existe en la biblioteca.")
        else:
            print("Ingrese la cantidad de ejemplares: ")
            aux_doble_cantidad=(input("Ingrese la cantidad de ejemplares: "))
            titulos.append(aux_doble_name)
            ejemplares.append(aux_doble_cantidad)
    
    elif(opcion_usuario==7):
        opcion_movimiento=(input("Desea solicitar un prestamo, o hacer una devolucion"))

        if(opcion_movimiento=="prestamo"):
            aux_prestamo_libro=(input("Que titulo desea solicitar en prestamo: "))
            for i in range(0, len(titulos)):
                if(aux_prestamo_libro==titulos[i]):
                    print("El libro existe")
                    if(ejemplares[i]>=1):
                        ejemplares[i]-=1
                        print("El libro ha sido prestado con exito")
                        print("Cantidad de ejemplares restantes: ", ejemplares[i])
                    else:
                        print("No hay copias para llevar en prestamo")
        
        elif(opcion_movimiento=="devolucion"):
            aux_devolucion_libro=(input("Que titulo desea devolver: "))
            aux_devolucion_libro=aux_devolucion_libro.lower()
            if aux_devolucion_libro in titulos:
                print("El libro existe en la biblioteca")
                indice_libro=titulos.index(aux_devolucion_libro)
                ejemplares[indice_libro]+=1
                print("El libro ha sido devuelto con exito")
                print("Cantidad de ejemplares restantes: ", ejemplares[indice_libro])
            else:
                print("El titulo no se encuentra en la biblioteca")
        
        else:
            print("No ha ingresado una opcion valida")
    
    elif(opcion_usuario==8):
        break
    


print("Gracias")