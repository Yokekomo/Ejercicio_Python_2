
"""    Ejercicio 6:
• Crea un programa que evalúe si una dirección de correo electrónico es válida o no en
función de si tiene “@” o “.” Hay que tener en cuenta que la dirección se considera
correcta si solo tiene una “@” y si tiene uno o más “."
"""

contador_arroba = 0
contador_punto = 0
email = 'albano@gmail.com'

for i in range(len(email)):
    if email[i] == '@':
        contador_arroba += 1
    if email[i] == '.':
        contador_punto += 1

if contador_arroba != 1 or contador_punto == 0:
    print('El email no es valido.')
else:
    print('Email correcto')

