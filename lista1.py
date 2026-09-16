precios = {
    "Cafe": 1.35,
    "Platano": 0.80,
    "Aguacate": 0.85,
    "Pepino": 0.70
}

while True:
    print("productos:")
    print("="*10)
    for p in precios:
        print(p)

    producto = input("Ingrese el nombre del producto (o 'salir' para terminar): ").strip()

    if producto.lower() == "salir":
        print("Programa terminado.")
        break

    if producto in precios:

        kilos = input("Ingrese la cantidad de kilos: ").strip()

        while not kilos.replace(".", "", 1).isdigit():
            print("La cantidad debe ser un número.")
            kilos = input("Ingrese la cantidad de kilos: ").strip()

        kilos = float(kilos)

        precio_total = precios[producto] * kilos

        print("El precio de", kilos, "kg de", producto, "es:", round(precio_total, 2))

    else:
        print("Ese producto no está disponible en la tienda.")
        
