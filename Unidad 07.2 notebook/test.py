#Ejercicio 5

frase_ejemplo="hola don pepito hola don jose"

lista_frase=frase_ejemplo.split()
set_frase={}

for i in lista_frase:
    set_frase.update(i)

print(set_frase)
