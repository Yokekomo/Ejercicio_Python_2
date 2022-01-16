"""
Par o impar
Lo primero que vamos a realizar es dar la bienvenida preguntando un número entre 1 y 1000
Cuando el usuario proporciona el número,
comprobaremos si es par o impar y después imprimimos el mensaje con el resultado.
Ejemplo:
Mensaje que se muestra: ¿En qué número estás pensando?
Entrada: 25
Salida: ¡Es un número impar! ¿Puedes añadir otro?
"""

print('Introduce un número entre 1 y 1000 para saber si es par o impar.')
contador = 0
while True:
    contador += 1
    if contador == 3:
        pregunta = input('¿Quieres salir? ')
        pregunta = pregunta.lower()
        contador = 0
        if pregunta == 'si':
            exit('Hasta la vista')
            break
    try:
        numero = int(input('¿En qué número estás pensando? '))
        if numero > 1000 or numero < 0:
            print('Tiene que ser un número entre 1 y 1000.')
        elif numero % 2 == 0:
            print('¡Es un número par! ¿Puedes añadir otro?')
        elif numero % 2 == 1:
            print('¡Es un número impar! ¿Puedes añadir otro?')
    except:
        print('Tiene que ser un número.')


