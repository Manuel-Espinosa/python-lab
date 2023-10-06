#reto 1
suma = 0
for numero in range(2, 101, 2):
    suma += numero
print("La suma de los números pares del 1 al 100 es:", suma)

#reto 2

# Solicitar al usuario que ingrese dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Solicitar al usuario que seleccione una operación
operacion = input("Seleccione una operación (+, -, *, /): ")

# Realizar la operación seleccionada
if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: División por cero"
else:
    resultado = "Operación no válida"

# Imprimir el resultado
print("Resultado:", resultado)

#reto 3

import random

numero_aleatorio = random.randint(1, 100)
intentos = 0

while True:
    intento = int(input("Adivina el número (entre 1 y 100): "))
    intentos += 1

    if intento < numero_aleatorio:
        print("El número es mayor. Intenta de nuevo.")
    elif intento > numero_aleatorio:
        print("El número es menor. Intenta de nuevo.")
    else:
        print(f"¡Correcto! Adivinaste el número {numero_aleatorio} en {intentos} intentos.")
        break

#reto 4

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

for i in range(1, 11):
    producto = numero * i
    print(f"{numero} x {i} = {producto}")

#reto 5

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un número para calcular su factorial: "))

if numero < 0:
    print("El factorial no está definido para números negativos.")
else:
    resultado = factorial(numero)
    print(f"El factorial de {numero} es {resultado}")
