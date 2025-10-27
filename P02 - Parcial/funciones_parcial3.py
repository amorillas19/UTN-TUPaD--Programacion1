def validarPrecio(p_recibido):

    precio_check = True
    while precio_check:

        if not(p_recibido == ""):
            precio_float = p_recibido
            precio_float=precio_float.replace(".", "")
            print("PRECIO FLOAT", precio_float)

            if precio_float.isdigit() :
                p_recibido=float(p_recibido)

                if p_recibido>0:
                    print("Es un numero, y mayor a 0")
                    precio_check=False
                    return p_recibido
                    
            else:
                p_recibido :str = input("Tiene que ser un numero: ")         
        else:
            p_recibido :str = input("No puede ingresar un vacio: ")       

def mostrar_productos():
    lista_productos = []
    precio_total = 0

    with open ("productos.csv", "a+") as archivo:
        archivo.seek(0)
        lista_productos = archivo.readlines()
        
        if len(lista_productos) == 0:
            print("Productos.csv no existia. CREANDO... ")
            archivo.write(f"nombre,precio\n")

        else:
            for i in range (1,len(lista_productos)):
                lista_productos[i]=lista_productos[i].strip().split(",")
                
                lista_productos[i][1]=float(lista_productos[i][1])
                precio_total+=lista_productos[i][1]
                print(f"Producto: {lista_productos[i][0]}, precio ${lista_productos[i][1]}")

        print(f"PRECIO TOTAL: ${precio_total}")    


def agregar_productos():

    nombre_producto :str = input("Ingrese el nombre del producto: ").lower()
    if nombre_producto == "":
        while nombre_producto == "":
            nombre_producto :str = input("Por favor ingrese un nombre valido: ").lower()
    
    
    precio_producto :str = input("Ingrese el precio del producto: ")

    precio_producto = validarPrecio(precio_producto)      

    
    with open ("productos.csv", "a+") as archivo:
        archivo.write(f"{nombre_producto},{precio_producto}\n")

    print("Producto añadido")


def editar_productos():

    modificar_lista = []

    with open ("productos.csv", "r") as archivo: 
        modificar_lista = archivo.readlines()
        
        for i in range(1,len(modificar_lista)):
            modificar_lista[i]=modificar_lista[i].strip().split(",")

    print(modificar_lista)

    modificar_producto :str = input("Que producto se modifica: ").lower()

    if modificar_producto == "":
        while modificar_producto == "":
            modificar_producto :str = input("Por favor ingrese un nombre valido: ").lower()
    
    check_existencia :bool = False
    for i in range(len(modificar_lista)):
        
        if modificar_producto == modificar_lista[i][0]:
            print("Producto encontrado")
            check_existencia=True

            modificar_precio :str = input ("Ingrese el nuevo valor del producto: ")
            modificar_precio=validarPrecio(modificar_precio)
            modificar_lista[i][0]=modificar_producto
            modificar_lista[i][1]=modificar_precio
    
    if check_existencia == False:
        print ("El producto no se encuentra en la lista")

    with open ("productos.csv", "w") as archivo:
        archivo.write("nombre,precio\n")
        for i in range(1,len(modificar_lista)):
            archivo.write(f"{modificar_lista[i][0]},{modificar_lista[i][1]}\n")
        

def eliminar_productos():

    eliminar_lista = []

    with open ("productos.csv", "r") as archivo: 
        eliminar_lista = archivo.readlines()
        
        for i in range(len(eliminar_lista)):
            eliminar_lista[i]=eliminar_lista[i].strip().split(",")
    
    print("========LISTA INICIAL=========")
    print(eliminar_lista)

    eliminar_producto :str = input("Que producto se elimina: ").lower()

    if eliminar_producto == "":
        while eliminar_producto == "":
            eliminar_producto :str = input("Por favor ingrese un nombre valido: ").lower()

    check_existencia :bool = False
    indice_eliminar : int = 0

    for i in range(1,len(eliminar_lista)):
        if eliminar_producto == eliminar_lista[i][0]:
            print("Producto encontrado")
            check_existencia=True
            indice_eliminar = i
    
    if indice_eliminar!=0:
        eliminar_lista.pop(indice_eliminar)
    
    
    if check_existencia == False:
        print ("El producto no se encuentra en la lista")

    with open ("productos.csv", "w") as archivo:
        archivo.write("nombre,precio\n")
        for i in range(1,len(eliminar_lista)):
            archivo.write(f"{eliminar_lista[i][0]},{eliminar_lista[i][1]}\n")