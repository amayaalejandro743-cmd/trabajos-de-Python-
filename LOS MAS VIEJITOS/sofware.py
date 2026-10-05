import random

paises = ("Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Ecuador", "Uruguay", "Paraguay")
print("="*60)
print("         SORTEO COPA DE PROGRAMACIÓN ADSO - FICHA 3409199")
print("="*60)
lista_nombres_aprendices = []
lista_cedulas_aprendices = []

for numero_aprendiz in range(1, 17):
    while True:
        print(f"\nIngrese el nombre completo del aprendiz # {numero_aprendiz}: ")
        nombre_ingresado = input().strip()
        nombre_sin_espacios = nombre_ingresado.replace(" ", "")
        if nombre_sin_espacios.isalpha() and nombre_ingresado != "":
            break
        print("Nombre inválido. Por favor, ingrese solo letras.")
        print("")

    while True:
        try:
            print(f"\nIngrese la cédula del aprendiz # {numero_aprendiz}: ")
            cedula_ingresada = int(input())
            cantidad_de_digitos = len(str(cedula_ingresada))
            if cantidad_de_digitos < 8 or cantidad_de_digitos > 11:
                print("La cédula solo puede tener de 8 a 11 dígitos.")
                print("")
                continue
            if cedula_ingresada in lista_cedulas_aprendices:
                print("Esa cédula ya está registrada. Ingrese una diferente.")
                print("")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
            print("")

    lista_nombres_aprendices.append(nombre_ingresado)
    lista_cedulas_aprendices.append(cedula_ingresada)

orden_aleatorio_aprendices = list(range(16))
random.shuffle(orden_aleatorio_aprendices)

nombre_integrante_uno = []
cedula_integrante_uno = []
nombre_integrante_dos = []
cedula_integrante_dos = []

for numero_seleccion in range(8):
    posicion_primer_integrante = numero_seleccion * 2
    posicion_segundo_integrante = numero_seleccion * 2 + 1

    indice_primer_integrante = orden_aleatorio_aprendices[posicion_primer_integrante]
    indice_segundo_integrante = orden_aleatorio_aprendices[posicion_segundo_integrante]

    nombre_integrante_uno.append(lista_nombres_aprendices[indice_primer_integrante])
    cedula_integrante_uno.append(lista_cedulas_aprendices[indice_primer_integrante])
    nombre_integrante_dos.append(lista_nombres_aprendices[indice_segundo_integrante])
    cedula_integrante_dos.append(lista_cedulas_aprendices[indice_segundo_integrante])

print("="*60)
print("          SORTEO DE SELECCIONES")
print("="*60)
for numero_seleccion in range(8):
    nombre_pais = paises[numero_seleccion]
    print(f"{nombre_pais}: {nombre_integrante_uno[numero_seleccion]} "
          f"(C.C. {cedula_integrante_uno[numero_seleccion]}) y "
          f"{nombre_integrante_dos[numero_seleccion]} "
          f"(C.C. {cedula_integrante_dos[numero_seleccion]})")

selecciones_en_competencia = list(range(8))
numero_de_fase = 1

