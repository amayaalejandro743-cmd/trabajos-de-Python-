#BASICO
#Se desea realizar un programa que pida el ingreso de los datos de n estudiantes (nombre y cedula) y 3 notas obtenidas
#por cada una de las siguientes asignaturas (matemáticas, español, religión, arte, inglés, sociales) 
#y sacar el promedio de las notas. Si las notas son mayores a 3 puntos de 5, se mandará un mensaje declarando 
#que el estudiante, ejemplo: JUNITO PEREZ, gano las asignaturas (xxxxxxx-xxx), 
#si el estudiante perdió alguna de las asignaturas el mensaje será: el estudiante perdió las asignaturas(xxxxx-xxx).
#Además, si el estudiante perdió más de tres asignaturas, se mostrará un mensaje indicando que perdió el año escolar,
#sino podrá habilitar las asignaturas perdidas y si el promedio de las notas obtenidas en las habilitaciones es superior a 3.5 de 5
#este habrá aprobado el año escolar y mandará un mensaje de felicitación.

materias = ("matemáticas", "español", "religión", "arte", "inglés", "sociales")
NOTA_MINIMA_APROBAR = 3.0

nombres = []
cedulas = []
notas_estudiantes = []
promedios = []
estados = []
perdio_anio = []

print("Bienvenido al programa de gestión de estudiantes")

while True:
    try:
        print("¿Desea registrar un nuevo estudiante? Digite (1-si desea registrar 1 nuevo estudiante)"
              " (2-para ver los resultados por estudiantes registrados) (3-para salir del programa)")
        opcion = int(input("Ingrese su elección: "))
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")
        continue

    if opcion not in (1, 2, 3):
        print("Opción inválida. Por favor, ingrese 1, 2 o 3.")
        continue

    if opcion == 1:
        while True:
            nombre = input("Ingrese el nombre del estudiante: ").strip()
            if nombre.replace(" ", "").isalpha() and nombre != "":
                break
            print("Nombre inválido. Por favor, ingrese solo letras.")

        while True:
            cedula = input("Ingrese la cédula del estudiante: ").strip()
            if not cedula.isdigit():
                print("Cédula inválida. Por favor, ingrese solo números.")
                continue
            if cedula in cedulas:
                print("Esa cédula ya está registrada. Ingrese una diferente.")
                continue
            break

        notas = []
        for materia in materias:
            notas_parciales = []
            for parcial in range(1, 4):
                while True:
                    try:
                        nota = float(input(f"Ingrese la nota {parcial} de {materia} (0-5): "))
                        if 0 <= nota <= 5:
                            notas_parciales.append(nota)
                            break
                        else:
                            print("Nota inválida. Debe estar entre 0 y 5.")
                    except ValueError:
                        print("Entrada inválida. Por favor, ingrese un número.")
            nota_materia = sum(notas_parciales) / len(notas_parciales)
            print(f"  Promedio de {materia}: {nota_materia:.2f}")
            notas.append(nota_materia)

        promedio = sum(notas) / len(notas)
        print(f"El promedio de {nombre} es: {promedio:.2f}")

        asignaturas_perdidas_idx = [i for i, nota in enumerate(notas) if nota < NOTA_MINIMA_APROBAR]
        asignaturas_perdidas = [materias[i] for i in asignaturas_perdidas_idx]

        estado = ""
        perdio = False

        if len(asignaturas_perdidas) == 0:
            print(f"{nombre} ganó todas las asignaturas.")
            estado = "Aprobado"
            perdio = False
        else:
            print(f"{nombre} perdió las asignaturas: {', '.join(asignaturas_perdidas)}")
            if len(asignaturas_perdidas) > 3:
                print(f"{nombre} perdió el año escolar.")
                estado = "Reprobado (más de 3 materias perdidas)"
                perdio = True
            else:
                habilitaciones = []
                for materia in asignaturas_perdidas:
                    while True:
                        try:
                            nota_habilitacion = float(input(f"Ingrese la nota de habilitación de {materia} (0-5): "))
                            if 0 <= nota_habilitacion <= 5:
                                habilitaciones.append(nota_habilitacion)
                                break
                            else:
                                print("Nota inválida. Debe estar entre 0 y 5.")
                        except ValueError:
                            print("Entrada inválida. Por favor, ingrese un número.")

                promedio_habilitaciones = sum(habilitaciones) / len(habilitaciones)

                if promedio_habilitaciones >= NOTA_MINIMA_APROBAR:
                    print(f"¡Felicidades! {nombre} aprobó el año escolar con un promedio de "
                          f"habilitación de {promedio_habilitaciones:.2f}.")
                    estado = f"Aprobado con habilitación ({promedio_habilitaciones:.2f})"
                    perdio = False
                    for idx, nota_hab in zip(asignaturas_perdidas_idx, habilitaciones):
                        notas[idx] = nota_hab
                    promedio = sum(notas) / len(notas)
                else:
                    print(f"{nombre} no aprobó el año escolar con un promedio de "
                          f"habilitación de {promedio_habilitaciones:.2f}.")
                    estado = f"Reprobado en habilitación ({promedio_habilitaciones:.2f})"
                    perdio = True

        nombres.append(nombre)
        cedulas.append(cedula)
        notas_estudiantes.append(notas)
        promedios.append(promedio)
        estados.append(estado)
        perdio_anio.append(perdio)

    elif opcion == 2:
        if not nombres:
            print("No hay estudiantes registrados.")
        else:
            for i in range(len(nombres)):
                print(f"Estudiante: {nombres[i]}, Cédula: {cedulas[i]}")
                for j in range(len(materias)):
                    print(f"  {materias[j]}: {notas_estudiantes[i][j]:.2f}")
                print(f"  Promedio final: {promedios[i]:.2f}")
                print(f"  Estado: {estados[i]}")
                print(f"  ¿Perdió el año?: {'Sí' if perdio_anio[i] else 'No'}")

    elif opcion == 3:
        print("Saliendo del programa. ¡Hasta luego!")
        break
      



        
