escursiones :list=[]
cupos :list=[]

bandera :bool=True

while bandera:
    print('''
          Bienvenido al Gestor de Turismo, ingrese la opcion deseada:
          1) Ingresar Excursion
          2) Ingresar Cupo por Excursion
          3) Mostrar Oferta/Cupo
          4) Consultar Cupo por nombre de excursion
          5) Listar excursiones con cupo
          6) Agregar Excursion
          7) Ver Excursiones sin Cupo
          8) Actualizar Cupos
          9) Ver todas las Excursiones
          10) Salir
          ''')
    opcion :str=input()
    if opcion=="1":
        agregar_escursion :bool=True
        while agregar_escursion:
            excursion: str=input("Ingrese nombre de la excursion: ")
            excursion=excursion.strip().upper()
            escursiones.append(excursion)
            continuar: str=input(f"Excursion {excursion} agregada con exito, desea agregar otra excursion? S/N ")
            if continuar.upper() =="N":
                agregar_escursion=False
            
    elif opcion=="2":
        for i in range(len(escursiones)):
            cupo: int=int(input(f"Ingrese un numero entero para indicar el cupo de la excursion {escursiones[i]}: "))
            if cupo<=0:
                cupo=0
                cupos.append(cupo)
            else:
                cupos.append(cupo)
            print(f"Cupo {cupo} agregado con exito para la excurcion {escursiones[i]}")
            
    elif opcion=="3":
        for i in range(len(escursiones)):
            print(f"La escursion: {escursiones[i]} dispone de {cupos[i]} cupos")
    elif opcion=="4":
        excursion_buscada :str=input("Ingrese la excursion buscada: ")
        excursion_buscada=excursion_buscada.strip().upper()
        if excursion_buscada in escursiones:
            cont :int=0
            encontrado :bool=False
            while not encontrado:
                if escursiones[cont]==excursion_buscada:
                    print(f"La excursion {excursion_buscada} tiene {cupos[cont]} cupos disponibles")
                    encontrado=True
                cont+=1
    elif opcion=="5":
        
            for i in range(len(cupos)):
                if not cupos[i]==0:
                    print(f"La excursion {escursiones[i]} tiene {cupos[i]} cupos disponibles")
        
    elif opcion=="6":
        agregar_escursion :bool=True
        while agregar_escursion:
            excursion: str=input("Ingrese nombre de la excursion: ")
            escursiones.append(excursion.strip().upper())
            cupo :int=int(input("Ingrese el cupo disponible para la excursion"))
            if cupo<=0:
                cupos.append(0)
            else:
                cupos.append(cupo)
            continuar: str=input(f"Excursion {excursion} con {cupo} cupo disponible, agregada con exito, desea agregar otra excursion? S/N ")
            if continuar.upper() =="N":
                agregar_escursion=False
    elif opcion=="7":
        if 0  in cupos:
            for i in range(len(cupos)):
                if  cupos[i]==0:
                    print(f"La excursion {escursiones[i]} no tiene cupos disponibles")
        else:
            print("No hay excursiones sin cupo disponibles")
    elif opcion=="8":
        excursion :str=input("Ingrese el nombre de la excursion a la que desea modificar el cupo: ")
        excursion=excursion.strip().upper()
        if excursion in escursiones:
            cont :int=0
            encontrado :bool=False
            while not encontrado:
                if escursiones[cont]==excursion:
                    cupo :int= int(input(f"Ingrese el nuevo cupo de la excursion {excursion}: "))
                    if cupo<=0:
                        cupos[cont]=0
                    else:
                        cupos[cont]=cupo
                    encontrado=True
                cont+=1
    elif opcion=="9":
        for i in range(len(escursiones)):
            print(f"La excursion {escursiones[i]} tiene {cupos[i]} cupos disponibles.")
    elif opcion=="10":
        bandera=False
        print("Adios.....")
    else:
        print("La opcion ingresada no es correcta, ingrese una opcion valida.")