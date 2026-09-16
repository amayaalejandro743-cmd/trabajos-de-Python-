productos = []

cantidad_productos = input("¿Cuántos productos va a registrar? ").strip()

while not cantidad_productos.isdigit() or int(cantidad_productos) <= 0:
    print("Debe ingresar un número mayor que 0.")
    cantidad_productos = input("¿Cuántos productos va a registrar? ").strip()

cantidad_productos = int(cantidad_productos)

contador = 0

while contador < cantidad_productos:

    print("--- Producto", contador + 1, "---")

    codigo = input("Código del producto: ").strip()

    while codigo == "":
        print("El código no puede estar vacío.")
        codigo = input("Código del producto: ").strip()

    codigo_repetido = False

    for producto in productos:
        if producto["codigo"] == codigo:
            codigo_repetido = True

    if codigo_repetido:
        print("Ese código ya existe, ingrese los datos de nuevo.")
        continue

    nombre = input("Nombre del producto: ").strip()

    while nombre == "":
        print("El nombre no puede estar vacío.")
        nombre = input("Nombre del producto: ").strip()

    precio = input("Precio del producto: ").strip()

    while not precio.replace(".", "", 1).isdigit():
        print("El precio debe ser un número.")
        precio = input("Precio del producto: ").strip()

    precio = float(precio)

    stock = input("Cantidad en stock: ").strip()

    while not stock.isdigit():
        print("El stock debe ser un número entero.")
        stock = input("Cantidad en stock: ").strip()

    stock = int(stock)

    productos.append({"codigo": codigo, "nombre": nombre, "precio": precio, "stock": stock})

    contador = contador + 1


while True:

    print()
    print("       MENÚ DE PRODUCTOS")
    print("1. Mostrar todos los productos")
    print("2. Buscar un producto")
    print("3. Agregar stock")
    print("4. Vender un producto")
    print("5. Encontrar el producto más caro")
    print("6. Calcular el valor total del inventario")
    print("7. Salir")

    opcion = input("Escoja una opción: ").strip()

    if opcion == "1":

        if len(productos) == 0:
            print("No hay productos registrados.")

        else:
            for producto in productos:
                print("Código:", producto["codigo"], "- Nombre:", producto["nombre"], "- Precio:", producto["precio"], "- Stock:", producto["stock"])

    elif opcion == "2":

        codigo_buscar = input("Ingrese el código del producto: ").strip()

        encontrado = False

        for producto in productos:
            if producto["codigo"] == codigo_buscar:
                print("Código:", producto["codigo"])
                print("Nombre:", producto["nombre"])
                print("Precio:", producto["precio"])
                print("Stock:", producto["stock"])
                encontrado = True

        if encontrado == False:
            print("No existe un producto con ese código.")

    elif opcion == "3":

        codigo_buscar = input("Ingrese el código del producto: ").strip()

        encontrado = False

        for producto in productos:
            if producto["codigo"] == codigo_buscar:
                encontrado = True

                cantidad_agregar = input("Ingrese la cantidad a agregar: ").strip()

                while not cantidad_agregar.isdigit() or int(cantidad_agregar) <= 0:
                    print("Debe ingresar un número entero mayor que 0.")
                    cantidad_agregar = input("Ingrese la cantidad a agregar: ").strip()

                cantidad_agregar = int(cantidad_agregar)

                producto["stock"] = producto["stock"] + cantidad_agregar

                print("Stock actualizado. Nuevo stock:", producto["stock"])

        if encontrado == False:
            print("No existe un producto con ese código.")

    elif opcion == "4":

        codigo_buscar = input("Ingrese el código del producto: ").strip()

        encontrado = False

        for producto in productos:
            if producto["codigo"] == codigo_buscar:
                encontrado = True

                cantidad_vender = input("Ingrese la cantidad a vender: ").strip()

                while not cantidad_vender.isdigit() or int(cantidad_vender) <= 0:
                    print("Debe ingresar un número entero mayor que 0.")
                    cantidad_vender = input("Ingrese la cantidad a vender: ").strip()

                cantidad_vender = int(cantidad_vender)

                if cantidad_vender > producto["stock"]:
                    print("No hay suficiente stock. Stock disponible:", producto["stock"])

                else:
                    producto["stock"] = producto["stock"] - cantidad_vender
                    total_venta = cantidad_vender * producto["precio"]
                    print("Venta realizada. Total a pagar:", round(total_venta, 2))
                    print("Stock restante:", producto["stock"])

        if encontrado == False:
            print("No existe un producto con ese código.")

    elif opcion == "5":

        if len(productos) == 0:
            print("No hay productos registrados.")

        else:
            producto_mas_caro = productos[0]

            for producto in productos:
                if producto["precio"] > producto_mas_caro["precio"]:
                    producto_mas_caro = producto

            print("El producto más caro es:", producto_mas_caro["nombre"], "- Precio:", producto_mas_caro["precio"])

    elif opcion == "6":

        valor_total = 0

        for producto in productos:
            valor_total = valor_total + (producto["precio"] * producto["stock"])

        print("El valor total del inventario es:", round(valor_total, 2))

    elif opcion == "7":
        print("Programa terminado.")
        break

    else:
        print("Opción incorrecta. Escoja del 1 al 7.")
