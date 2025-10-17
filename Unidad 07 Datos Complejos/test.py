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