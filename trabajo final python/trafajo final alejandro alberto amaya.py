import random
import string
import sys

usuarios = {}                  
solicitudes_credenciales = []    
solicitudes_compra = []          
codigos_pago = {}                

#base de datos de peliculas y series
categorias = {
    "Accion": {
        "Pelicula": {
            "John Wick": {"anio": 2014, "descripcion": "Asesino retirado busca venganza", "calificaciones": []},
            "Mad Max Fury Road": {"anio": 2015, "descripcion": "Persecucion en el desierto", "calificaciones": []},
            "Gladiador": {"anio": 2000, "descripcion": "Un general busca justicia en Roma", "calificaciones": []},
            "Duro de Matar": {"anio": 1988, "descripcion": "Un policia enfrenta terroristas", "calificaciones": []},
            "Mision Imposible": {"anio": 1996, "descripcion": "Un agente debe limpiar su nombre", "calificaciones": []}
        },
        "Serie": {
            "The Boys": {"anio": 2019, "descripcion": "Superheroes corruptos y sus rivales", "calificaciones": []},
            "Daredevil": {"anio": 2015, "descripcion": "Un abogado ciego combate el crimen", "calificaciones": []},
            "Vikingos": {"anio": 2013, "descripcion": "Las conquistas de Ragnar Lothbrok", "calificaciones": []},
            "24": {"anio": 2001, "descripcion": "Un agente contra el reloj", "calificaciones": []},
            "Reacher": {"anio": 2022, "descripcion": "Un ex militar resuelve crimenes", "calificaciones": []}
        }
    },
    "Comedia": {
        "Pelicula": {
            "Superbad": {"anio": 2007, "descripcion": "Dos amigos y una fiesta de graduacion", "calificaciones": []},
            "Que paso ayer": {"anio": 2009, "descripcion": "Una despedida de soltero sin control", "calificaciones": []},
            "Chicas pesadas": {"anio": 2004, "descripcion": "Una chica nueva en un colegio cruel", "calificaciones": []},
            "Dos tontos muy tontos": {"anio": 1994, "descripcion": "Dos amigos y un viaje absurdo", "calificaciones": []},
            "Elf": {"anio": 2003, "descripcion": "Un humano criado por elfos", "calificaciones": []}
        },
        "Serie": {
            "Brooklyn Nine-Nine": {"anio": 2013, "descripcion": "Policias divertidos en Nueva York", "calificaciones": []},
            "Friends": {"anio": 1994, "descripcion": "Seis amigos viviendo en Nueva York", "calificaciones": []},
            "The Office": {"anio": 2005, "descripcion": "La vida diaria en una oficina", "calificaciones": []},
            "Parks and Recreation": {"anio": 2009, "descripcion": "Una funcionaria y su pueblo", "calificaciones": []},
            "Modern Family": {"anio": 2009, "descripcion": "Tres familias muy diferentes", "calificaciones": []}
        }
    },
    "Terror": {
        "Pelicula": {
            "El Conjuro": {"anio": 2013, "descripcion": "Una familia acosada por una presencia", "calificaciones": []},
            "Hereditary": {"anio": 2018, "descripcion": "Una familia y un oscuro secreto", "calificaciones": []},
            "It": {"anio": 2017, "descripcion": "Amigos enfrentan a un payaso siniestro", "calificaciones": []},
            "Sinister": {"anio": 2012, "descripcion": "Un escritor encuentra videos macabros", "calificaciones": []},
            "Scream": {"anio": 1996, "descripcion": "Un asesino enmascarado acecha un pueblo", "calificaciones": []}
        },
        "Serie": {
            "La maldicion de Hill House": {"anio": 2018, "descripcion": "Una casa embrujada y su pasado", "calificaciones": []},
            "American Horror Story": {"anio": 2011, "descripcion": "Una historia de terror por temporada", "calificaciones": []},
            "Stranger Things": {"anio": 2016, "descripcion": "Misterios sobrenaturales en un pueblo", "calificaciones": []},
            "The Walking Dead": {"anio": 2010, "descripcion": "Sobrevivientes de un apocalipsis zombi", "calificaciones": []},
            "Penny Dreadful": {"anio": 2014, "descripcion": "Monstruos clasicos en Londres", "calificaciones": []}
        }
    },
    "Ciencia ficcion": {
        "Pelicula": {
            "Interestelar": {"anio": 2014, "descripcion": "Un viaje espacial para salvar la Tierra", "calificaciones": []},
            "Matrix": {"anio": 1999, "descripcion": "Un hacker descubre la realidad", "calificaciones": []},
            "Blade Runner 2049": {"anio": 2017, "descripcion": "Un cazador de replicantes busca respuestas", "calificaciones": []},
            "Avatar": {"anio": 2009, "descripcion": "Un marine en el planeta Pandora", "calificaciones": []},
            "Ex Machina": {"anio": 2014, "descripcion": "Un programador evalua una inteligencia artificial", "calificaciones": []}
        },
        "Serie": {
            "Black Mirror": {"anio": 2011, "descripcion": "El lado oscuro de la tecnologia", "calificaciones": []},
            "Dark": {"anio": 2017, "descripcion": "Viajes en el tiempo en un pueblo aleman", "calificaciones": []},
            "Westworld": {"anio": 2016, "descripcion": "Androides en un parque tematico", "calificaciones": []},
            "The Mandalorian": {"anio": 2019, "descripcion": "Un cazarrecompensas en la galaxia", "calificaciones": []},
            "Fringe": {"anio": 2008, "descripcion": "Casos de ciencia extrema en el FBI", "calificaciones": []}
        }
    }
}

