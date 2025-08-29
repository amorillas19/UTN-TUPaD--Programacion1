import random

numeroElegido=int(random.randint(0,101))
print(numeroElegido)

flag : bool = bool(True)
flagInterna : bool = bool (True)
contadorIntentos : int=int(1)




while(flag==True):
    
    print("Adivine el numero:")

    while(flagInterna==True):
        numeroUsuario=(input())
        if(isinstance(numeroUsuario, int)):
            flagInterna==False
            print("paso por aca")

    if (numeroUsuario==numeroElegido):
        print("correcto")
        print("Acertaste en ", contadorIntentos, " intentos")
        flag=False
    elif(numeroUsuario>numeroElegido):
        print("El numero debe ser mas chico")
        contadorIntentos+=1
    elif(numeroUsuario<numeroElegido):
        print("El numero debe ser mas grande")
        contadorIntentos+=1

