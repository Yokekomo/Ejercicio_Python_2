def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplica(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


while True:
    try:
        op1 = (int(input("Introduce el primer número: ")))
        op2 = (int(input("Introduce el segundo número: ")))
        break
    except ValueError:
        print('No ha introducido un valor numérico')

while True:
    try:
        operacion = input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

        if operacion == "suma":
            print(suma(op1, op2))
            break

        elif operacion == "resta":
            print(resta(op1, op2))
            break

        elif operacion == "multiplica":
            print(multiplica(op1, op2))
            break

        elif operacion == "divide":
            try:
                print(divide(op1, op2))
                break
            except ZeroDivisionError:
                print('No se puede dividir por zero')


    except:
        print("Operación no contemplada")



print("Operación ejecutada. Continuación de ejecución del programa ")