import random

numeros = list("0123456789")

nombresg = []
apellidosg = []
cedulag = []
usuariog = []
contraseñag = []

print("REGISTRO INICIAL DE LOS 10 USUARIOS DEL SISTEMA")
print(" ")

for us in range(1, 4):
    while True:
        print(f"ingrese los nombres del usuario # {us}: ")
        nombres = str(input()).strip()
        if nombres.replace(" ", "").isalpha() and nombres != "":
            break
        print("Nombres inválidos. Por favor, ingrese solo letras.")
        print(" ")

    while True:
        print(f"ingrese el apellido del usuario # {us}: ")
        apellido = str(input()).strip()
        if apellido.replace(" ", "").isalpha() and apellido != "":
            break
        print("Apellido inválido. Por favor, ingrese solo letras.")
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
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

    usuario_base = ""
    for palabra in nombres.split():
        usuario_base = usuario_base + palabra[0].upper()
    usuario_base = usuario_base + apellido.replace(" ", "").upper()

    usuario_generado = usuario_base
    contador = 2
    while usuario_generado in usuariog:
        usuario_generado = usuario_base + str(contador)
        contador = contador + 1

    while True:
        contraseña_generada = ""
        for i in range(6):
            contraseña_generada = contraseña_generada + random.choice(numeros)
        if contraseña_generada not in contraseñag:
            break

    nombresg.append(nombres)
    apellidosg.append(apellido)
    cedulag.append(cedula)
    usuariog.append(usuario_generado)
    contraseñag.append(contraseña_generada)

    print(f"Usuario generado: {usuario_generado}")
    print(f"contraseña generada: {contraseña_generada}")
    print(" ")

print(" ")
print("REGISTRO INICIAL COMPLETO")
print(" ")