# usuario admin 
admin = {
    "usuario": "admin",
    "clave": None
}

LIMITE_PRUEBA = 5
PRECIO = 12000

#validar clave
def validar_clave(clave):
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_especial = False

    for letra in clave:
        if letra.isupper():
            tiene_mayuscula = True
        elif letra.islower():
            tiene_minuscula = True
        elif letra.isdigit():
            tiene_numero = True
        elif letra in string.punctuation:
            tiene_especial = True

    if len(clave) >= 8 and tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial:
        return True
    else:
        return False

#genera clave 
def generar_clave():
    caracteres = string.ascii_letters + string.digits + string.punctuation

    clave_valida = False
    while not clave_valida:
        lista = random.choices(caracteres, k=10)
        clave = "".join(lista)
        clave_valida = validar_clave(clave)
    return clave

#genera token
def generar_token():
    letras = random.choices(string.ascii_uppercase, k=2)
    letras = "".join(letras)
    numero = random.randint(0, 9)
    token = letras + str(numero)
    return token

#genera el codigo de pago 
def generar_codigo_pago():
    codigo = random.randint(1000, 9999)
    return str(codigo)


#funciones para pedir datos 
#----------------------------------------------------
def pedir_numero(mensaje, minimo, maximo):
    while True:
        texto = input(mensaje).strip()

        if texto == "":
            print("Error: debe ingresar un numero.")
            continue

        if not texto.isdigit():
            print("Error: solo se permiten numeros.")
            continue

        numero = int(texto)

        if minimo <= numero <= maximo:
            return numero

        print(f"Error: el numero debe estar entre {minimo} y {maximo}.")


def pedir_texto(mensaje, minimo=1, maximo=100):
    while True:
        texto = input(mensaje).strip()

        if texto == "":
            print("Error: este campo no puede quedar vacio.")
            continue

        if len(texto) < minimo:
            print(f"Error: debe tener minimo {minimo} caracteres.")
            continue

        if len(texto) > maximo:
            print(f"Error: no puede superar los {maximo} caracteres.")
            continue

        return texto


def pedir_si_no(mensaje):
    while True:
        respuesta = input(mensaje).strip().upper()
        if respuesta == "S":
            return True
        if respuesta == "N":
            return False
        print("Error: solo puede responder S o N.")


