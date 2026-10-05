import datetime

clases_gimnasio = {"Yoga": 14, "Spinning": 15, "Crossfit": 18}

socios = []


def pedir_texto(mensaje):
    valor = input(mensaje).strip()
    while valor == "":
        print("Este campo no puede estar vacío.")
        valor = input(mensaje).strip()
    return valor


def pedir_entero(mensaje, minimo=None):
    valor = input(mensaje).strip()
    while not valor.isdigit():
        print("Debe ingresar un número entero.")
        valor = input(mensaje).strip()
    valor = int(valor)
    if minimo is not None:
        while valor < minimo:
            print("El valor debe ser mayor o igual a", minimo)
            valor = pedir_entero(mensaje)
    return valor


def pedir_opcion(mensaje, opciones_validas):
    valor = input(mensaje).strip()
    while valor not in opciones_validas:
        print("Opción no válida. Escoja entre:", opciones_validas)
        valor = input(mensaje).strip()
    return valor


def pedir_fecha(mensaje):

    while True:
        texto_fecha = input(mensaje + " (formato DD/MM/AAAA): ").strip()

        try:
            fecha_valida = datetime.datetime.strptime(texto_fecha, "%d/%m/%Y")
            return texto_fecha
        except ValueError:
            print("Fecha inválida. Debe tener el formato DD/MM/AAAA, por ejemplo 26/09/2026")


def crear_socios_iniciales():
    lista = [
        {"id": 1, "nombre": "Juan Pérez", "edad": 20, "membresia": "premium", "pago_al_dia": True, "clases": ["Yoga", "Spinning"]},
        {"id": 2, "nombre": "Laura Gómez", "edad": 16, "membresia": "basica", "pago_al_dia": False, "clases": ["Yoga"]},
        {"id": 3, "nombre": "Carlos Ruiz", "edad": 22, "membresia": "premium", "pago_al_dia": True, "clases": ["Crossfit"]},
        {"id": 4, "nombre": "Ana Torres", "edad": 14, "membresia": "basica", "pago_al_dia": True, "clases": ["Yoga"]},
    ]
    return lista


def buscar_socio_por_id(id_socio):
    for socio in socios:
        if socio["id"] == id_socio:
            return socio
    return None


def mostrar_socios_admin():
    if len(socios) == 0:
        print("No hay socios registrados todavía.")
    else:
        print("--- Socios registrados ---")
        for socio in socios:
            estado_pago = "al día" if socio["pago_al_dia"] else "PENDIENTE"
            print("ID:", socio["id"], "- Nombre:", socio["nombre"], "- Edad:", socio["edad"], "- Membresía:", socio["membresia"], "- Pago:", estado_pago, "- Clases:", socio["clases"])


def mostrar_socios_usuario():
    if len(socios) == 0:
        print("No hay socios registrados todavía.")
    else:
        print("--- Socios ---")
        for socio in socios:
            print("ID:", socio["id"], "- Nombre:", socio["nombre"])


def mostrar_clases():
    print("--- Clases disponibles ---")
    for clase in clases_gimnasio:
        print("-", clase, "(edad mínima:", clases_gimnasio[clase], "años)")


# --- Punto 1: evaluar a un solo socio para una clase ---
def evaluar_socio(socio, clase):

    pago_ok = socio["pago_al_dia"]
    edad_ok = socio["edad"] >= clases_gimnasio[clase]

    if pago_ok and edad_ok:
        print(socio["nombre"], "está HABILITADO para asistir a", clase)
    else:
        print(socio["nombre"], "NO está habilitado para asistir a", clase, "porque:")
        if pago_ok == False:
            print("- El pago del mes no está al día.")
        if edad_ok == False:
            print("- La edad (", socio["edad"], "años) es menor al mínimo requerido (", clases_gimnasio[clase], "años).")


def esta_habilitado(socio, clase):
    return socio["pago_al_dia"] and socio["edad"] >= clases_gimnasio[clase]


# --- Punto 2: consultar habilitados con filter ---
def habilitados_para_clase(clase):

    habilitados = list(filter(lambda socio: esta_habilitado(socio, clase), socios))

    if len(habilitados) == 0:
        print("No hay socios habilitados para", clase)
    else:
        print("Socios habilitados para", clase, ":")
        for socio in habilitados:
            print("-", socio["nombre"])


# --- Punto 3: registrar asistencia con *args y parámetros con nombre ---
def registrar_asistencia(*asistentes, clase, fecha, instructor, salon):

    print("--- Registro de asistencia ---")
    print("Clase:", clase)
    print("Fecha:", fecha)
    print("Instructor:", instructor)
    print("Salón:", salon)
    print("Asistentes:")

    for socio in asistentes:
        print("-", socio["nombre"])


# --- Punto 4: alerta de renovación ---
def alerta_renovacion():

    morosos = list(filter(lambda socio: socio["pago_al_dia"] == False, socios))

    if len(morosos) == 0:
        print("No hay socios con pagos pendientes.")
    else:
        print("--- Socios con pago pendiente ---")
        for socio in morosos:
            print(socio["nombre"], "- no podrá asistir a:", socio["clases"])


