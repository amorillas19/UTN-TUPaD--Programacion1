#Ejercicio10

ventas=[[10,20,30,40],
        [5,10,15,20],
        [10000,2,3,4],
        [2,4,6,8],
        [3,5,7,9],
        [8,7,6,5],
        [120,200,100,500]
        ]
venta_producto=[]
ventas_totales=0
indice_ventas_totales=0
venta_mayor=0
indice_venta_producto=0


for numero in range(0,4):
    aux_venta=0
    for i in range(len(ventas)):
        aux_venta+=ventas[i][numero]
    venta_producto.append(aux_venta)
print(venta_producto)

for i in range(len(ventas)):
    aux_totales=0
    for j in range(4):
        aux_totales+=ventas[i][j]
    if(aux_totales>ventas_totales):
        ventas_totales=aux_totales
        indice_ventas_totales=i
print("El dia con mayores ventas fue el dia n°", indice_ventas_totales+1, "donde se vendieron ", ventas_totales ," productos")

for i in range(len(venta_producto)):
    if(venta_producto[i]>venta_mayor):
        venta_mayor=venta_producto[i]
        indice_venta_producto=i
print("El mas vendido fue el producto N°", indice_venta_producto+1)