while len(selecciones_en_competencia) > 2:
    cantidad_selecciones = len(selecciones_en_competencia)
    random.shuffle(selecciones_en_competencia)

    print("="*60)
    print(f"            FASE {numero_de_fase} ({cantidad_selecciones} SELECCIONES)")
    print("="*60)

    puntos_de_la_fase = [0] * cantidad_selecciones

    for posicion_actual in range(cantidad_selecciones):
        posicion_siguiente = (posicion_actual + 1) % cantidad_selecciones

        indice_primer_equipo = selecciones_en_competencia[posicion_actual]
        indice_segundo_equipo = selecciones_en_competencia[posicion_siguiente]

        nombre_primer_equipo = paises[indice_primer_equipo]
        nombre_segundo_equipo = paises[indice_segundo_equipo]

        print(f"Partido: {nombre_primer_equipo} vs {nombre_segundo_equipo}")
        print(f"1-Ganó {nombre_primer_equipo}")
        print(f"2-Ganó {nombre_segundo_equipo}")
        print("3-Empate")

        while True:
            try:
                resultado_partido = int(input("Ingrese el resultado: "))
            except ValueError:
                print("Entrada inválida. Ingrese un número.")
                print("")
                continue
            if resultado_partido not in (1, 2, 3):
                print("Opción inválida. Ingrese 1, 2 o 3.")
                print("")
                continue
            break

        if resultado_partido == 1:
            puntos_de_la_fase[posicion_actual] = puntos_de_la_fase[posicion_actual] + 3
            print(f"Ganó {nombre_primer_equipo}")
        elif resultado_partido == 2:
            puntos_de_la_fase[posicion_siguiente] = puntos_de_la_fase[posicion_siguiente] + 3
            print(f"Ganó {nombre_segundo_equipo}")
        else:
            puntos_de_la_fase[posicion_actual] = puntos_de_la_fase[posicion_actual] + 1
            puntos_de_la_fase[posicion_siguiente] = puntos_de_la_fase[posicion_siguiente] + 1
            print("Empate")

    for pasada in range(cantidad_selecciones):
        for posicion in range(0, cantidad_selecciones - pasada - 1):
            puntos_actuales = puntos_de_la_fase[posicion]
            puntos_siguientes = puntos_de_la_fase[posicion + 1]
            if puntos_actuales < puntos_siguientes:
                puntos_de_la_fase[posicion] = puntos_siguientes
                puntos_de_la_fase[posicion + 1] = puntos_actuales
                equipo_actual = selecciones_en_competencia[posicion]
                equipo_siguiente = selecciones_en_competencia[posicion + 1]
                selecciones_en_competencia[posicion] = equipo_siguiente
                selecciones_en_competencia[posicion + 1] = equipo_actual

    print("="*60)
    print(f"           Tabla de posiciones FASE {numero_de_fase}:")
    print("="*60)
    for posicion in range(cantidad_selecciones):
        nombre_del_equipo = paises[selecciones_en_competencia[posicion]]
        puntos_del_equipo = puntos_de_la_fase[posicion]
        print(f"{posicion + 1}) {nombre_del_equipo} - {puntos_del_equipo} puntos")
        print("-"*60)

    cupos_disponibles = cantidad_selecciones // 2
    puntaje_del_ultimo_cupo = puntos_de_la_fase[cupos_disponibles - 1]

    posiciones_con_ese_puntaje = []
    for posicion in range(cantidad_selecciones):
        if puntos_de_la_fase[posicion] == puntaje_del_ultimo_cupo:
            posiciones_con_ese_puntaje.append(posicion)

    posicion_mas_lejana_empatada = max(posiciones_con_ese_puntaje)

    if posicion_mas_lejana_empatada < cupos_disponibles:
        selecciones_clasificadas = selecciones_en_competencia[0:cupos_disponibles]
    else:
        primera_posicion_empatada = min(posiciones_con_ese_puntaje)
        cantidad_clasificada_directo = primera_posicion_empatada
        cupos_en_disputa = cupos_disponibles - cantidad_clasificada_directo

        grupo_empatado = []
        for posicion in posiciones_con_ese_puntaje:
            grupo_empatado.append(selecciones_en_competencia[posicion])

        selecciones_clasificadas = selecciones_en_competencia[0:cantidad_clasificada_directo]

        numero_de_intento = 0
        while True:
            numero_de_intento = numero_de_intento + 1
            cantidad_equipos_empatados = len(grupo_empatado)

            print("="*60)
            print(f"DESEMPATE - {cantidad_equipos_empatados} SELECCIONES "
                  f"DISPUTAN {cupos_en_disputa} CUPO(S)")
            print("="*60)

            puntos_del_desempate = [0] * cantidad_equipos_empatados

            for primera_posicion in range(cantidad_equipos_empatados):
                for segunda_posicion in range(primera_posicion + 1, cantidad_equipos_empatados):
                    indice_primer_equipo = grupo_empatado[primera_posicion]
                    indice_segundo_equipo = grupo_empatado[segunda_posicion]
                    nombre_primer_equipo = paises[indice_primer_equipo]
                    nombre_segundo_equipo = paises[indice_segundo_equipo]

                    print("="*60)
                    print(f"Partido de desempate: {nombre_primer_equipo} vs {nombre_segundo_equipo}")
                    print(f"1-Ganó {nombre_primer_equipo}")
                    print(f"2-Ganó {nombre_segundo_equipo}")
                    print("3-Empate")

                    while True:
                        try:
                            resultado_partido = int(input("Ingrese el resultado: "))
                        except ValueError:
                            print("Entrada inválida. Ingrese un número.")
                            print("")
                            continue
                        if resultado_partido not in (1, 2, 3):
                            print("Opción inválida. Ingrese 1, 2 o 3.")
                            print("")
                            continue
                        break

                    if resultado_partido == 1:
                        puntos_del_desempate[primera_posicion] = puntos_del_desempate[primera_posicion] + 3
                    elif resultado_partido == 2:
                        puntos_del_desempate[segunda_posicion] = puntos_del_desempate[segunda_posicion] + 3
                    else:
                        puntos_del_desempate[primera_posicion] = puntos_del_desempate[primera_posicion] + 1
                        puntos_del_desempate[segunda_posicion] = puntos_del_desempate[segunda_posicion] + 1

            for pasada in range(cantidad_equipos_empatados):
                for posicion in range(0, cantidad_equipos_empatados - pasada - 1):
                    puntos_actuales = puntos_del_desempate[posicion]
                    puntos_siguientes = puntos_del_desempate[posicion + 1]
                    if puntos_actuales < puntos_siguientes:
                        puntos_del_desempate[posicion] = puntos_siguientes
                        puntos_del_desempate[posicion + 1] = puntos_actuales
                        equipo_actual = grupo_empatado[posicion]
                        equipo_siguiente = grupo_empatado[posicion + 1]
                        grupo_empatado[posicion] = equipo_siguiente
                        grupo_empatado[posicion + 1] = equipo_actual

            print("="*60)
            print("         Tabla de posiciones del desempate:")
            print("="*60)
            for posicion in range(cantidad_equipos_empatados):
                nombre_del_equipo = paises[grupo_empatado[posicion]]
                puntos_del_equipo = puntos_del_desempate[posicion]
                print(f"{posicion + 1}) {nombre_del_equipo} - {puntos_del_equipo} puntos")
                print("-"*60)

            puntaje_minimo_del_desempate = puntos_del_desempate[cupos_en_disputa - 1]
            posiciones_con_puntaje_minimo = []
            for posicion in range(cantidad_equipos_empatados):
                if puntos_del_desempate[posicion] == puntaje_minimo_del_desempate:
                    posiciones_con_puntaje_minimo.append(posicion)

            posicion_mas_lejana_del_desempate = max(posiciones_con_puntaje_minimo)

            if posicion_mas_lejana_del_desempate < cupos_en_disputa:
                selecciones_clasificadas = selecciones_clasificadas + grupo_empatado[0:cupos_en_disputa]
                break
            elif numero_de_intento >= 5:
                print("\nEmpate persistente tras varios desempates. Se define por sorteo aleatorio.")
                random.shuffle(grupo_empatado)
                selecciones_clasificadas = selecciones_clasificadas + grupo_empatado[0:cupos_en_disputa]
                break
            else:
                primera_posicion_del_desempate = min(posiciones_con_puntaje_minimo)
                cantidad_asegurada_del_desempate = primera_posicion_del_desempate
                selecciones_clasificadas = selecciones_clasificadas + grupo_empatado[0:cantidad_asegurada_del_desempate]
                cupos_en_disputa = cupos_en_disputa - cantidad_asegurada_del_desempate

                nuevo_grupo_empatado = []
                for posicion in posiciones_con_puntaje_minimo:
                    nuevo_grupo_empatado.append(grupo_empatado[posicion])
                grupo_empatado = nuevo_grupo_empatado

    nombres_de_los_clasificados = []
    for indice_equipo in selecciones_clasificadas:
        nombres_de_los_clasificados.append(paises[indice_equipo])

    print("="*60)
    print(f"          Clasifican a la siguiente fase: {', '.join(nombres_de_los_clasificados)}")

    selecciones_en_competencia = selecciones_clasificadas
    numero_de_fase = numero_de_fase + 1

