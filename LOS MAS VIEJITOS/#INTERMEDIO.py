materias = ("matemáticas", "español", "religión", "arte", "inglés", "sociales")
grados = (6, 7, 8, 9, 10, 11)
NOTA_MINIMA_APROBAR = 3.0
HABILITACION_APROBAR = 3.5

grado6 = []
grado7 = []
grado8 = []
grado9 = []
grado10 = []
grado11 = []

grados_listas = [grado6, grado7, grado8, grado9, grado10, grado11]
profesores_nombres = []
profesores_cedulas = []
profesores_sexos = []
profesores_materias = []
profesores_grados = []
profesores_director = []

print("BIENVENIDO A EL PROGRAMA ACADEMIGO DEL COLEGIO ADSO")
print(" ")
print("MENU DE OPCIONES")
print(" ")

while True:
    try:
        print("""1-REGISTRAR ESTUDIANTES DE UN GRADO
2-REGISTRAR PROFESOR PARA CADA MATERIA
3-REPORTE
4-SALIR""")
        opcion = int(input("ingrese 1, 2, 3 'o' 4 seleccion: "))
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")
        print(" ")
        continue

    if opcion not in (1, 2, 3, 4):
        print("Opción inválida. Por favor, ingrese 1, 2, 3 o 4.")
        print(" ")
        continue

    if opcion == 1:
        while True:
            try:
                print("Grados disponibles: 6, 7, 8, 9, 10, 11")
                grado = int(input("Ingrese el grado: "))
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
                continue
            if grado not in grados:
                print("Grado inválido. Por favor, ingrese un grado real.")
                continue
            break

        indice_grado = grados.index(grado)

        while True:
            while True:
                nombre = input("Ingrese el nombre del estudiante: ").strip()
                if nombre.replace(" ", "").isalpha() and nombre != "":
                    break
                print("Nombre inválido. Por favor, ingrese solo letras.")

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

            asignaturas_perdidas_idx = [i for i, nota in enumerate(notas) if nota <= NOTA_MINIMA_APROBAR]
            asignaturas_ganadas_idx = [i for i, nota in enumerate(notas) if nota > NOTA_MINIMA_APROBAR]
            asignaturas_perdidas = [materias[i] for i in asignaturas_perdidas_idx]
            asignaturas_ganadas = [materias[i] for i in asignaturas_ganadas_idx]

            estado = ""
            perdio = False

            if len(asignaturas_perdidas) == 0:
                print(f"El estudiante {nombre.upper()} ganó las asignaturas ({', '.join(asignaturas_ganadas)}).")
                estado = "Aprobado"
                perdio = False
            else:
                print(f"El estudiante {nombre.upper()} perdió las asignaturas ({', '.join(asignaturas_perdidas)}).")
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

                    if promedio_habilitaciones > HABILITACION_APROBAR:
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

            estudiante = [nombre, notas, promedio, estado, perdio]
            grados_listas[indice_grado].append(estudiante)

            while True:
                otro = input(f"¿Desea registrar otro estudiante en el grado {grado}? (s/n): ").strip().lower()
                if otro in ("s", "n"):
                    break
                print("Respuesta inválida. Ingrese 's' o 'n'.")
            if otro == "n":
                break

    elif opcion == 2:
        while True:
            try:
                print("Grados disponibles: 6, 7, 8, 9, 10, 11")
                grado = int(input("Ingrese el grado: "))
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
                continue
            if grado not in grados:
                print("Grado inválido. Por favor, ingrese un grado real.")
                continue
            break

        print("Materias disponibles:")
        for i, materia in enumerate(materias, start=1):
            print(f"  {i}-{materia}")

        while True:
            try:
                numero_materia = int(input("Ingrese el número de la materia: "))
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
                continue
            if numero_materia not in range(1, len(materias) + 1):
                print("Número de materia inválido.")
                continue
            break

        materia = materias[numero_materia - 1]

        while True:
            nombre_profesor = input("Ingrese el nombre del profesor: ").strip()
            if nombre_profesor.replace(" ", "").isalpha() and nombre_profesor != "":
                break
            print("Nombre inválido. Por favor, ingrese solo letras.")

        while True:
            cedula_profesor = input("Ingrese la cédula del profesor: ").strip()
            if not cedula_profesor.isdigit():
                print("Cédula inválida. Por favor, ingrese solo números.")
                continue
            break

        while True:
            sexo_profesor = input("Ingrese el sexo del profesor (M/F): ").strip().upper()
            if sexo_profesor in ("M", "F"):
                break
            print("Sexo inválido. Ingrese M o F.")

        indice_existente = None
        for i in range(len(profesores_nombres)):
            if profesores_materias[i] == materia and profesores_grados[i] == grado:
                indice_existente = i
                break

        if indice_existente is not None:
            print(f"Ya había un profesor para {materia} en el grado {grado} "
                  f"({profesores_nombres[indice_existente]}). Se actualiza.")
            profesores_nombres[indice_existente] = nombre_profesor
            profesores_cedulas[indice_existente] = cedula_profesor
            profesores_sexos[indice_existente] = sexo_profesor
        else:
            profesores_nombres.append(nombre_profesor)
            profesores_cedulas.append(cedula_profesor)
            profesores_sexos.append(sexo_profesor)
            profesores_materias.append(materia)
            profesores_grados.append(grado)
            profesores_director.append(False)
            indice_existente = len(profesores_nombres) - 1

        while True:
            es_director = input(f"¿Este profesor es el director de grupo del grado {grado}? (s/n): ").strip().lower()
            if es_director in ("s", "n"):
                break
            print("Respuesta inválida. Ingrese 's' o 'n'.")

        if es_director == "s":
            for i in range(len(profesores_director)):
                if profesores_grados[i] == grado and profesores_director[i] and i != indice_existente:
                    print(f"El grado {grado} ya tenía como director de grupo a {profesores_nombres[i]}. Se reemplaza.")
                    profesores_director[i] = False
            profesores_director[indice_existente] = True
            print(f"{nombre_profesor} quedó registrado como director de grupo del grado {grado}.")

    elif opcion == 3:
        while True:
            print(""" REPORTE
1-SITUACIÓN DE LOS ESTUDIANTES
2-PROFESORES REGISTRADOS POR GRADO
3-REPORTE GENERAL (TODOS LOS GRADOS)""")
            try:
                sub_opcion = int(input("ingrese 1, 2 'o' 3 seleccion: "))
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
                continue
            if sub_opcion not in (1, 2, 3):
                print("Opción inválida. Por favor, ingrese 1, 2 o 3.")
                continue
            break

        if sub_opcion in (1, 2):
            while True:
                try:
                    print("Grados disponibles: 6, 7, 8, 9, 10, 11")
                    grado = int(input("Ingrese el grado: "))
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")
                    continue
                if grado not in grados:
                    print("Grado inválido. Por favor, ingrese un grado real.")
                    continue
                break
            grados_a_mostrar = [grado]
        else:
            grados_a_mostrar = list(grados)

        for grado in grados_a_mostrar:
            indice_grado = grados.index(grado)

            if sub_opcion in (1, 3):
                lista_estudiantes = grados_listas[indice_grado]

                print(f" SITUACIÓN DE LOS ESTUDIANTES - GRADO {grado} ")
                if not lista_estudiantes:
                    print("No hay estudiantes registrados en este grado.")
                else:
                    for estudiante in lista_estudiantes:
                        nombre, notas, promedio, estado, perdio = estudiante
                        print(f"\nEstudiante: {nombre}")
                        for j in range(len(materias)):
                            print(f"  {materias[j]}: {notas[j]:.2f}")
                        print(f"  Promedio final: {promedio:.2f}")
                        print(f"  Estado: {estado}")
                        print(f"  ¿Perdió el año?: {'Sí' if perdio else 'No'}")

            if sub_opcion in (2, 3):
                print(f"PROFESORES REGISTRADOS - GRADO {grado} ")

                director_nombre = None
                for i in range(len(profesores_director)):
                    if profesores_grados[i] == grado and profesores_director[i]:
                        director_nombre = profesores_nombres[i]
                        break
                print(f"Director de grupo: {director_nombre if director_nombre else 'no asignado'}")

                print("Profesores por materia:")
                for materia in materias:
                    encontrado = False
                    for i in range(len(profesores_materias)):
                        if profesores_materias[i] == materia and profesores_grados[i] == grado:
                            print(f"  {materia}: {profesores_nombres[i]}, "
                                  f"Cédula: {profesores_cedulas[i]}, Sexo: {profesores_sexos[i]}")
                            encontrado = True
                            break
                    if not encontrado:
                        print(f"  {materia}: no asignado")

    elif opcion == 4:
        print("Saliendo del programa. ¡Hasta luego!")
        break
