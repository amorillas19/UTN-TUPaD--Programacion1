#Ejercicio 01

def factorial(num):
    if num == 0:
        return 1
    else:
        return factorial(num-1)*num

numero = int(input("Ingresa un número entero positivo: "))
        
if numero > 1:
    print("Por favor, ingresa un número mayor o igual a 1")
    
    print(f"\nFactoriales desde 1 hasta {numero}:")
    
    # Calcular y mostrar factorial para cada número
    for i in range(1, numero + 1):
        resultado = factorial(i)
        print(f"{i}! = {resultado}")

else:
    print("Debe ingresar un numero entero positivo") 

#Ejercicio 02

def fibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def mostrar_fibonacci(posiciones):
    print(f"\nSerie de Fibonacci hasta la posición {posiciones}:")
    
    for i in range(posiciones + 1):
        valor = fibonacci(i)
        print(f"F({i}) = {valor}")

posicion = int(input("¿Hasta qué posición deseas ver la serie de Fibonacci? "))

mostrar_fibonacci(posicion)

print(f"\nEl valor en la posición {posicion} es: {fibonacci(posicion)}")
    
#Ejercicio 03

def potencia(base, exponente):
    
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)


def probar_potencia():

    print("PRUEBAS DE LA FUNCIÓN POTENCIA RECURSIVA")

    
    # Lista de casos de prueba
    casos_prueba = [
        (2, 3),    # 2^3 = 8
        (5, 2),    # 5^2 = 25
        (10, 0),   # 10^0 = 1
        (3, 4),    # 3^4 = 81
        (7, 1),    # 7^1 = 7
    ]
    
    print("\nCasos de prueba predefinidos:")
    print("-" * 60)
    for base, exp in casos_prueba:
        resultado = potencia(base, exp)
        print(f"{base}^{exp} = {resultado}")
    
    print("\n" + "=" * 60)


def main():
    probar_potencia()

    # Solicitar datos al usuario
    base = float(input("\nIngresa la base (o 'q' para salir): "))
    exponente = int(input("Ingresa el exponente (entero no negativo): "))
    
    # Validar exponente
    if exponente > 0:
        resultado = potencia(base, exponente)
        print(f"\nResultado: {base}^{exponente} = {resultado}")
    elif exponente < 0:
        print("Error: El exponente debe ser un entero no negativo")

#Ejercicio 04

def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

print("Conversión de Decimal a Binario")
print("=" * 40)


numero = int(input("\nIngresa un número decimal positivo: "))

if numero < 0:
    print("Por favor ingresa un número positivo")
else:
    binario = decimal_a_binario(numero)
    print(f"\nEl número {numero} en binario es: {binario}")
    print(f"Verificación con bin(): {bin(numero)[2:]}")            


#Ejercicio 05

def es_palindromo(palabra):
    palabra = palabra.lower()

    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    
    return es_palindromo(palabra[1:-1])


print("Verificador de Palíndromos")
print("=" * 50)

palabras_prueba = [
    "oso",
    "radar",
    "neuquen",
    "reconocer",
    "python",
    "anilina",
    "casa",
    "ala",
    "somos",
    "oro"
]

print("\nPruebas automáticas:")
print("-" * 50)
for palabra in palabras_prueba:
    resultado = es_palindromo(palabra)
    estado = "✓ ES palíndromo" if resultado else "✗ NO es palíndromo"
    print(f"{palabra:15} → {estado}")

print("Modo interactivo (escribe 'salir' para terminar)")

while True:
    palabra = input("\nIngresa una palabra: ")
    
    if palabra.lower() == "salir":
        print("¡Hasta luego!")
        break
    
    if es_palindromo(palabra):
        print(f"✓ '{palabra}' ES un palíndromo")
    else:
        print(f"✗ '{palabra}' NO es un palíndromo")

#Ejercicio 06

def suma_digitos(n):
    if n < 10:
        return n

    return (n % 10) + suma_digitos(n // 10)

print("Suma de Dígitos - Método Recursivo")

casos_prueba = [1234, 9, 305, 0, 99, 1000, 56789]

for numero in casos_prueba:
    resultado = suma_digitos(numero)
    print(f"suma_digitos({numero}) = {resultado}")

while True:
    entrada = input("\nIngresa un número positivo (o 'salir' para terminar): ")
    
    if entrada.lower() == "salir":
        print("¡Hasta luego!")
        break
    
    numero = int(entrada)
    
    if numero < 0:
        print("Por favor ingresa un número positivo")
    else:
        resultado = suma_digitos(numero)
        print(f"La suma de los dígitos de {numero} es: {resultado}")

#Ejercicio 07

def contar_bloques(n):
    if n == 1:
        return 1
    
    return n + contar_bloques(n - 1)


def visualizar_piramide(n):

    print(f"\nPirámide con base de {n} bloques:")
    print("-" * 40)
    
    for nivel in range(n, 0, -1):
        espacios = " " * (n - nivel) * 2
        bloques = "█ " * nivel
        print(f"{espacios}{bloques}")
    
    total = contar_bloques(n)
    print(f"\nTotal de bloques: {total}")

# Casos de prueba
casos_prueba = [1, 2, 3, 4, 5, 10]

print("\nPruebas automáticas:")
print("-" * 50)
for num in casos_prueba:
    resultado = contar_bloques(num)
    print(f"contar_bloques({num}) = {resultado}")


while True:
    entrada = input("\n¿Cuántos bloques tiene la base? (o 'salir'): ")
    
    if entrada.lower() == "salir":
        print("¡Hasta luego!")
        break
    
    n = int(entrada)
    
    if n <= 0:
        print("Por favor ingresa un número positivo")
    else:
        visualizar_piramide(n)

#Ejercicio 08

def contar_digito(numero, digito):
    
    if numero == 0:
        return 0
    
    ultimo_digito = numero % 10
    
    if ultimo_digito == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)


print("Contador de Dígitos en un Número")
print("=" * 50)

numero = int(input("\nIngresa un número: "))
digito = int(input("Ingresa el dígito a buscar (0-9): "))

resultado = contar_digito(numero, digito)
print(f"\nEl dígito {digito} aparece {resultado} veces en {numero}")