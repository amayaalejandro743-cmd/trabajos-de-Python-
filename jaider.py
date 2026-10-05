DESCUENTO_UMBRAL_ALTO = 1000000
DESCUENTO_UMBRAL_MEDIO = 500000
DESCUENTO_PORCENTAJE_ALTO = 0.10
DESCUENTO_PORCENTAJE_MEDIO = 0.05

NIVEL_MINIMO_DEFECTO = 5


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


def pedir_decimal(mensaje, minimo=None):
    valor = input(mensaje).strip()
    while not valor.replace(".", "", 1).isdigit():
        print("Debe ingresar un número válido.")
        valor = input(mensaje).strip()
    valor = float(valor)
    if minimo is not None:
        while valor < minimo:
            print("El valor debe ser mayor o igual a", minimo)
            valor = pedir_decimal(mensaje)
    return valor


def crear_inventario_inicial():
    inventario = {
        1: {"nombre": "Teclado", "categoria": "Tecnología", "precio": 45000, "stock": 20},
        2: {"nombre": "Mouse", "categoria": "Tecnología", "precio": 25000, "stock": 30},
        3: {"nombre": "Monitor", "categoria": "Tecnología", "precio": 380000, "stock": 8},
        4: {"nombre": "Cuaderno", "categoria": "Papelería", "precio": 3500, "stock": 100},
        5: {"nombre": "Lapicero", "categoria": "Papelería", "precio": 1200, "stock": 200},
        6: {"nombre": "Silla", "categoria": "Muebles", "precio": 150000, "stock": 12},
        7: {"nombre": "Escritorio", "categoria": "Muebles", "precio": 320000, "stock": 6},
    }
    return inventario


def valor_total_inventario(inventario):
    total = sum(datos["precio"] * datos["stock"] for datos in inventario.values())
    print("El valor total del inventario es: $", round(total, 2))


def productos_por_categoria(inventario, categoria):
    encontrados = {id_p: datos for id_p, datos in inventario.items() if datos["categoria"].lower() == categoria.lower()}

    if len(encontrados) == 0:
        print("No hay productos registrados en la categoría", categoria)
    else:
        print("Productos en la categoría", categoria, ":")
        for id_p, datos in encontrados.items():
            print("ID:", id_p, "- Nombre:", datos["nombre"], "- Precio:", datos["precio"], "- Stock:", datos["stock"])


def calcular_descuento(total):
    if total > DESCUENTO_UMBRAL_ALTO:
        return total * DESCUENTO_PORCENTAJE_ALTO
    elif total > DESCUENTO_UMBRAL_MEDIO:
        return total * DESCUENTO_PORCENTAJE_MEDIO
    else:
        return 0


def registrar_venta(inventario):

    carrito = {}

    while True:
        for 
        id_producto = pedir_entero("Ingrese el ID del producto (0 para terminar la venta): ")

        if id_producto == 0:
            break

        if id_producto not in inventario:
            print("No existe un producto con ese ID.")
            continue

        cantidad = pedir_entero("Ingrese la cantidad a vender: ", minimo=1)

        if cantidad > inventario[id_producto]["stock"]:
            print("No hay suficiente stock de", inventario[id_producto]["nombre"], "- Stock disponible:", inventario[id_producto]["stock"])
            print("Esa parte de la venta no pudo completarse.")
            continue

        if id_producto in carrito:
            carrito[id_producto] = carrito[id_producto] + cantidad
        else:
            carrito[id_producto] = cantidad

        print(cantidad, "unidad(es) de", inventario[id_producto]["nombre"], "agregada(s) a la venta.")

    if len(carrito) == 0:
        print("No se registró ningún producto en la venta.")
        return

    total = sum(inventario[id_p]["precio"] * cant for id_p, cant in carrito.items())

    descuento = calcular_descuento(total)
    total_con_descuento = total - descuento

    for id_p, cant in carrito.items():
        inventario[id_p]["stock"] = inventario[id_p]["stock"] - cant

    print("--- Resumen de la venta ---")
    for id_p, cant in carrito.items():
        print("-", inventario[id_p]["nombre"], "x", cant, "= $", inventario[id_p]["precio"] * cant)

    print("Subtotal: $", round(total, 2))
    print("Descuento aplicado: $", round(descuento, 2))
    print("Total a pagar: $", round(total_con_descuento, 2))


def productos_bajo_minimo(inventario, minimo=NIVEL_MINIMO_DEFECTO):

    bajos = {id_p: datos for id_p, datos in inventario.items() if datos["stock"] < minimo}

    if len(bajos) == 0:
        print("No hay productos por debajo del mínimo de", minimo, "unidades.")
    else:
        print("Productos por debajo del mínimo de", minimo, "unidades:")
        for id_p, datos in bajos.items():
            print("ID:", id_p, "- Nombre:", datos["nombre"], "- Stock actual:", datos["stock"])


def reabastecer_producto(inventario):

    id_producto = pedir_entero("Ingrese el ID del producto a reabastecer: ")

    if id_producto in inventario:

        cantidad = pedir_entero("Ingrese la cantidad a agregar: ", minimo=1)
        inventario[id_producto]["stock"] = inventario[id_producto]["stock"] + cantidad
        print("Stock actualizado. Nuevo stock de", inventario[id_producto]["nombre"], ":", inventario[id_producto]["stock"])

    else:

        print("Ese ID no existe todavía. Se registrará como producto nuevo.")

        nombre = pedir_texto("Nombre del producto: ")
        categoria = pedir_texto("Categoría del producto: ")
        precio = pedir_decimal("Precio del producto: ", minimo=0)
        cantidad = pedir_entero("Cantidad inicial en stock: ", minimo=0)

        inventario[id_producto] = {"nombre": nombre, "categoria": categoria, "precio": precio, "stock": cantidad}
        print("Producto nuevo agregado correctamente.")


def mostrar_menu():
    print()
    print("       MENÚ DE VENTAS")
    print("1. Valor total del inventario")
    print("2. Consultar productos por categoría")
    print("3. Registrar una venta")
    print("4. Ver productos bajo el mínimo")
    print("5. Reabastecer o agregar producto")
    print("6. Salir")


def main():

    inventario = crear_inventario_inicial()

    while True:

        mostrar_menu()
        opcion = input("Escoja una opción: ").strip()

        if opcion == "1":
            valor_total_inventario(inventario)

        elif opcion == "2":
            categoria = pedir_texto("Ingrese la categoría a consultar: ")
            productos_por_categoria(inventario, categoria)

        elif opcion == "3":
            registrar_venta(inventario)

        elif opcion == "4":
            usar_defecto = input("¿Usar el mínimo por defecto (" + str(NIVEL_MINIMO_DEFECTO) + ")? (si/no): ").strip().lower()

            if usar_defecto == "si":
                productos_bajo_minimo(inventario)
            else:
                minimo = pedir_entero("Ingrese el nivel mínimo a consultar: ", minimo=0)
                productos_bajo_minimo(inventario, minimo)

        elif opcion == "5":
            reabastecer_producto(inventario)

        elif opcion == "6":
            print("Programa terminado.")
            break

        else:
            print("Opción incorrecta. Escoja del 1 al 6.")


main()
