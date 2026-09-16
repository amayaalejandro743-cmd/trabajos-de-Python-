carrito = {}

while True:

    articulo = input("Ingrese el nombre del artículo (o 'fin' para terminar la compra): ").strip()

    if articulo.lower() == "fin":
        break

    if articulo == "":
        print("El nombre no puede estar vacío.")
        continue

    precio = input("Ingrese el precio del artículo: ").strip()

    while not precio.replace(".", "", 1).isdigit():
        print("El precio debe ser un número.")
        precio = input("Ingrese el precio del artículo: ").strip()

    precio = float(precio)

    carrito[articulo] = precio

    print("Artículo agregado.")

print()
print("Lista de la compra")

total = 0

for articulo in carrito:
    print(articulo, "-", carrito[articulo])
    total = total + carrito[articulo]

print("Total:", round(total, 2))
