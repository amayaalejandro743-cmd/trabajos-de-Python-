import random

letras = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
numeros = list("0123456789")

nombreg = []
cedulag = []
usuariog = []
contraseñag = []

for us in range(1, 3):
    while True:
        print(f"ingrese el nombre del usuario # {us}: ")
        nombre = str(input()).strip()
        if nombre.replace(" ", "").isalpha() and nombre != "":
            nombreg.append(nombre)
            break
        print("Nombre inválido. Por favor, ingrese solo letras.")
        print(" ")

    while True:
        try:
            print(f"ingrese la cedula del usuario # {us}: ")
            cedula = int(input())
            if not (8 <= len(str(cedula)) <= 11):
                print("la cedula solo puede tener de 8 a 11 dijitos")
                print(" ")
                continue
            if cedula in cedulag:
                print("Esa cédula ya está registrada. Ingrese una diferente.")
                print(" ")
                continue
            cedulag.append(cedula)
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

    while True:
        usuario_generado = ""
        for i in range(4):
            usuario_generado = usuario_generado + random.choice(letras)
        if usuario_generado not in usuariog:
            usuariog.append(usuario_generado)
            break

    while True:
        contraseña_generada = ""
        for i in range(4):
            contraseña_generada = contraseña_generada + random.choice(numeros)
        if contraseña_generada not in contraseñag:
            contraseñag.append(contraseña_generada)
            break

for i in range(len(nombreg)):
    print(f" se le asigna a {nombreg[i]} identificado con cedula {cedulag[i]} "
          f"el usuario es {usuariog[i]} y contraseña {contraseñag[i]} ")
