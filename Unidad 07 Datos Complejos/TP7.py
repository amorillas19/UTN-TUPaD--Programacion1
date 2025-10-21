#Ejercicio 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melon': 3000, 'Uva':
1450}

precios_frutas['Naranja']=1200
precios_frutas['Manzana']=1500
precios_frutas['Pera']=2300

print("Ejercicio 1, lista original")
print(precios_frutas)
print("-------------------")

#Ejercicio 2

precios_frutas['Banana']=1300
precios_frutas['Manzana']=1700
precios_frutas['Melon']=2800

print("Ejercicio 2, lista modificada")
print(precios_frutas)
print("-------------------")

#Ejercicio 3
lista_random=precios_frutas.keys()

print("Ejercicio 3 Lista llaves")
print(lista_random)
print("-------------------")

#Ejercicio 4

diccionario_telefonos={}

while True:
    nombre=input("Ingrese el nombre: ")
    telefono=input("Ingrese el telefono: ")
    diccionario_telefonos[nombre]=telefono
    if (len(diccionario_telefonos)>4):
        break

nombre_busqueda=input("Ingrese el nombre de la persona que desea ubicar?")
if(diccionario_telefonos.get(nombre_busqueda)):
    print(f"El nombre {nombre_busqueda} tiene el telefono: {diccionario_telefonos[nombre_busqueda]}")
else:
    print(f"El nombre {nombre_busqueda} NO tiene telefono")

#Ejercicio 5

frase=input("Ingrese una frase")

#Set de palabras unicas
palabras_unicas=frase.split()
set_random=set(palabras_unicas)
print(set_random)

#Recuento de palabras en la frase
repetidas=frase.split()
diccionario_repetidas={}

for i in repetidas:
    contador=int(repetidas.count(i))
    diccionario_repetidas[i]=contador

print(diccionario_repetidas)

#Ejercicio 6

diccionario_alumnos={}
for i in range(3):
    nombre=input("Ingrese el nombre del alumno: ")
    list=[]
    for j in range(3):
        numero=float(input("Ingrese la nota: "))
        list.append(numero)
    tupla=tuple(list)
    diccionario_alumnos[nombre]=tupla


for i in diccionario_alumnos:
    promedio=0
    for j in range(3):
        promedio+=diccionario_alumnos[i][j]
    print(f"La nota promedio de {i} es de: {promedio/3}") 

#Ejercicio 7

parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7, 8}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

#Ejercicio 8

supermercado={"manzana": 700, "banana":500, "huevo":120, "fideos":1000}
flag_menu :bool = True

while flag_menu:
    print('''Que desea hacer?
          1-Consultar stock de un producto
          2- Agregar cantidad de stock a un producto
          3- Agregar producto al supermercado.
          4- Salir:''')
    opcion = input()

    if (opcion == "1"):  
        stock_consulta=input("De que producto deseas consultar stock? ")
        while(not(stock_consulta.isalpha())):
            stock_consulta=input("Ingreso invalido. De que producto deseas consultar stock? ")
        stock_consulta.lower()
        if stock_consulta in supermercado:
            print(supermercado[stock_consulta])
        else:
            print("El producto no existe")

    if (opcion == "2"): 
        stock_agregar :str = input("De que producto deseas agregar stock? ")
        while (not (stock_agregar.isalpha())):
                stock_agregar=input("Ingreso invalido. De que producto deseas agregar stock? ")
        stock_agregar.lower()
        if stock_agregar in supermercado:
            cantidad_agregar :str = input("Cuantas unidades desea agregar al stock? ")
            if (not (cantidad_agregar.isdigit())):
                while (not (cantidad_agregar.isdigit())):
                    cantidad_agregar = input("Debe ingresar un numero valido por favor: ")
            else:
                integer_agregar :int = int(cantidad_agregar)
                supermercado[stock_agregar] += integer_agregar
                print (f"La cantidad de stock ha sido actualizada. Ahora el producto {stock_agregar} tiene {supermercado[stock_agregar]} unidades")
        else:
                print ("El producto no existe")

    if (opcion == "3"): 
        producto_agregar :str = input("Que producto desea agregar al supermercado? ")
        while (not (producto_agregar.isalnum())):
            print ("Nombre invalido, por favor ingreselo correctamente: ")
        if producto_agregar in supermercado:
            print ("Producto ya existente")
        else:
            print("El producto no está en el supermercado.")
            producto_cantidad = input("Que cantidad tiene el producto a agregar? ")
            while (not(producto_cantidad.isdigit())):
                producto_cantidad = input("Cantidad no valida. Por favor ingrese la cantidad del producto a agregar: ")
            producto_cantidad :int = int (producto_cantidad)
            supermercado[producto_agregar] = producto_cantidad
            print ("Producto agregado exitosamente")
            print (supermercado)
    
    if (opcion == "4"):
        print("Gracias!")
        flag_menu=False

    else:
        print ("Opcion no valida")

#Ejercicio 9

agenda = {("lunes","13"):"Reunion", 
          ("martes","15"):"Asado", 
          ("jueves","20"):"Viaje", 
          ("viernes","10"):"Despedida"}

dia = input("En que dia desea consultar la actividad? ").lower()
hora = input("En que hora se realizará la actividad? ")

tupla_busqueda = (dia, hora)

if tupla_busqueda in agenda:
    print (agenda[tupla_busqueda])
else:
    print ("No hay actividades para ese dia y horario")

#Ejercicio 10

original = {"Argentina": "Buenos aires", 
            "Brasil": "Brasilia", 
            "Chile":"Santiago", 
            "Colombia": "Bogota"}

invertido = {}

for i in original:
    key=original[i]
    value=i
    tupla=(key, value)
    invertido.update({tupla})

print(invertido)
