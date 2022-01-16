
"""    Ejercicio 5:
• Crea un programa que pida por teclado introducir una contraseña. La contraseña no
podrá tener menos de 8 caracteres ni espacios en blanco. Si la contraseña es correcta,
el programa imprime “Contraseña OK”. En caso contrario imprime “Contraseña
errónea"
"""

password = input('Introduce la contraseña: ')

if(' ' in password) or len(password) < 8:
    print('La contraseña no puede contener espacios en blanco o menos de 8 caracteres')
else:
    print('La contraseña es correcta')
