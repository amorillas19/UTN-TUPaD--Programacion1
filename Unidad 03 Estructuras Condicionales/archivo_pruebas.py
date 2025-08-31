palabra_usuario=(input("Ingrese una frase o palabra: "))
palabra_usuario=palabra_usuario.lower()
ultimo_caracter=(len(palabra_usuario)-1)
if (palabra_usuario[ultimo_caracter] == "a"):
    print (palabra_usuario+"!")
elif(palabra_usuario[ultimo_caracter] == "e"):
    print (palabra_usuario+"!")
elif(palabra_usuario[ultimo_caracter] == "i"):
    print (palabra_usuario+"!")
elif(palabra_usuario[ultimo_caracter] == "o"):
    print (palabra_usuario+"!")
elif(palabra_usuario[ultimo_caracter] == "u"):
    print (palabra_usuario+"!")
else:
    print(palabra_usuario)