def elegir_categoria():
    print("Categorias disponibles:")
    for i, categoria in enumerate(categorias.keys(), start=1):
        print(f"{i}. {categoria}")
    opcion = pedir_numero("Seleccione una categoria: ", 1, len(categorias))
    categoria_seleccionada = list(categorias.keys())[opcion - 1]
    return categoria_seleccionada


def elegir_tipo(categoria):
    tipos = list(categorias[categoria].keys())
    print(f"Tipos disponibles en la categoria '{categoria}':")
    for i, tipo in enumerate(tipos, start=1):
        print(f"{i}. {tipo}")
    opcion = pedir_numero("Seleccione un tipo: ", 1, len(tipos))
    tipo_seleccionado = tipos[opcion - 1]
    return tipo_seleccionado

#-------------------------------------------------------------


def promedio(datos):
    notas = datos["calificaciones"]
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)


def mostrar_lista(lista):
    if len(lista) == 0:
        print("No hay resultados.")
    for i in range(len(lista)):
        categoria, tipo, nombre = lista[i]
        datos = categorias[categoria][tipo][nombre]
        print(f"{i + 1}. [{tipo}] {nombre} ({datos['anio']}) - {categoria} - Calificacion: {promedio(datos):.1f}")


def buscar():
    resultados = []
    print("1. Por categoria y tipo")
    print("2. Por nombre")
    opcion = pedir_numero("Opcion: ", 1, 2)
    if opcion == 1:
        categoria = elegir_categoria()
        tipo = elegir_tipo(categoria)
        for nombre in categorias[categoria][tipo]:
            resultados.append((categoria, tipo, nombre))
    else:
        texto = pedir_texto("Nombre a buscar: ", 1, 80).lower()
        for categoria in categorias:
            for tipo in categorias[categoria]:
                for nombre in categorias[categoria][tipo]:
                    if texto in nombre.lower():
                        resultados.append((categoria, tipo, nombre))
    return resultados


def seleccionar(lista):
    if len(lista) == 0:
        print("No hay resultados.")
        return None
    mostrar_lista(lista)
    numero = pedir_numero("Elija un numero (0 para volver): ", 0, len(lista))
    if numero == 0:
        return None
    return lista[numero - 1]


def reemplazar_en_espacios(viejo, nuevo):
    # Si el Admin cambia el nombre o elimina un recurso, se actualiza
    # (nuevo) o se quita (nuevo = None) de los espacios personales.
    for cedula in usuarios:
        lista = usuarios[cedula]["espacio_personal"]
        if viejo in lista:
            posicion = lista.index(viejo)
            if nuevo is None:
                lista.pop(posicion)
            else:
                lista[posicion] = nuevo



def pantalla_bloqueo(usuario_actual):
    # Devuelve True si el usuario recupero el acceso
    while True:
        print("\nSus credenciales estan bloqueadas (version de prueba terminada).")
        print("1. Adquirir plataforma digital ADSO (COMPRAR)")
        print("2. Ingresar codigo de pago")
        print("3. Volver")
        opcion = pedir_numero("Opcion: ", 1, 3)

        if opcion == 1:
            if usuario_actual in solicitudes_compra:
                print("Ya tiene una solicitud de compra pendiente.")
            else:
                solicitudes_compra.append(usuario_actual)
                print(f"Solicitud enviada al administrador. Valor: ${PRECIO:,}")
                print("El administrador le entregara un codigo de 4 digitos.")
        elif opcion == 2:
            codigo = pedir_texto("Ingrese el codigo de pago (4 digitos): ", 4, 4)
            if not codigo.isdigit():
                print("Error: el codigo solo tiene numeros.")
            elif codigos_pago.get(usuario_actual) == codigo:
                usuarios[usuario_actual]["bloqueado"] = False
                usuarios[usuario_actual]["comprado"] = True
                del codigos_pago[usuario_actual]
                print("Acceso total restablecido. Disfrute la plataforma!")
                return True
            else:
                print("Error: codigo incorrecto.")
        else:
            return False


