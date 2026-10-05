peliculas = {
    "accion": ["Avengers", "John Wick", "Misión Imposible"],
    "comedia": ["Son como niños", "¿Qué pasó ayer?", "Jumanji"],
    "terror": ["El Conjuro", "It", "La Monja"],
    "ciencia ficcion": ["Interestelar", "Avatar", "Matrix"]
}

cliente = {}
viendo = {}

opcion = 0

while opcion != 8:

    print("========= PLATAFORMA DE PELÍCULAS =========")
    print("0. Agregar usuario")
    print("1. Ver categorías")
    print("2. Ver películas por categoría")
    print("3. Buscar película")
    print("4. Agregar película")
    print("5. Crear categoría")
    print("6. Cantidad de películas por categoría")
    print("7. Categoría con más películas")
    print("8. Salir")

    opcion = input("Seleccione una opción: ").strip()

    while opcion == "" or opcion.isdigit() == False:
        print("Opción no válida.")
        opcion = input("Seleccione una opción: ").strip()

    opcion = int(opcion)

    while opcion < 0 or opcion > 8:
        print("Opción no válida.")
        opcion = input("Seleccione una opción: ").strip()

        while opcion == "" or opcion.isdigit() == False:
            print("Opción no válida.")
            opcion = input("Seleccione una opción: ").strip()

        opcion = int(opcion)

    if opcion == 0:

        print("========= REGISTRO DE USUARIOS =========")

        nombre = input("Digite el nombre del usuario: ").strip()

        while nombre == "":
            print("El nombre no puede estar vacío.")
            nombre = input("Digite el nombre del usuario: ").strip()

        telefono = input("Digite el teléfono del usuario: ").strip()

        while telefono == "" or telefono.isdigit() == False:
            print("El teléfono debe contener solamente números.")
            telefono = input("Digite el teléfono del usuario: ").strip()

        while telefono in cliente:
            print("Ese teléfono ya está registrado.")
            telefono = input("Digite otro teléfono: ").strip()

            while telefono == "" or telefono.isdigit() == False:
                print("El teléfono debe contener solamente números.")
                telefono = input("Digite otro teléfono: ").strip()

        cliente[telefono] = {
            "nombre": nombre
        }

        print("Usuario registrado correctamente.")

    elif opcion == 1:

        print("========= CATEGORÍAS DISPONIBLES =========")

        if len(peliculas) == 0:
            print("No hay categorías disponibles.")

        else:

            for categoria in peliculas:
                print("-", categoria)

    elif opcion == 2:

        print("========= CATEGORÍAS =========")

        for categoria in peliculas:
            print("-", categoria)

        categoria = input("Ingrese la categoría que desea consultar: ").strip()
        categoria = categoria.lower()

        while categoria == "":
            print("La categoría no puede estar vacía.")
            categoria = input("Ingrese la categoría que desea consultar: ").strip()
            categoria = categoria.lower()

        while categoria not in peliculas:
            print("La categoría no existe.")
            categoria = input("Ingrese nuevamente la categoría: ").strip()
            categoria = categoria.lower()

            while categoria == "":
                print("La categoría no puede estar vacía.")
                categoria = input("Ingrese nuevamente la categoría: ").strip()
                categoria = categoria.lower()

        print("========= PELÍCULAS =========")

        if len(peliculas[categoria]) == 0:
            print("No hay películas en esta categoría.")

        else:

            for pelicula in peliculas[categoria]:

                cantidad = 0

                for telefono in viendo:

                    if viendo[telefono] == pelicula:
                        cantidad = cantidad + 1

                print("-", pelicula, "| Usuarios viéndola:", cantidad, "/ 3")

    elif opcion == 3:

        if len(cliente) == 0:
            print("Primero debe registrar un usuario.")

        else:

            print("========= USUARIOS =========")

            for telefono in cliente:
                print("Nombre:", cliente[telefono]["nombre"])
                print("Teléfono:", telefono)
                print("----------------------")

            telefono = input("Digite el teléfono del usuario que solicita el servicio: ").strip()

            while telefono == "" or telefono.isdigit() == False:
                print("El teléfono no es válido.")
                telefono = input("Digite nuevamente el teléfono: ").strip()

            while telefono not in cliente:
                print("El usuario no existe.")
                telefono = input("Digite nuevamente el teléfono: ").strip()

                while telefono == "" or telefono.isdigit() == False:
                    print("El teléfono no es válido.")
                    telefono = input("Digite nuevamente el teléfono: ").strip()

            nombre = input("Ingrese el nombre de la película: ").strip()

            while nombre == "":
                print("El nombre no puede estar vacío.")
                nombre = input("Ingrese el nombre de la película: ").strip()

            encontrada = False
            categoria_pelicula = ""

            for categoria in peliculas:

                for pelicula in peliculas[categoria]:

                    if pelicula.lower() == nombre.lower():
                        encontrada = True
                        categoria_pelicula = categoria
                        nombre_pelicula = pelicula

            if encontrada == False:

                print("La película no está disponible.")

            else:

                cantidad = 0

                for usuario in viendo:

                    if viendo[usuario].lower() == nombre_pelicula.lower():
                        cantidad = cantidad + 1

                if telefono in viendo:

                    print("El usuario ya está viendo una película.")
                    print("Debe dejar de verla antes de seleccionar otra.")

                elif cantidad >= 3:

                    print("La película no está disponible en este momento.")
                    print("Ya hay 3 usuarios viendo esta película.")

                else:

                    viendo[telefono] = nombre_pelicula

                    print("La película está disponible.")
                    print("Categoría:", categoria_pelicula)
                    print("El usuario comenzó a ver:", nombre_pelicula)

    elif opcion == 4:

        print("========= CATEGORÍAS =========")

        for categoria in peliculas:
            print("-", categoria)

        categoria = input("Ingrese la categoría donde desea agregar la película: ").strip()
        categoria = categoria.lower()

        while categoria == "":
            print("La categoría no puede estar vacía.")
            categoria = input("Ingrese la categoría donde desea agregar la película: ").strip()
            categoria = categoria.lower()

        while categoria not in peliculas:
            print("La categoría no existe.")
            categoria = input("Ingrese nuevamente la categoría: ").strip()
            categoria = categoria.lower()

            while categoria == "":
                print("La categoría no puede estar vacía.")
                categoria = input("Ingrese nuevamente la categoría: ").strip()
                categoria = categoria.lower()

        nombre = input("Ingrese el nombre de la película: ").strip()

        while nombre == "":
            print("El nombre de la película no puede estar vacío.")
            nombre = input("Ingrese el nombre de la película: ").strip()

        existe = False

        for pelicula in peliculas[categoria]:

            if pelicula.lower() == nombre.lower():
                existe = True

        while existe == True:

            print("Esa película ya existe en esta categoría.")
            nombre = input("Ingrese otro nombre: ").strip()

            while nombre == "":
                print("El nombre de la película no puede estar vacío.")
                nombre = input("Ingrese otro nombre: ").strip()

            existe = False

            for pelicula in peliculas[categoria]:

                if pelicula.lower() == nombre.lower():
                    existe = True

        peliculas[categoria].append(nombre)

        print("Película agregada correctamente.")

    elif opcion == 5:

        categoria = input("Ingrese el nombre de la nueva categoría: ").strip()
        categoria = categoria.lower()

        while categoria == "":
            print("El nombre de la categoría no puede estar vacío.")
            categoria = input("Ingrese el nombre de la nueva categoría: ").strip()
            categoria = categoria.lower()

        while categoria in peliculas:

            print("Esa categoría ya existe.")
            categoria = input("Ingrese otro nombre de categoría: ").strip()
            categoria = categoria.lower()

            while categoria == "":
                print("El nombre de la categoría no puede estar vacío.")
                categoria = input("Ingrese otro nombre de categoría: ").strip()
                categoria = categoria.lower()

        peliculas[categoria] = []

        print("Categoría creada correctamente.")

        nombre = input("Ingrese el nombre de la primera película: ").strip()

        while nombre == "":
            print("El nombre de la película no puede estar vacío.")
            nombre = input("Ingrese el nombre de la primera película: ").strip()

        peliculas[categoria].append(nombre)

        print("Película agregada correctamente.")

    elif opcion == 6:

        print("========= CANTIDAD DE PELÍCULAS =========")

        for categoria in peliculas:

            cantidad = len(peliculas[categoria])

            print(categoria, ":", cantidad)

    elif opcion == 7:

        if len(peliculas) == 0:

            print("No hay categorías disponibles.")

        else:

            mayor = -1
            categoria_mayor = ""

            for categoria in peliculas:

                cantidad = len(peliculas[categoria])

                if cantidad > mayor:
                    mayor = cantidad
                    categoria_mayor = categoria

            print("========= CATEGORÍA CON MÁS PELÍCULAS =========")
            print("Categoría:", categoria_mayor)
            print("Cantidad de películas:", mayor)

    elif opcion == 8:

        print("Gracias por usar la plataforma de películas.")
