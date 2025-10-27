import os

herramientas = []
existencias = []

flag_menu :bool = True

while flag_menu:
    
    print('''Menu de opciones:
      1- Ingresar herramientas: 
      2- Ingresar existencias por herramientas: 
      3- Mostrar existencias de herramientas: 
      4- Consultar disponibilidad de una herramienta: 
      5- Listar herramientas agotadas: 
      6- Agregar herramienta y cantidad inicial: 
      7- Actualizar existencias (venta/ingreso)
      8- Salir''')
    
    opcion :str = input("Ingrese que opcion desea utilizar: ")

    if opcion == "1":
            
            herramienta_ingresada :str = input("Ingrese el nombre de la herramienta.").lower()

            if herramienta_ingresada == "":
                print ("Por favor ingrese un nombre valido de herramienta.")

            else:
                print ("Herramienta agregada exitosamente.")
                herramientas.append (herramienta_ingresada)
                existencias.append (0)
        
    
    elif opcion == "2":
        if len(herramientas)>0:

            for i in range(len(herramientas)):

                print(f"Herramienta: {herramientas[i]}.\n")
                cantidad_ingresada :str = (input())

                if cantidad_ingresada == "" or cantidad_ingresada.isalpha():
                    print("No ha hecho un ingreso valido. Por favor ingrese numeros")
                else:
                    existencias[i]=int(cantidad_ingresada)

        else:
            print("No hay herramientas en stock para agregar existencias. ")        

    elif opcion == "3":
        for i in range(len(herramientas)):
            print (f"Herramienta: {herramientas[i]}. Cantidad: {existencias[i]}")

    elif opcion == "4":
        herramienta_consultada :str = input(("Sobre que herramienta deseas consultar? ")).lower()
        print(herramienta_consultada)
        if herramienta_consultada in herramientas:
            print ("Herramienta encontrada. ")
            for i in range(len(herramientas)):
                if herramienta_consultada == herramientas[i]:
                    print (f"Cantidad: {existencias[i]}")
        else:
            print("La herramienta no ha sido ingresada")


    elif opcion == "5":
        for i in range (len(herramientas)):
            if existencias[i] == 0:
                print(f"La herramienta {herramientas[i]} tiene 0 existencias")
                

    elif opcion == "6":
        herramienta_sumar :str = (input("Ingrese la herramienta que desea agregar: ")).lower()

        if herramienta_sumar == "":
            print ("Por favor ingrese un nombre valido de herramienta.")

        else:
            if herramienta_sumar in herramientas:
                print("La herramienta ya existe en la lista")

            else:
                print ("Herramienta agregada exitosamente.")
                cantidad_sumar : str = (input("Ingrese la cantidad de herramientas: "))

                if cantidad_sumar == "" or cantidad_sumar.isalpha():
                    print("No ha ingresado un numero valido")
                else:
                    print("Cantidad de herramientas exitosamente agregadad.")
                    herramientas.append(herramienta_sumar)
                    existencias.append(int(cantidad_sumar))
            


    elif opcion == "7":

        print('''Que desea realizar?:
              A- Ingresar la venta de herramientas:
              B- Ingresar la recepcion de herramientas: ''')
        vi_opcion = (input("Ingrese la opcion que desea realizar: ")).lower()

        if vi_opcion == "":
            print("Por favor ingrese una opcion valida")

        elif vi_opcion == "a":
            venta_herramienta :str = input("De que herramienta desea vender? ")

            if venta_herramienta in herramientas:

                indice_venta=herramientas.index(venta_herramienta)

                venta_cantidad : str =input("Cuantas unidades desea vender?")

                if venta_cantidad == "" or venta_cantidad.isalpha():
                    print ("No ha ingresado un numero valido")
                else:
                    venta_cantidad = int(venta_cantidad)
                    
                    if (existencias[indice_venta]-venta_cantidad) < 0:
                        print ("No pueden venderse mas existencias de las disponibles")
                    else:
                        existencias[indice_venta]-=venta_cantidad
                        print(f"Ahora quedan {existencias[indice_venta]} ejemplares")

            else:
                print("La herramienta no existe")


        elif vi_opcion == "b":
            ingreso_herramienta :str = input("De que herramienta desea ingresar existencias? ")

            if ingreso_herramienta in herramientas:

                indice_ingreso=herramientas.index(ingreso_herramienta)

                ingreso_cantidad : str = input("Cuantas unidades desea ingresar? ")

                if ingreso_cantidad == "" or ingreso_cantidad.isalpha():
                    print ("No ha ingresado un numero valido")
                else:
                    ingreso_cantidad = int(ingreso_cantidad)
                    existencias[indice_ingreso]+=ingreso_cantidad
                    print(f"Ahora quedan {existencias[indice_ingreso]} ejemplares")

        else:
            print("La opcion ingresada no era valida.")

    elif opcion == "8":
        print ("Gracias")
        flag_menu=False

    else: 
        print ("no es una opcion valida")

    print ("\n")
    print ("\n")       
             