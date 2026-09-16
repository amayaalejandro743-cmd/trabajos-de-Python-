pasajeros = [("Deivis Jiménez", 15170230, "Valledupar"), ("Sofía Quintero", 1065576300, "Barranquilla"),("Pedro Sánchez", 16124479, "Bucaramanga"),("Juan Méndez", 1067345987, "Bogotá")]


ciudades = [("Valledupar", "Cesar"),("Barranquilla", "Atlántico"),("Bucaramanga", "Santander"),("Bogotá", "Cundinamarca"),("Riohacha", "Guajira")]

equpaje = [("tipo1", 0 ), ("tipo2", 20000),("tipo3",50000)]

precios_destino = []

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

        agregado = False

        while agregado == False:

            print(" Pasajeros ya registrados ")
            for pasajero in pasajeros:
                print("ID:", pasajero[1],   pasajero[0], " Destino:", pasajero[2])

            print(" Ciudades disponibles ")
            for ciudad in ciudades:
                print( ciudad[0], "(", ciudad[1], ")")

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
                continue

            destino = input("Ciudad de destino: ").strip()

            while destino == "":
                print("La ciudad no puede estar vacía.")
                destino = input("Ciudad de destino: ").strip()

           
            ciudad_existe = False

            for ciudad in ciudades:
                if ciudad[0].lower() == destino.lower():
                    ciudad_existe = True

            if ciudad_existe == False:
                print("Esa ciudad no existe en la lista.")
                continue

            pasajeros.append((nombre, id_pasajero, destino))
            print("Pasajero agregado correctamente.")

            
            encontro_precio = False
            indice_precio = 0
            precio_tiquete = 0

            for i in range(len(precios_destino)):
                if precios_destino[i][0].lower() == destino.lower():
                    precio_tiquete = precios_destino[i][1]
                    indice_precio = i
                    encontro_precio = True

            if encontro_precio == False:
                precio_tiquete = 100000
                precios_destino.append((destino, precio_tiquete))
                indice_precio = len(precios_destino) - 1

            costo_equipaje = 0
            tipo_equipaje = "Ninguno"
            equipaje_rechazado = False
            tiene_equipaje_bool = False

            print("¿Tiene equipaje?")
            print("1. Sí")
            print("2. No")
            tiene_equipaje = input("Escoja una opción: ").strip()

            while tiene_equipaje != "1" and tiene_equipaje != "2":
                print("Escoja 1 o 2.")
                tiene_equipaje = input("Escoja una opción: ").strip()

            if tiene_equipaje == "1":
                tiene_equipaje_bool = True

            if tiene_equipaje_bool:

                peso = input("Ingrese el peso del equipaje en kg: ").strip()

                while not peso.replace(".", "", 1).isdigit():
                    print("El peso debe ser un número.")
                    peso = input("Ingrese el peso del equipaje en kg: ").strip()

                peso = float(peso)

                if peso <= 10:
                    tipo_equipaje = "tipo1"
                elif peso <= 20:
                    tipo_equipaje = "tipo2"
                elif peso <= 50:
                    tipo_equipaje = "tipo3"
                else:
                    print("El equipaje excede el peso permitido (50 kg) y no puede ser llevado.")
                    equipaje_rechazado = True

                if equipaje_rechazado == False:
                    for equipaje_item in equpaje:
                        if equipaje_item[0] == tipo_equipaje:
                            costo_equipaje = equipaje_item[1]

            total_pagar = precio_tiquete + costo_equipaje

            print("Valor del tiquete:", precio_tiquete)

            if equipaje_rechazado:
                print("Equipaje: no permitido (excede el peso)")
            else:
                print("Costo del equipaje:", costo_equipaje)

            print("Total a pagar:", total_pagar)

            
            precios_destino[indice_precio] = (destino, precio_tiquete + 20000)

            agregado = True

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
        print(" iD DE PASAJEROS ")
        for pasajero in pasajeros:
            print("ID:", pasajero[1],   pasajero[0])
            
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
        print(" Ciudades disponibles ")
        for ciudad in ciudades:
            print( ciudad[0], "(", ciudad[1], ")")


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
        print(" Ciudades disponibles ")
        for ciudad in ciudades:
            print( ciudad[0], "(", ciudad[1], ")")

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