def ver_recurso(usuario_actual, seleccion, desde_espacio=False):
    # Devuelve "seguir" o "inicio"
    categoria, tipo, nombre = seleccion
    datos = categorias[categoria][tipo][nombre]
    usuario = usuarios[usuario_actual]

    print(f"\n--- Reproduciendo: {nombre} ---")
    print(f"Categoria: {categoria}")
    print(f"Tipo: {tipo}")
    print(f"Año: {datos['anio']}")
    print(f"Descripcion: {datos['descripcion']}")
    print(f"Calificacion promedio: {promedio(datos):.1f}")

    if not usuario["comprado"]:
        usuario["vistos"] += 1
        print(f"(Version de prueba: {usuario['vistos']} de {LIMITE_PRUEBA} recursos)")

    calificacion = pedir_numero("Califique de 1 (mala) a 5 (excelente): ", 1, 5)
    datos["calificaciones"].append(calificacion)
    print(f"Gracias por calificar '{nombre}' con {calificacion}.")

    if not desde_espacio and seleccion not in usuario["espacio_personal"]:
        if pedir_si_no("¿Agregar a su espacio personal? (S/N): "):
            usuario["espacio_personal"].append(seleccion)
            print("Agregada a su espacio personal.")

    if not usuario["comprado"] and usuario["vistos"] >= LIMITE_PRUEBA:
        usuario["bloqueado"] = True
        print(f"\nLlego al limite de {LIMITE_PRUEBA} recursos de la version de prueba.")
        if not pantalla_bloqueo(usuario_actual):
            return "inicio"

    print("\n1. Seguir en la plataforma")
    print("2. Ir al inicio del aplicativo")
    print("3. Salir de la plataforma")
    opcion = pedir_numero("Opcion: ", 1, 3)
    if opcion == 3:
        print("Gracias por usar el sistema. Hasta luego!")
        sys.exit()
    if opcion == 2:
        return "inicio"
    return "seguir"


