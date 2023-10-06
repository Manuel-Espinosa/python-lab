# Bucles en Python

Los bucles permiten ejecutar un bloque de código repetidamente mientras se cumple una condición. Los bucles más comunes en Python son el bucle `for` y el bucle `while`. Aquí tienes una descripción general de cómo funcionan:

## Bucle `for`:

El bucle `for` se utiliza para iterar sobre una secuencia (como una lista, una tupla, una cadena de texto o un rango) y ejecutar un bloque de código para cada elemento de la secuencia. La sintaxis básica es la siguiente:

for elemento in secuencia:
    # Código que se ejecuta para cada elemento

Por ejemplo, para iterar sobre una lista de números e imprimir cada número:

numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)

## Bucle `while`:

El bucle `while` se utiliza para ejecutar un bloque de código mientras se cumple una condición. La sintaxis básica es la siguiente:

while condicion:
    # Código que se ejecuta mientras la condición sea verdadera

Por ejemplo, para contar desde 1 hasta 5 utilizando un bucle `while`:

contador = 1
while contador <= 5:
    print(contador)
    contador += 1

## Control de bucles:

Dentro de los bucles, puedes usar palabras clave como `break` y `continue` para controlar el flujo del bucle.

- `break`: Se utiliza para salir del bucle por completo si se cumple una condición.

- `continue`: Se utiliza para saltar la iteración actual y pasar a la siguiente si se cumple una condición.

Por ejemplo, un bucle `for` que utiliza `break` para salir temprano si se encuentra un número par:

numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    if numero % 2 == 0:
        break
    print(numero)

Estos son los conceptos básicos de los bucles en Python. Puedes utilizar bucles para automatizar tareas que requieren repetición y procesamiento de datos.
