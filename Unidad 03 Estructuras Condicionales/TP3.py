#Ejercicio 9

terremoto=float(input("ingrese la magnitud del terremoto: "))

if terremoto<3 and terremoto>0:
    print("muy leve")
elif terremoto>=3 and terremoto<4:
    print("leve")
elif terremoto>=4 and terremoto<5:
    print("moderado")
elif terremoto>=5 and terremoto<6:
    print("Fuerte")
elif terremoto>=6 and terremoto<7:
    print("Muy fuerte")
elif terremoto>7:
    print("extremo")
else:
    print("No es un valor que corresponde a la escala de Ritcher")