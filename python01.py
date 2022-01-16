"""
Ejercicio 1:
• Crea un programa que pida dos números por teclado. El programa tendrá una función
llamada “DevuelveMax” encargada de devolver el número más alto de los dos
introducidos.
"""

numero1 = int(input('Introduce el primer número: '))
numero2 = int(input('Introduce el segundo número: '))


def devuelveMax(num1, num2):
    if num1 > num2:
        return f'El número {num1} es más alto que el numero {num2}.'
    elif num1 < num2:
        return f'El número {num2} es más alto que el numero {num1}.'
    else:
        return 'Los números introducidos son iguales.'


print(devuelveMax(numero1, numero2))