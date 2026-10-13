mascotas = {
    "M001": {
        "nombre": "Max",
        "especie": "perro",
        "edad": 3,
        "adoptada": False
    },
    "M002": {
        "nombre": "Luna",
        "especie": "gato",
        "edad": 2,
        "adoptada": False
    },
    "M003": {
        "nombre": "Rocky",
        "especie": "perro",
        "edad": 5,
        "adoptada": True
    },
    "M004": {
        "nombre": "Michi",
        "especie": "gato",
        "edad": 1,
        "adoptada": False
    },
    "M005": {
        "nombre": "Coco",
        "especie": "conejo",
        "edad": 2,
        "adoptada": False
    }
}




opcion = 0

while opcion != 9:
    print("===== REFUGIO DE MASCOTAS =====")
    print("1. Registrar mascota")
    print("2. Mostrar todas las mascotas")
    print("3. Mostrar mascotas disponibles")
    print("4. Buscar mascotas por especie")
    print("5. Adoptar una mascota")
    print("6. Contar mascotas por especie")
    print("7. Mostrar la mascota más joven")
    print("8. Mostrar estadísticas")
    print("9. Salir")

    opcion = input("Seleccione una opción: ").strip()

    while opcion == "" or opcion.isdigit() == False:
        print("Opción no válida.")
        opcion = input("Seleccione una opción: ").strip()

    opcion = int(opcion)

    while opcion < 1 or opcion > 9:
        print("Opción no válida.")
        opcion = input("Seleccione una opción: ").strip()

        while opcion == "" or opcion.isdigit() == False:
            print("Opción no válida.")
            opcion = input("Seleccione una opción: ").strip()

        opcion = int(opcion)

    if opcion == 1:

        codigo = input("Ingrese el código de la mascota: ").strip()
        codigo = codigo.upper()

        while codigo == "" or len(codigo) != 4:
            print("El código debe tener exactamente 4 caracteres.")
            codigo = input("Ingrese el código de la mascota: ").strip()
            codigo = codigo.upper()

        while codigo in mascotas:
            print("Ese código ya existe.")
            codigo = input("Ingrese otro código: ").strip()
            codigo = codigo.upper()

            while codigo == "" or len(codigo) != 4:
                print("El código debe tener exactamente 4 caracteres.")
                codigo = input("Ingrese otro código: ").strip()
                codigo = codigo.upper()

        nombre = input("Ingrese el nombre de la mascota: ").strip()

        while nombre == "":
            print("El nombre no puede estar vacío.")
            nombre = input("Ingrese el nombre de la mascota: ").strip()

        print("===== ESPECIE =====")
        print("1. Perro")
        print("2. Gato")
        print("3. Otra especie")

        especie = input("Seleccione una opción: ").strip()

        while especie == "" or especie.isdigit() == False:
            print("Opción no válida.")
            especie = input("Seleccione una opción: ").strip()

        especie = int(especie)

        while especie < 1 or especie > 3:
            print("Opción no válida.")
            especie = input("Seleccione una opción: ").strip()

            while especie == "" or especie.isdigit() == False:
                print("Opción no válida.")
                especie = input("Seleccione una opción: ").strip()

            especie = int(especie)

        if especie == 1:
            especie = "perro"

        elif especie == 2:
            especie = "gato"

        else:
            especie = input("Ingrese la especie: ").strip()

            while especie == "":
                print("La especie no puede estar vacía.")
                especie = input("Ingrese la especie: ").strip()

            especie = especie.lower()

        edad = input("Ingrese la edad de la mascota: ").strip()

        while edad == "" or edad.isdigit() == False:
            print("La edad debe ser un número.")
            edad = input("Ingrese la edad de la mascota: ").strip()

        edad = int(edad)

        mascotas[codigo] = {
            "nombre": nombre,
            "especie": especie,
            "edad": edad,
            "adoptada": False
        }

        print("Mascota registrada correctamente.")

    elif opcion == 2:

        if len(mascotas) == 0:
            print("No hay mascotas registradas.")

        else:
            print("===== TODAS LAS MASCOTAS =====")

            for codigo, mascota in mascotas.items():
                print("Código:", codigo)
                print("Nombre:", mascota["nombre"])
                print("Especie:", mascota["especie"])
                print("Edad:", mascota["edad"])

                if mascota["adoptada"] == True:
                    print("Estado: Adoptada")
                else:
                    print("Estado: Disponible")

                print("----------------------")

    elif opcion == 3:

        if len(mascotas) == 0:
            print("No hay mascotas registradas.")

        else:
            hay_disponibles = False

            print("===== MASCOTAS DISPONIBLES =====")

            for codigo, mascota in mascotas.items():

                if mascota["adoptada"] == False:
                    hay_disponibles = True

                    print("Código:", codigo)
                    print("Nombre:", mascota["nombre"])
                    print("Especie:", mascota["especie"])
                    print("Edad:", mascota["edad"])
                    print("----------------------")

            if hay_disponibles == False:
                print("No hay mascotas disponibles para adopción.")

    elif opcion == 4:

        if len(mascotas) == 0:
            print("No hay mascotas registradas.")

        else:
            print("===== BUSCAR POR ESPECIE =====")
            print("1. Perro")
            print("2. Gato")
            print("3. Otra especie")

            especie = input("Seleccione una opción: ").strip()

            while especie == "" or especie.isdigit() == False:
                print("Opción no válida.")
                especie = input("Seleccione una opción: ").strip()

            especie = int(especie)

            while especie < 1 or especie > 3:
                print("Opción no válida.")
                especie = input("Seleccione una opción: ").strip()

                while especie == "" or especie.isdigit() == False:
                    print("Opción no válida.")
                    especie = input("Seleccione una opción: ").strip()

                especie = int(especie)

            if especie == 1:
                especie_buscada = "perro"

            elif especie == 2:
                especie_buscada = "gato"

            else:
                especie_buscada = input("Ingrese la especie que desea buscar: ").strip()

                while especie_buscada == "":
                    print("La especie no puede estar vacía.")
                    especie_buscada = input("Ingrese la especie que desea buscar: ").strip()

                especie_buscada = especie_buscada.lower()

            encontrada = False

            for codigo, mascota in mascotas.items():

                if mascota["especie"] == especie_buscada:
                    encontrada = True

                    print("Código:", codigo)
                    print("Nombre:", mascota["nombre"])
                    print("Especie:", mascota["especie"])
                    print("Edad:", mascota["edad"])

                    if mascota["adoptada"] == True:
                        print("Estado: Adoptada")
                    else:
                        print("Estado: Disponible")

                    print("----------------------")

            if encontrada == False:
                print("No hay mascotas de esa especie.")

    elif opcion == 5:

        if len(mascotas) == 0:
            print("No hay mascotas registradas.")

        else:

            print("===== MASCOTAS REGISTRADAS =====")

            for codigo, mascota in mascotas.items():
                print("Código:", codigo)
                print("Nombre:", mascota["nombre"])
                print("Especie:", mascota["especie"])
                print("----------------------")

            codigo = input("Ingrese el código de la mascota: ").strip()
            codigo = codigo.upper()

            while codigo == "" or len(codigo) != 4:
                print("El código debe tener exactamente 4 caracteres.")
                codigo = input("Ingrese el código de la mascota: ").strip()
                codigo = codigo.upper()

            while codigo not in mascotas:
                print("La mascota no existe.")
                codigo = input("Ingrese nuevamente el código: ").strip()
                codigo = codigo.upper()

                while codigo == "" or len(codigo) != 4:
                    print("El código debe tener exactamente 4 caracteres.")
                    codigo = input("Ingrese nuevamente el código: ").strip()
                    codigo = codigo.upper()

            if mascotas[codigo]["adoptada"] == False:
                mascotas[codigo]["adoptada"] = True
                print("La mascota fue adoptada correctamente.")

            else:
                print("Esta mascota ya fue adoptada.")

    elif opcion == 6:

        perros = 0
        gatos = 0
        otras = 0

        for codigo, mascota in mascotas.items():

            if mascota["especie"] == "perro":
                perros = perros + 1

            elif mascota["especie"] == "gato":
                gatos = gatos + 1

            else:
                otras = otras + 1

        print("===== CANTIDAD POR ESPECIE =====")
        print("Perros:", perros)
        print("Gatos:", gatos)
        print("Otras especies:", otras)

    elif opcion == 7:

        if len(mascotas) == 0:
            print("No hay mascotas registradas.")

        else:

            menor = None
            codigo_menor = ""

            for codigo, mascota in mascotas.items():

                if menor == None or mascota["edad"] < menor["edad"]:
                    menor = mascota
                    codigo_menor = codigo

            print("===== MASCOTA MÁS JOVEN =====")
            print("Código:", codigo_menor)
            print("Nombre:", menor["nombre"])
            print("Especie:", menor["especie"])
            print("Edad:", menor["edad"])

            if menor["adoptada"] == True:
                print("Estado: Adoptada")
            else:
                print("Estado: Disponible")

    elif opcion == 8:

        total = len(mascotas)
        disponibles = 0
        adoptadas = 0
        perros = 0
        gatos = 0
        otras = 0

        for codigo, mascota in mascotas.items():

            if mascota["adoptada"] == True:
                adoptadas = adoptadas + 1
            else:
                disponibles = disponibles + 1

            if mascota["especie"] == "perro":
                perros = perros + 1

            elif mascota["especie"] == "gato":
                gatos = gatos + 1

            else:
                otras = otras + 1

        print("===== ESTADÍSTICAS =====")
        print("Total de mascotas:", total)
        print("Mascotas disponibles:", disponibles)
        print("Mascotas adoptadas:", adoptadas)
        print("Perros:", perros)
        print("Gatos:", gatos)
        print("Otras especies:", otras)

    elif opcion == 9:
        print("Gracias por usar el sistema de adopción.")
