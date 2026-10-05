nombre_estudiantes = []
edad_estudiantes = []
#ingreso de datos
while True:
    print("ingrese el nombre del estudiante: (0 para salir) ")
    estudiante = str(input())

    if estudiante == "0":
        break

    print("digite la edad del estudiante: ")
    edad = int(input())
    while edad < 0 or edad > 120:
        print("la edad debe estar entre 0 y 120, digite nuevamente: ")
        edad = int(input())

    nombre_estudiantes.append(estudiante)
    edad_estudiantes.append(edad)
#estudiantes mayores de edad    
print(" Estudiantes mayores de edad")
i = 0
while i < len(nombre_estudiantes):
    if edad_estudiantes[i] >= 18:
        print(nombre_estudiantes[i])
    i = i + 1

edad_mayor = 0
i = 0
while i < len(edad_estudiantes):
    if edad_estudiantes[i] > edad_mayor:
        edad_mayor = edad_estudiantes[i]
    i = i + 1
#los mas viejos
print("Estudiante(s) con mayor edad")
i = 0
while i < len(nombre_estudiantes):
    if edad_estudiantes[i] == edad_mayor:
        print(nombre_estudiantes[i])
    i = i + 1