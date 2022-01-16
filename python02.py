"""
Ejercicio 2:
• Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos
deberán ser almacenados en una lista y mostrar en consola el mensaje: “Los datos
personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por
teclado)
"""

nombre = input('Introduce un nombre: ')

direccion = input('Introduce una dirección: ')

tfno = input('Introduce un teléfono: ')

lista = [nombre, direccion, tfno]

print("Los datos personales son: " + lista[0] + " " + lista[1] + " " + lista[2])