def menu_admin():
    while True:
        print("--- MENU ADMIN ---")
        print("1. Agregar pelicula o serie")
        print("2. Consultar por categoria o nombre")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Categoria con mayor y menor cantidad")
        print("6. Solicitudes de credenciales")
        print("7. Solicitudes de compra")
        print("8. Informes")
        print("9. Cerrar sesion")
        opcion = pedir_numero("Opcion: ", 1, 9)

        if opcion == 1:
            categoria = elegir_categoria()
            tipo = elegir_tipo(categoria)
            while True:
                nombre = pedir_texto("Ingrese el nombre: ", 1, 80)
                if nombre in categorias[categoria][tipo]:
                    print("Error: ya existe una pelicula o serie con ese nombre en esa categoria y tipo.")
                else:
                    break
            anio = pedir_numero("Ingrese el año (1900-2100): ", 1900, 2100)
            descripcion = pedir_texto("Ingrese la descripcion: ", 5, 250)
            categorias[categoria][tipo][nombre] = {"anio": anio, "descripcion": descripcion, "calificaciones": []}
            print(f"{tipo} '{nombre}' agregada a '{categoria}' con calificacion 0.")

        elif opcion == 2:
            seleccion = seleccionar(buscar())
            if seleccion:
                categoria, tipo, nombre = seleccion
                datos = categorias[categoria][tipo][nombre]
                print(f"Nombre: {nombre}")
                print(f"Categoria: {categoria}")
                print(f"Tipo: {tipo}")
                print(f"Año: {datos['anio']}")
                print(f"Descripcion: {datos['descripcion']}")
                print(f"Calificacion promedio: {promedio(datos):.1f}")

        elif opcion == 3:
            seleccion = seleccionar(buscar())
            if seleccion:
                categoria, tipo, nombre = seleccion
                datos = categorias[categoria][tipo][nombre]
                print("Ingrese los nuevos datos. Todos los campos son obligatorios.")

                while True:
                    nuevo_nombre = pedir_texto(f"Nuevo nombre ({nombre}): ", 2, 80)
                    if nuevo_nombre != nombre and nuevo_nombre in categorias[categoria][tipo]:
                        print("Error: ya existe otra pelicula o serie con ese nombre.")
                    else:
                        break
                nuevo_anio = pedir_numero(f"Nuevo año ({datos['anio']}): ", 1900, 2100)
                nueva_descripcion = pedir_texto("Nueva descripcion: ", 5, 250)

                if nuevo_nombre != nombre:
                    categorias[categoria][tipo][nuevo_nombre] = categorias[categoria][tipo].pop(nombre)
                    reemplazar_en_espacios(seleccion, (categoria, tipo, nuevo_nombre))
                    nombre = nuevo_nombre

                categorias[categoria][tipo][nombre]["anio"] = nuevo_anio
                categorias[categoria][tipo][nombre]["descripcion"] = nueva_descripcion
                categorias[categoria][tipo][nombre]["calificaciones"] = []   # la calificacion vuelve a 0
                print(f"{tipo} '{nombre}' actualizada. Su calificacion volvio a 0.")

        elif opcion == 4:
            seleccion = seleccionar(buscar())
            if seleccion:
                categoria, tipo, nombre = seleccion
                preguntas = [
                    f"¿Esta seguro de eliminar '{nombre}'? (S/N): ",
                    f"¿Realmente desea eliminar '{nombre}'? (S/N): ",
                    f"ULTIMA CONFIRMACION: ¿Eliminar '{nombre}' definitivamente? (S/N): "
                ]
                confirmado = True
                for pregunta in preguntas:
                    if not pedir_si_no(pregunta):
                        confirmado = False
                        print("Eliminacion cancelada.")
                        break
                if confirmado:
                    del categorias[categoria][tipo][nombre]
                    reemplazar_en_espacios(seleccion, None)
                    print(f"{tipo} '{nombre}' eliminada exitosamente.")

        elif opcion == 5:
            mayor = None
            menor = None
            for categoria in categorias:
                total = len(categorias[categoria]["Pelicula"]) + len(categorias[categoria]["Serie"])
                if mayor is None or total > mayor[1]:
                    mayor = (categoria, total)
                if menor is None or total < menor[1]:
                    menor = (categoria, total)
            print(f"Categoria con mayor cantidad: {mayor[0]} ({mayor[1]} items)")
            print(f"Categoria con menor cantidad: {menor[0]} ({menor[1]} items)")

        elif opcion == 6:
            print("\nSolicitudes de credenciales (orden de llegada):")
            if len(solicitudes_credenciales) == 0:
                print("No hay solicitudes pendientes.")
            else:
                for i in range(len(solicitudes_credenciales)):
                    cedula = solicitudes_credenciales[i]
                    print(f"{i + 1}. {usuarios[cedula]['nombre']} - cedula {cedula}")
                eleccion = pedir_numero("Seleccione una solicitud (0 para volver): ", 0, len(solicitudes_credenciales))
                if eleccion != 0:
                    cedula = solicitudes_credenciales[eleccion - 1]
                    token = pedir_texto("Token que entrega el usuario: ", 3, 3).upper()
                    if token == usuarios[cedula]["token"]:
                        solicitudes_credenciales.pop(eleccion - 1)
                        usuarios[cedula]["clave"] = generar_clave()
                        usuarios[cedula]["token"] = generar_token()
                        print("Token verificado. Nuevas credenciales:")
                        print(f"Usuario: {cedula}")
                        print(f"Contraseña: {usuarios[cedula]['clave']}")
                        print(f"Nuevo token: {usuarios[cedula]['token']}")
                    else:
                        print("Token incorrecto. La solicitud sigue pendiente.")

        elif opcion == 7:
            print("\nSolicitudes de compra (orden de llegada):")
            if len(solicitudes_compra) == 0:
                print("No hay solicitudes de compra pendientes.")
            else:
                for i in range(len(solicitudes_compra)):
                    cedula = solicitudes_compra[i]
                    print(f"{i + 1}. {usuarios[cedula]['nombre']} - cedula {cedula}")
                eleccion = pedir_numero("Seleccione una solicitud (0 para volver): ", 0, len(solicitudes_compra))
                if eleccion != 0:
                    cedula = solicitudes_compra.pop(eleccion - 1)
                    codigo = generar_codigo_pago()
                    codigos_pago[cedula] = codigo
                    print(f"Codigo de pago para {usuarios[cedula]['nombre']}: {codigo}")
                    print("Entregue este codigo al usuario.")

        elif opcion == 8:
            compradores = 0
            en_prueba = 0
            for cedula in usuarios:
                if usuarios[cedula]["comprado"]:
                    compradores += 1
                if usuarios[cedula]["ingreso"]:
                    en_prueba += 1
            print("\n--- INFORMES ---")
            print(f"Usuarios que compraron el acceso: {compradores}")
            print(f"Usuarios que ingresaron a la version de prueba: {en_prueba}")
            print(f"Monto recaudado: ${compradores * PRECIO:,}")

        else:
            print("Sesion cerrada con exito :)")
            return



