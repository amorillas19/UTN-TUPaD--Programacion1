from funciones_parcial3 import mostrar_productos, agregar_productos, editar_productos,  eliminar_productos

flag_menu = True

while flag_menu:
    print('''======MENU DE PRODUCTOS======
          1. Mostrar productos
          2. Agregar producto
          3. Editar precio de producto
          4. Eliminar producto
          5. Salir
          ==========================
          Seleccione una opcion: ''')
    
    opcion :str = input ("Seleccione una opcion: ")

    if opcion == "1":
        mostrar_productos()

    elif opcion == "2":
        agregar_productos()

    elif opcion == "3":
        editar_productos()

    elif opcion == "4":
        eliminar_productos()

    elif opcion == "5":
        print ("Gracias")
        flag_menu=False

    else:
        print("Opcion incorrecta")

    


