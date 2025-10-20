paises=["Argentina", "Puerto Rico", "Brasil", "Chile", "Argelia"]

pais_ingresado = input("Pais? ")
pais_ingresado = pais_ingresado.lower()
paises_encontrados=[]

for pais in paises:
    if pais_ingresado in pais.lower(): 
        paises_encontrados.append(pais)

print (paises_encontrados)