def menu_usuario(usuario_actual):
    while True:
        print("\n--- MENU USUARIO ---")
        print("1. Buscar pelicula o serie")
        print("2. RECOMENDADAS")
        print("3. Mi espacio personal")
        print("4. Cerrar sesion")
        opcion = pedir_numero("Opcion: ", 1, 4)

        if opcion == 1:
            seleccion = seleccionar(buscar())
            if seleccion:
                if ver_recurso(usuario_actual, seleccion) == "inicio":
                    return

        elif opcion == 2:
            todos = []
            hay_notas = False
            for categoria in categorias:
                for tipo in categorias[categoria]:
                    for nombre in categorias[categoria][tipo]:
                        todos.append((categoria, tipo, nombre))
                        if len(categorias[categoria][tipo][nombre]["calificaciones"]) > 0:
                            hay_notas = True

            if not hay_notas:
                recomendadas = random.sample(todos, min(10, len(todos)))
            else:
                puntuados = []
                for item in todos:
                    c, t, n = item
                    puntuados.append((promedio(categorias[c][t][n]), item))
                puntuados.sort(reverse=True)
                recomendadas = []
                for puntaje, item in puntuados[:10]:
                    recomendadas.append(item)

            print("\n*** RECOMENDADAS ***")
            seleccion = seleccionar(recomendadas)
            if seleccion:
                if ver_recurso(usuario_actual, seleccion) == "inicio":
                    return

        elif opcion == 3:
            while True:
                mi_lista = usuarios[usuario_actual]["espacio_personal"]
                print("\n--- MI ESPACIO PERSONAL ---")
                print("1. Ver mi lista")
                print("2. Agregar pelicula o serie")
                print("3. Reproducir")
                print("4. Eliminar")
                print("5. Volver")
                opcion_espacio = pedir_numero("Opcion: ", 1, 5)

                if opcion_espacio == 1:
                    mostrar_lista(mi_lista)

                elif opcion_espacio == 2:
                    seleccion = seleccionar(buscar())
                    if seleccion:
                        if seleccion in mi_lista:
                            print("Ya esta en su espacio personal.")
                        else:
                            mi_lista.append(seleccion)
                            print("Agregada a su espacio personal.")

                elif opcion_espacio == 3:
                    if len(mi_lista) == 0:
                        print("Su espacio personal esta vacio.")
                    else:
                        seleccion = seleccionar(mi_lista)
                        if seleccion:
                            if ver_recurso(usuario_actual, seleccion, True) == "inicio":
                                return

                elif opcion_espacio == 4:
                    if len(mi_lista) == 0:
                        print("Su espacio personal esta vacio.")
                    else:
                        seleccion = seleccionar(mi_lista)
                        if seleccion:
                            if pedir_si_no(f"¿Eliminar '{seleccion[2]}' de su lista? (S/N): "):
                                mi_lista.remove(seleccion)
                                print("Eliminada de su espacio personal.")

                else:
                    break

        else:
            print("Sesion cerrada con exito :)")
            return


