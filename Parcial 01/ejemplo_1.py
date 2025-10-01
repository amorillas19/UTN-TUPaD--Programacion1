titulos :list=["Harry potter","1984","El señor","Rebelion en la granja"]
ejemplares :list=[3,0,2,2]
bandera :bool=True


while bandera:
    print('''
          Bienbenido a la biblioteca UTN
          elija la opcion del menu que desea ejecutar
          1)Ingrsar lista titulos
          2)Ingresar lista de ejemplares
          3)Mostrar catálogo
          4)Consultar disponibilidad de un título específico
          5)Listar disponibles
          6)Agregar título
          7)Ver títulos agotados
          8)Actualizar ejemplares (préstamo/devolución)
          9)Salir
          ''')
    opcion :str=input("Ingrese la opcion del menu que desea ejecutar: ")
    
    if opcion=="1":
        bandera_titulo :bool=True
        while bandera_titulo:
            titulo :str=input("Ingrese el titulo del libro: ")
            titulo=titulo.upper()
            while titulo=="":
             print("El titulo no puede estar vacio, ingrese de nuevo el titulo")
             titulo=input("Ingrese el titulo del libro: ")
             titulo=titulo.upper()
            titulos.append(titulo)
            desicion :str=input("Desea agregar otro titulo? S/N")
            if desicion.lower()=="n":
                 bandera_titulo=False
        
    elif opcion=="2":
        for i in range(len(titulos)):
            print(f"El titulo del libro es : {titulos[i]}")
            numero_ejemplar :str=input("Ingrese el numero de ejemplar para este libro: ")
            while numero_ejemplar.isalpha() or int(numero_ejemplar)<0:
                print("El numero ingresado no es valido")
                numero_ejemplar=input("Ingrese el numero de ejemplar para este libro: ")
            ejemplares.append(int(numero_ejemplar))
            print(f"El libro {titulos[i]} tiene {ejemplares[i]} disponibles")
    elif opcion=="3":
        for i in range(len(titulos)):
             print(f"El libro {titulos[i]} tiene {ejemplares[i]} disponibles")
    elif opcion=="4":
        titulo_buscado :str=input("Ingrese el titulo buscado")
        titulo_buscado=titulo_buscado.upper()
        if titulo_buscado in titulos:
            for i in range(len(titulos)):
                if titulo_buscado==titulos[i]:
                    print(f"El titulo {titulo_buscado} tiene {ejemplares[i]} disponibles")
                    break
        else:
            print("El titulo ingresado no existe en la biblioteca")
                
    elif opcion=="5":
        if ejemplares.count(0)==len(ejemplares):
            print("No hay ejemplares disponibles en este momento")
        else:
            for i in range(len(titulos)):
                if ejemplares[i]>0:
                    print(f"El titulo {titulos[i]} tiene {ejemplares[i]} disponibles")
    elif opcion=="6":
         bandera_titulo :bool=True
         while bandera_titulo:
            titulo :str=input("Ingrese el titulo del libro: ")
            titulo=titulo.upper()
            while titulo=="":
             print("El titulo no puede estar vacio, ingrese de nuevo el titulo")
             titulo=input("Ingrese el titulo del libro: ")
             titulo=titulo.upper()
            titulos.append(titulo)
            numero_ejemplar :str=input("Ingrese el numero de ejemplar para este libro: ")
            while numero_ejemplar.isalpha() or int(numero_ejemplar)<0:
                print("El numero ingresado no es valido")
                numero_ejemplar=input("Ingrese el numero de ejemplar para este libro: ")
            ejemplares.append(int(numero_ejemplar))
            desicion :str=input("Desea agregar otro titulo? S/N")
            if desicion.lower()=="n":
                 bandera_titulo=False
    elif opcion=="7":
        if ejemplares.count(0)==0:
            print("No existen ejemplares agotados")
        else:
            for i in range(len(titulos)):
                if ejemplares[i]==0:
                    print(f"El titulo {titulos[i]} tiene {ejemplares[i]} disponibles")
    elif opcion=="8":
            titulo :str=input("Ingrese el titulo del libro: ")
            titulo=titulo.upper()
            if titulo in titulos:
                gestion :str=input("Que accion quiere realizar: Devolver o Retirar")
                gestion=gestion.lower()
                if gestion =="devolver":
                    indice_devolucion=titulos.index(titulo)
                    ejemplares[indice_devolucion]+=1
                    print(f"El titulo {titulo} ah sido devuelto con exito")
                else:
                    indice_retiro=titulos.index(titulo)
                    if ejemplares[indice_retiro]>0:
                        ejemplares[indice_retiro]-=1
                        print(f"El titulo {titulo} ah sido prestado con exito")
                    else:
                        print(f"No hay ejemplares disponibles actualmente para el titulo {titulo}")
            else:
                print(f"El titulo ingresado, {titulo} no existe en la biblioteca")
    elif opcion=="9":
        print("Adios......")
        bandera=False
    else:
        print("La opcion ingresada no es valida")