#Ejercicio6

ejemplo=[1,2,3,4,5,6,7]


for i in range((len(ejemplo)-1), 0, -1):
    aux=ejemplo[i]
    ejemplo[i]=ejemplo[i-1]
    ejemplo[i-1]=aux
    
ejemplo[0]=aux

print(ejemplo)

