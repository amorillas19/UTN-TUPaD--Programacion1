#Ejercicio 5

frase="hola don pepito hola don jose"

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
