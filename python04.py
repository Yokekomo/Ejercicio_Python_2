
"""    Ejercicio 4:
• Crea un programa que muestre los números impares del 1 al 100. Los números deberán
aparecer una al lado del otro sin salto de línea.
"""

for i in range(1, 100):
    if i % 2 == 1:
        print(i, end=' ')
