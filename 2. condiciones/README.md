Condicionales en Python

Los condicionales en Python permiten controlar el flujo del programa basado en condiciones lógicas. Los condicionales más comunes son `if`, `elif` (opcional) y `else`. Aquí tienes una descripción general de cómo funcionan:

if (Si):

La instrucción `if` se usa para ejecutar un bloque de código si una condición es verdadera (True). La sintaxis básica es la siguiente:

if condicion:
    # Código que se ejecuta si la condición es verdadera

Por ejemplo:

edad = 18
if edad >= 18:
    print("Eres mayor de edad")

elif (Si no, si):

La instrucción `elif` se usa para verificar múltiples condiciones después de un `if`. Puedes tener cero o más bloques `elif` después de un `if`. La sintaxis es la siguiente:

if condicion1:
    # Código que se ejecuta si la condición1 es verdadera
elif condicion2:
    # Código que se ejecuta si la condición2 es verdadera
else:
    # Código que se ejecuta si ninguna de las condiciones anteriores es verdadera

Por ejemplo:

nota = 85
if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
else:
    print("C")

else (Sino):

La instrucción `else` se usa para ejecutar un bloque de código si la condición en el `if` o en el último `elif` no es verdadera. La sintaxis es la siguiente:

if condicion:
    # Código que se ejecuta si la condición es verdadera
else:
    # Código que se ejecuta si la condición no es verdadera

Por ejemplo:

edad = 15
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

Estos son los conceptos básicos de los condicionales en Python. Puedes anidar condicionales (`if` dentro de `if`) y usar operadores lógicos (como `and`, `or`, `not`) para crear condiciones más complejas.
