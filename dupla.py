pasajeros = [("Deivis Jiménez", 15170230, "Valledupar"), ("Sofía Quintero", 1065576300, "Barranquilla"),("Pedro Sánchez", 16124479, "Bucaramanga"),("Juan Méndez", 1067345987, "Bogotá")]


ciudades = [("Valledupar", "Cesar"),("Barranquilla", "Atlántico"),("Bucaramanga", "Santander"),("Bogotá", "Cundinamarca"),("Riohacha", "Guajira")]


while True:

    print("       MENÚ DE PASAJEROS")
    
    print("1. Agregar pasajero")
    print("2. Agregar ciudad")
    print("3. Buscar ciudad por ID")
    print("4. Pasajeros por ciudad")
    print("5. Buscar departamento por ID")
    print("6. Pasajeros por departamento")
    print("7. Salir")
   

    opcion = input("Escoja una opción: ").strip()

   
    if opcion == "1":

        nombre = input("Nombre del pasajero: ").strip()

        while nombre == "":
            print("El nombre no puede estar vacío.")
            nombre = input("Nombre del pasajero: ").strip()

        id_pasajero = input("ID del pasajero: ").strip()

        while not id_pasajero.isdigit() or int(id_pasajero) <= 0:
            print("El ID debe ser un número mayor que 0.")
            id_pasajero = input("ID del pasajero: ").strip()

        id_pasajero = int(id_pasajero)

       
        existe = False

        for pasajero in pasajeros:
            if pasajero[1] == id_pasajero:
                existe = True

        if existe:
            print("Ese ID ya existe.")

        else:

            destino = input("Ciudad de destino: ").strip()

            while destino == "":
                print("La ciudad no puede estar vacía.")
                destino = input("Ciudad de destino: ").strip()

           
            ciudad_existe = False

            for ciudad in ciudades:
                if ciudad[0].lower() == destino.lower():
                    ciudad_existe = True

            if ciudad_existe:
                pasajeros.append((nombre, id_pasajero, destino))
                print("Pasajero agregado correctamente.")

            else:
                print("Esa ciudad no existe en la lista.")

    elif opcion == "2":

        ciudad_nueva = input("Nombre de la ciudad: ").strip()

        while ciudad_nueva == "":
            print("La ciudad no puede estar vacía.")
            ciudad_nueva = input("Nombre de la ciudad: ").strip()

        departamento = input("Departamento: ").strip()

        while departamento == "":
            print("El departamento no puede estar vacío.")
            departamento = input("Departamento: ").strip()

        existe = False

        for ciudad in ciudades:
            if ciudad[0].lower() == ciudad_nueva.lower():
                existe = True

        if existe:
            print("Esa ciudad ya existe.")

        else:
            ciudades.append((ciudad_nueva, departamento))
            print("Ciudad agregada correctamente.")

    elif opcion == "3":
        id_pasajero = input("Ingrese el ID: ").strip()

        while id_pasajero == "":
            print("El ID no puede estar vacío.")
            id_pasajero = input("Ingrese el ID: ").strip()

        if id_pasajero.isdigit():

            id_pasajero = int(id_pasajero)
            encontrado = False

            for pasajero in pasajeros:

                if pasajero[1] == id_pasajero:
                    print("El pasajero viaja a:", pasajero[2])
                    encontrado = True

            if encontrado == False:
                print("No existe ese pasajero.")

        else:
            print("El ID debe ser un número.")


    
    elif opcion == "4":

        ciudad_buscar = input("Ingrese la ciudad: ").strip()

        while ciudad_buscar == "":
            print("La ciudad no puede estar vacía.")
            ciudad_buscar = input("Ingrese la ciudad: ").strip()

        cantidad = 0
        for pasajero in pasajeros:
            if pasajero[2].lower() == ciudad_buscar.lower():
                cantidad = cantidad + 1
        print("Hay",cantidad,"pasajero(s) que viajan a",ciudad_buscar)

    elif opcion == "5":
        id_pasajero = input("Ingrese el ID: ").strip()

        while id_pasajero == "":
            print("El ID no puede estar vacío.")
            id_pasajero = input("Ingrese el ID: ").strip()

        if id_pasajero.isdigit():

            id_pasajero = int(id_pasajero)
            encontrado = False

            for pasajero in pasajeros:

                if pasajero[1] == id_pasajero:

                    destino = pasajero[2]

                    for ciudad in ciudades:

                        if ciudad[0].lower() == destino.lower():

                            print("El pasajero viaja al departamento de:",ciudad[1])

                            encontrado = True

            if encontrado == False:
                print("No se encontró el pasajero.")

        else:
            print("El ID debe ser un número.")

    elif opcion == "6":

        departamento_buscar = input("Ingrese el departamento: ").strip()

        while departamento_buscar == "":
            print("El departamento no puede estar vacío.")
            departamento_buscar = input("Ingrese el departamento: ").strip()

        cantidad = 0

        for pasajero in pasajeros:

            destino = pasajero[2]

            for ciudad in ciudades:

                if ciudad[0].lower() == destino.lower():

                    if ciudad[1].lower() == departamento_buscar.lower():

                        cantidad = cantidad + 1

        print("Hay",cantidad, "pasajero(s) que viajan al departamento de", departamento_buscar)
        
    elif opcion == "7":

        print("Programa terminado.")
        break
    else:

        print("Opción incorrecta. Escoja del 1 al 7.")