try:
    while True:
        print("===== BIENVENIDO A LA PLATAFORMA ADSO =====")
        print("1. Iniciar sesion")
        print("2. Registrarse")
        print("3. Olvide mis credenciales")
        print("4. Salir")
        opcion = pedir_numero("Opcion: ", 1, 4)

        if opcion == 1:
            usuario = pedir_texto("Ingrese su usuario (cedula): ", 1, 30)

            # Primer ingreso del Admin: se genera y se muestra la contraseña
            if usuario == admin["usuario"] and admin["clave"] is None:
                admin["clave"] = generar_clave()
                print("Primer ingreso del administrador.")
                print(f"Su contraseña es: {admin['clave']}")
                print("Guardela, la necesitara para ingresar.")

            clave = pedir_texto("Ingrese su clave: ", 1, 100)

            if usuario == admin["usuario"] and clave == admin["clave"]:
                print("Sesion iniciada como administrador.")
                menu_admin()
            elif usuario in usuarios and clave == usuarios[usuario]["clave"]:
                print(f"Bienvenido {usuarios[usuario]['nombre']}.")
                usuarios[usuario]["ingreso"] = True
                acceso = True
                if usuarios[usuario]["bloqueado"]:
                    acceso = pantalla_bloqueo(usuario)
                if acceso:
                    menu_usuario(usuario)
            else:
                print("Error: usuario o clave incorrectos.")

        elif opcion == 2:
            print("--- REGISTRO ---")
            while True:
                nombre_completo = pedir_texto("Nombre completo: ", 1, 60)
                if nombre_completo.replace(" ", "").isalpha() and len(nombre_completo.split()) >= 2:
                    break
                print("Error: escriba nombre y apellido, solo con letras y espacios.")

            while True:
                cedula = pedir_texto("Cedula: ", 6, 10)
                if cedula.isdigit():
                    break
                print("Error: la cedula solo debe tener numeros.")

            if cedula in usuarios:
                print("Error: esa cedula ya esta registrada.")
            else:
                while True:
                    telefono = pedir_texto("Telefono: ", 7, 10)
                    if telefono.isdigit():
                        break
                    print("Error: el telefono solo debe tener numeros.")

                
                while True:
                    correo = pedir_texto("Correo electronico: ", 5, 50)

                    if " " in correo:
                        print("Error: el correo no puede tener espacios.")
                    elif "@" not in correo:
                        print("Error: el correo debe tener @.")
                    elif "." not in correo:
                        print("Error: el correo debe tener un punto.com, .net, .org, etc.")
                    else:
                        break


                usuarios[cedula] = {
                    "nombre": nombre_completo,
                    "telefono": telefono,
                    "correo": correo,
                    "clave": generar_clave(),
                    "token": generar_token(),
                    "vistos": 0,
                    "bloqueado": False,
                    "comprado": False,
                    "ingreso": False,
                    "espacio_personal": []
                }
                print("Registro exitoso. GUARDE ESTOS DATOS:")
                print(f"Usuario: {cedula}")
                print(f"Contraseña: {usuarios[cedula]['clave']}")
                print(f"Token de recuperacion: {usuarios[cedula]['token']}")

        elif opcion == 3:
            while True:
                cedula = pedir_texto("Ingrese su cedula: ", 6, 10)
                if cedula.isdigit():
                    break
                print("Error: la cedula solo debe tener numeros.")

            if cedula not in usuarios:
                print("Error: esa cedula no esta registrada.")
            elif cedula in solicitudes_credenciales:
                print("Ya tiene una solicitud pendiente.")
            else:
                solicitudes_credenciales.append(cedula)
                print("Solicitud enviada al administrador. Tenga a mano su token de recuperacion.")

        else:
            print("Gracias por usar el sistema. Hasta luego!")
            break

except ("ERROR"):
    print("Programa finalizado.")