# --- Funciones exclusivas del admin ---
def agregar_socio():

    mostrar_socios_admin()

    nuevo_id = pedir_entero("Ingrese el ID del nuevo socio: ")

    if buscar_socio_por_id(nuevo_id) is not None:
        print("Ya existe un socio con ese ID.")
        return

    nombre = pedir_texto("Nombre del socio: ")
    edad = pedir_entero("Edad del socio: ", minimo=0)
    membresia = pedir_opcion("Tipo de membresía (basica/premium): ", ["basica", "premium"])
    pago = pedir_opcion("¿Pago al día? (si/no): ", ["si", "no"])

    mostrar_clases()

    clases_inscritas = []

    while True:
        clase = input("Ingrese una clase para inscribir (Enter para terminar): ").strip()

        if clase == "":
            break

        if clase not in clases_gimnasio:
            print("Esa clase no existe.")
            continue

        clases_inscritas.append(clase)

    nuevo_socio = {
        "id": nuevo_id,
        "nombre": nombre,
        "edad": edad,
        "membresia": membresia,
        "pago_al_dia": pago == "si",
        "clases": clases_inscritas
    }

    socios.append(nuevo_socio)
    print("Socio agregado correctamente.")


def editar_pago():

    mostrar_socios_admin()

    id_socio = pedir_entero("Ingrese el ID del socio a editar: ")
    socio = buscar_socio_por_id(id_socio)

    if socio is None:
        print("No existe un socio con ese ID.")
        return

    print("Estado actual del pago:", "al día" if socio["pago_al_dia"] else "pendiente")

    nuevo_estado = pedir_opcion("Nuevo estado (si = al día / no = pendiente): ", ["si", "no"])
    socio["pago_al_dia"] = (nuevo_estado == "si")

    print("Estado de pago actualizado.")


def editar_clases_socio():

    mostrar_socios_admin()

    id_socio = pedir_entero("Ingrese el ID del socio a editar: ")
    socio = buscar_socio_por_id(id_socio)

    if socio is None:
        print("No existe un socio con ese ID.")
        return

    print("Clases actuales de", socio["nombre"], ":", socio["clases"])
    mostrar_clases()

    clase = pedir_opcion("Ingrese la clase a agregar: ", list(clases_gimnasio.keys()))

    if clase in socio["clases"]:
        print("El socio ya está inscrito en esa clase.")
    else:
        socio["clases"].append(clase)
        print("Clase agregada correctamente.")


# --- Menús ---
def menu_admin():

    while True:

        print()
        print("       MENÚ ADMINISTRADOR")
        print("1. Ver socios registrados")
        print("2. Agregar socio nuevo")
        print("3. Editar estado de pago de un socio")
        print("4. Agregar clase a un socio")
        print("5. Salir (volver al menú principal)")

        opcion = pedir_opcion("Escoja una opción: ", ["1", "2", "3", "4", "5"])

        if opcion == "1":
            mostrar_socios_admin()

        elif opcion == "2":
            agregar_socio()

        elif opcion == "3":
            editar_pago()

        elif opcion == "4":
            editar_clases_socio()

        elif opcion == "5":
            break


def menu_usuario():

    while True:

        print()
        print("       MENÚ USUARIO")
        print("1. Evaluar si un socio puede asistir a una clase")
        print("2. Ver socios habilitados para una clase")
        print("3. Registrar asistencia a una sesión")
        print("4. Alerta de renovación (pagos pendientes)")
        print("5. Salir (volver al menú principal)")

        opcion = pedir_opcion("Escoja una opción: ", ["1", "2", "3", "4", "5"])

        if opcion == "1":

            mostrar_socios_usuario()
            id_socio = pedir_entero("Ingrese el ID del socio: ")
            socio = buscar_socio_por_id(id_socio)

            if socio is None:
                print("No existe un socio con ese ID.")
                continue

            mostrar_clases()
            clase = pedir_opcion("Ingrese la clase: ", list(clases_gimnasio.keys()))

            evaluar_socio(socio, clase)

        elif opcion == "2":
            mostrar_clases()
            clase = pedir_opcion("Ingrese la clase: ", list(clases_gimnasio.keys()))
            habilitados_para_clase(clase)

        elif opcion == "3":

            mostrar_socios_usuario()

            asistentes = []

            while True:
                id_socio = pedir_entero("Ingrese el ID de un asistente (0 para terminar): ")

                if id_socio == 0:
                    break

                socio = buscar_socio_por_id(id_socio)

                if socio is None:
                    print("No existe un socio con ese ID.")
                    continue

                ya_agregado = False
                for asistente in asistentes:
                    if asistente["id"] == socio["id"]:
                        ya_agregado = True

                if ya_agregado:
                    print("Ese socio ya fue agregado a esta sesión.")
                    continue

                asistentes.append(socio)
                print(socio["nombre"], "agregado a la sesión.")

            if len(asistentes) == 0:
                print("No se registraron asistentes.")
                continue

            mostrar_clases()
            clase = pedir_opcion("Clase dictada: ", list(clases_gimnasio.keys()))
            fecha = pedir_fecha("Fecha de la sesión")
            instructor = pedir_texto("Nombre del instructor: ")
            salon = pedir_texto("Salón: ")

            registrar_asistencia(*asistentes, clase=clase, fecha=fecha, instructor=instructor, salon=salon)

        elif opcion == "4":
            alerta_renovacion()

        elif opcion == "5":
            break


def main():

    global socios
    socios = crear_socios_iniciales()

    while True:

        print()
        print("       BIENVENIDO A FITZONE")
        print("1. Ingresar como Administrador")
        print("2. Ingresar como Usuario")
        print("3. Salir del programa")

        opcion = pedir_opcion("Escoja una opción: ", ["1", "2", "3"])

        if opcion == "1":
            menu_admin()

        elif opcion == "2":
            menu_usuario()

        elif opcion == "3":
            print("Programa terminado.")
            break


main()
