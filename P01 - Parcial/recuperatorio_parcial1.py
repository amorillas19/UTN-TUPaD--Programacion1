herramientas = []
existencias = []

flag_menu = True

while flag_menu:
    
  print('''Menu de opciones
        1- Ingresar herramientas
        2- Ingresar existencias
        3- Mostrar existencias
        4- Consultar disponibilidad
        5- Listar agotados
        6- Agregar herramienta
        7- Actualizar (Venta/Ingreso)
        8- Salir''')
  
  opcion : str = input("Ingrese que opcion desea utilizar: ")

  if opcion == "1":
    herramienta_agregar :str = input("Que herramienta desea agregar?").lower()

    if herramienta_agregar == "":
      print ("Ingreso invalido")
    else:
      print("Herramienta agregada") 
      herramientas.append(herramienta_agregar)
      existencias.append(0)
  


  elif opcion == "2":

    if (len(herramientas))==0:
      print("La lista de herramientas esta vacia, por favor ingrese una herramienta por lo menos.")

    else:
      for i in range(len(herramientas)):

        print(f"Herramienta: {herramientas[i]}")
        cantidad_agregar :str = input("Cuantas unidades desea agregar? ")

        if cantidad_agregar == "" or not(cantidad_agregar.isdigit()):
          print("No es un numero valido")

        else:
          cantidad_agregar = int(cantidad_agregar)
          existencias[i] = cantidad_agregar
          print("Cantidad agregada exitosamente")


  elif opcion == "3":
    for i in range(len(herramientas)):
      print(f"Herramienta: {herramientas[i]}. Stock: {existencias[i]} unidades")


  elif opcion == "4":
    herramienta_consultar :str = input("Ingrese la herramienta para averiguar stock: ").lower()

    if herramienta_consultar == "":
      print("Informacion no valida")
    elif herramienta_consultar in herramientas:
      indice_consultar=herramientas.index(herramienta_consultar)
      print(f"La herramienta {herramienta_consultar} posee {existencias[indice_consultar]} unidades")
    else:
      print("No existe en la lista")


  elif opcion == "5":

    if not(0) in existencias:
      print("No hay productos con 0 unidades")
    else: 
      for i in range(len(existencias)):
        if existencias[i] == 0 :
          print(f"La Herramienta: {herramientas[i]} NO posee existencias ({existencias[i]} unidades)")


  elif opcion == "6":
    nueva_herramienta : str = (input("Ingrese una nueva herramienta: ")).lower()

    if nueva_herramienta == "":
      print("Informacion no valida")

    else:

      if not(nueva_herramienta in herramientas):

        nueva_cantidad : str = input("Ingrese la cantidad: ")

        if nueva_cantidad == "" or not(nueva_cantidad.isdigit()):
          print ("No es un numero valido")
        else: 
          nueva_cantidad = int(nueva_cantidad)
          herramientas.append(nueva_herramienta)
          existencias.append(nueva_cantidad)


      else:
        print ("La herramienta ya existe en la lista")


  elif opcion == "7":
    print('''MENU DE ACTUALIZACION:
          1- Venta de herramientas
          2- Ingreso de herramientas''')
    opcion_actu :str = input("Ingrese el numero correspondiente a la opcion: ")

    if opcion_actu == "":
      print ("Opcion no valida")

    elif opcion_actu == "1":

      herramienta_venta :str = input("Cual herramienta desea vender? ").lower()
      if herramienta_venta == "":
        print("Opcion no valida")
      elif herramienta_venta in herramientas:
        print ("Herramienta encontrada")
        herramienta_i = herramientas.index(herramienta_venta)

        cantidad_venta : str = input("Cuantas herramientas desea vender?")

        if cantidad_venta == "" or not(cantidad_venta.isdigit()):
          print ("Valor no valido")
        else:
          cantidad_venta=int(cantidad_venta)

          if cantidad_venta>existencias[herramienta_i]:
            print("La cantidad ingresada supera al stock existente")
          else:
            existencias[herramienta_i]-=cantidad_venta
            print(f"La herramienta {herramientas[herramienta_i]} ahora tiene {existencias[herramienta_i]} unidades")

      else:
        print ("La herramienta no se encuentra en la lista")

    elif opcion_actu == "2":
      herramienta_ingreso :str = input ("Ingrese de que herramienta desea agregar unidades? ").lower()

      if herramienta_ingreso == "":
        print ("Opcion invalida")

      elif herramienta_ingreso in herramientas:
        print ("Herramienta encontrada")
        herramienta_j = herramientas.index(herramienta_ingreso)
        cantidad_ingreso :str = input("Cuantas unidades desea ingresar? ")

        if cantidad_ingreso == "" or not(cantidad_ingreso.isdigit()):
          print ("El valor ingresado no es correcto")

        else:
          cantidad_ingreso = int(cantidad_ingreso)
          existencias[herramienta_j]+=cantidad_ingreso
          print("INGRESO ACEPTADO")
          print(f"La herramienta {herramientas[herramienta_j]} ahora posee {existencias[herramienta_j]} unidades")

      else:
        print("La herramienta no se encuentra en la lista")

    else: 
      print ("Opcion no valida")

  elif opcion == "8":
    flag_menu = False 
    print("Gracias")

  else:
    print ("Opcion no valida")