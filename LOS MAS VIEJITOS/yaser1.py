vector1 = [0, 0, 0, 0, 0]
vector2 = [0, 0, 0, 0, 0]

while True:
    try:
        print("¿Qué vector desea llenar primero?")
        print("1. Vector 1")
        print("2. Vector 2")
        vec = int(input("Ingrese su opción: "))
        print(" ")
        if vec == 1 or vec == 2:
            break
        else:
            print("Error: solo puede ingresar 1 o 2.")
    except ValueError:
        print(" ")
        print("Error: debe ingresar un número entero (1 o 2).")


if vec == 1:
    primero, nombre_primero = vector1, "Vector 1"
    segundo, nombre_segundo = vector2, "Vector 2"
else:
    primero, nombre_primero = vector2, "Vector 2"
    segundo, nombre_segundo = vector1, "Vector 1"

print(f"Llenando el {nombre_primero}")
for i in range(5):
    while True:
        try:
            numero = int(input(f"Ingrese el número {i + 1} (entre 0 y 9): "))
            if 0 <= numero <= 9:
                primero[i] = numero
                break
            else:
                print("Error: el número debe estar entre 0 y 9.")
        except ValueError:
            print("Error: debe ingresar un número entero.")

print(f"Llenando el {nombre_segundo}")
for i in range(5):
    while True:
        try:
            numero = int(input(f"Ingrese el número {i + 1} (entre 0 y 9): "))
            if 0 <= numero <= 9:
                segundo[i] = numero
                break
            else:
                print("Error: el número debe estar entre 0 y 9.")
        except ValueError:
            print("Error: debe ingresar un número entero.")

print("Vector 1:", vector1)
print("Vector 2:", vector2)

vector3 = vector1 + vector2
vector3.sort()

print("Vector 3 (unión ordenada de Vector 1 y Vector 2):")
print(vector3)

print("Cantidad de veces que aparece cada número:")
ya_mostrados = []
for numero in vector3:
    if numero not in ya_mostrados:
        cantidad = vector3.count(numero)
        print(f"El número {numero} aparece {cantidad} vez/veces")
        ya_mostrados.append(numero)