print("="*60)
print("          GRAN FINAL")
print("="*60)

indice_finalista_uno = selecciones_en_competencia[0]
indice_finalista_dos = selecciones_en_competencia[1]

while True:
    nombre_finalista_uno = paises[indice_finalista_uno]
    nombre_finalista_dos = paises[indice_finalista_dos]

    print(" ")
    print(f"\nPartido Final: {nombre_finalista_uno} vs {nombre_finalista_dos}")
    print(f"1-Ganó {nombre_finalista_uno}")
    print(f"2-Ganó {nombre_finalista_dos}")
    print("3-Empate")

    while True:
        try:
            resultado_final = int(input("Ingrese el resultado: "))
        except ValueError:
            print("Entrada inválida. Ingrese un número.")
            print("")
            continue
        if resultado_final not in (1, 2, 3):
            print("Opción inválida. Ingrese 1, 2 o 3.")
            print("")
            continue
        break

    if resultado_final != 3:
        break
    print("Empate en la final. Se juega un partido de desempate.")

if resultado_final == 1:
    indice_campeon = indice_finalista_uno
else:
    indice_campeon = indice_finalista_dos

nombre_del_campeon = paises[indice_campeon]

print(" ")
print(f"¡{nombre_del_campeon.upper()} ES LA SELECCIÓN CAMPEONA DE LA COPA ADSO!")
print(f"Integrantes campeones: {nombre_integrante_uno[indice_campeon]} "
      f"(C.C. {cedula_integrante_uno[indice_campeon]}) y "
      f"{nombre_integrante_dos[indice_campeon]} "
      f"(C.C. {cedula_integrante_dos[indice_campeon]})")