while True:
    print("""MENU DE OPCIONES
1-VER LISTADO DE USUARIOS
2-ACTUALIZAR UN USUARIO
3-RECORDAR CONTRASEÑA
4-AGREGAR NUEVO USUARIO
5-SALIR""")
    try:
        opcion = int(input("ingrese su elección: "))
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")
        print(" ")
        continue

    if opcion not in (1, 2, 3, 4, 5):
        print("Opción inválida. Por favor, ingrese 1, 2, 3, 4 o 5.")
        print(" ")
        continue

    if opcion == 1:
        print(" ")
        print("===== LISTADO DE USUARIOS =====")
        for i in range(len(nombresg)):
            print(f"{i + 1}) Nombres: {nombresg[i]}, Apellido: {apellidosg[i]}, "
                  f"Cédula: {cedulag[i]}, Usuario: {usuariog[i]}, Contraseña: {contraseñag[i]}")
        print(" ")

    elif opcion == 2:
        while True:
            try:
                print("Ingrese la cédula del usuario que desea actualizar: ")
                cedula_buscar = int(input())
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")

        if cedula_buscar not in cedulag:
            print("No se encontró ningún usuario con esa cédula.")
            print(" ")
            continue

        indice = cedulag.index(cedula_buscar)

        while True:
            print(f"""¿Qué desea actualizar de {nombresg[indice]} {apellidosg[indice]}?
1-Nombres
2-Apellido
3-Cédula
4-Usuario
5-Contraseña
6-Cancelar""")
            try:
                sub_opcion = int(input("ingrese su elección: "))
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
                continue
            if sub_opcion not in (1, 2, 3, 4, 5, 6):
                print("Opción inválida. Por favor, ingrese un número entre 1 y 6.")
                continue
            break

        if sub_opcion == 1:
            while True:
                print("Ingrese los nuevos nombres: ")
                nuevo_valor = str(input()).strip()
                if nuevo_valor.replace(" ", "").isalpha() and nuevo_valor != "":
                    nombresg[indice] = nuevo_valor
                    print("Nombres actualizados.")
                    break
                print("Nombres inválidos. Por favor, ingrese solo letras.")

        elif sub_opcion == 2:
            while True:
                print("Ingrese el nuevo apellido: ")
                nuevo_valor = str(input()).strip()
                if nuevo_valor.replace(" ", "").isalpha() and nuevo_valor != "":
                    apellidosg[indice] = nuevo_valor
                    print("Apellido actualizado.")
                    break
                print("Apellido inválido. Por favor, ingrese solo letras.")

        elif sub_opcion == 3:
            while True:
                try:
                    print("Ingrese la nueva cédula: ")
                    nueva_cedula = int(input())
                    if not (8 <= len(str(nueva_cedula)) <= 11):
                        print("la cedula solo puede tener de 8 a 11 dijitos")
                        continue
                    if nueva_cedula in cedulag and nueva_cedula != cedulag[indice]:
                        print("Esa cédula ya está registrada en otro usuario.")
                        continue
                    cedulag[indice] = nueva_cedula
                    print("Cédula actualizada.")
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")

        elif sub_opcion == 4:
            while True:
                print("Ingrese el nuevo usuario: ")
                nuevo_usuario = str(input()).strip().upper()
                if nuevo_usuario == "":
                    print("El usuario no puede estar vacío.")
                    continue
                if nuevo_usuario in usuariog and nuevo_usuario != usuariog[indice]:
                    print("Ese usuario ya está en uso por otra persona.")
                    continue
                usuariog[indice] = nuevo_usuario
                print("Usuario actualizado.")
                break

        elif sub_opcion == 5:
            while True:
                print("Ingrese la nueva contraseña (6 dígitos): ")
                nueva_contraseña = str(input()).strip()
                if not nueva_contraseña.isdigit() or len(nueva_contraseña) != 6:
                    print("La contraseña debe tener exactamente 6 dígitos numéricos.")
                    continue
                if nueva_contraseña in contraseñag and nueva_contraseña != contraseñag[indice]:
                    print("Esa contraseña ya está en uso por otra persona.")
                    continue
                contraseñag[indice] = nueva_contraseña
                print("Contraseña actualizada.")
                break

        print(" ")

    elif opcion == 3:
        while True:
            try:
                print("Ingrese su número de documento: ")
                cedula_buscar = int(input())
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")

        if cedula_buscar in cedulag:
            indice = cedulag.index(cedula_buscar)
            print(f"Su contraseña es: {contraseñag[indice]}")
        else:
            print("No se encontró ningún usuario con esa cédula.")
        print(" ")

    elif opcion == 4:
        if len(nombresg) >= 10:
            print("El sistema ya tiene el máximo de 10 usuarios.")
            print(f"Para agregar uno nuevo se debe eliminar al primer usuario ingresado: "
                  f"{nombresg[0]} {apellidosg[0]} (usuario {usuariog[0]}).")
            while True:
                confirmar = input("¿Desea eliminarlo para poder registrar uno nuevo? (s/n): ").strip().lower()
                if confirmar in ("s", "n"):
                    break
                print("Respuesta inválida. Ingrese 's' o 'n'.")

            if confirmar == "n":
                print("Operación cancelada. No se agregó ningún usuario nuevo.")
                print(" ")
                continue

            nombresg.pop(0)
            apellidosg.pop(0)
            cedulag.pop(0)
            usuariog.pop(0)
            contraseñag.pop(0)
            print("Primer usuario eliminado.")
            print(" ")

        while True:
            print("ingrese los nombres del nuevo usuario: ")
            nombres = str(input()).strip()
            if nombres.replace(" ", "").isalpha() and nombres != "":
                break
            print("Nombres inválidos. Por favor, ingrese solo letras.")

        while True:
            print("ingrese el apellido del nuevo usuario: ")
            apellido = str(input()).strip()
            if apellido.replace(" ", "").isalpha() and apellido != "":
                break
            print("Apellido inválido. Por favor, ingrese solo letras.")

        while True:
            try:
                print("ingrese la cedula del nuevo usuario: ")
                cedula = int(input())
                if not (8 <= len(str(cedula)) <= 11):
                    print("la cedula solo puede tener de 8 a 11 dijitos")
                    continue
                if cedula in cedulag:
                    print("Esa cédula ya está registrada. Ingrese una diferente.")
                    continue
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")

        usuario_base = ""
        for palabra in nombres.split():
            usuario_base = usuario_base + palabra[0].upper()
        usuario_base = usuario_base + apellido.replace(" ", "").upper()

        usuario_generado = usuario_base
        contador = 2
        while usuario_generado in usuariog:
            usuario_generado = usuario_base + str(contador)
            contador = contador + 1

        while True:
            contraseña_generada = ""
            for i in range(6):
                contraseña_generada = contraseña_generada + random.choice(numeros)
            if contraseña_generada not in contraseñag:
                break

        nombresg.append(nombres)
        apellidosg.append(apellido)
        cedulag.append(cedula)
        usuariog.append(usuario_generado)
        contraseñag.append(contraseña_generada)

        print(f"Nuevo usuario registrado: {usuario_generado}")
        print(" ")

    elif opcion == 5:
        print("Saliendo del programa. ¡Hasta luego!")
        break
