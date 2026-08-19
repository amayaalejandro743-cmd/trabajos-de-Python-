cupos_adso = 40
cupos_tecnico = 34
cupos_multimedia = 40

codigo_persona = []
nombre = []
apellido = []
edad = []
programa_formacion = []
validacioon_caracteres = 10

print("Bienvenido al sistema de control de cupos del SENA")

# modo_inscripcion en True significa que el programa está inscribiendo personas.
# modo_inscripcion en False significa que el programa está mostrando el menú final.
modo_inscripcion = True
seguir_programa = True

while seguir_programa:

    if modo_inscripcion == True:
        print("seleccione el programa de formación al que desea inscribirse:")
        print("1. Análisis y Desarrollo de Sistemas de Información")
        print("2. Técnico en programación")
        print("3. Multimedia")

        while True:
            try:
                programa = int(input("Ingrese el número del programa a inscribirse: "))
                if programa < 1 or programa > 3:
                    print("Opción inválida. Por favor, seleccione un programa válido.")
                else:
                    break
            except:
                print("Debe ingresar solo números.")

        if programa == 1:
            if cupos_adso > 0:
                nombre_persona = input("Ingrese el nombre de la persona: ")
                while nombre_persona.isalpha() == False:
                    print("El nombre solo debe contener letras.")
                    nombre_persona = input("Ingrese el nombre de la persona: ")
                nombre.append(nombre_persona)
                print(" ")

                apellido_persona = input("Ingrese los apellidos de la persona (puede ingresar los dos separados por un espacio): ")
                while apellido_persona.replace(" ", "").isalpha() == False or apellido_persona.strip() == "":
                    print("El apellido solo debe contener letras (puede ingresar los dos apellidos separados por un espacio).")
                    apellido_persona = input("Ingrese los apellidos de la persona (puede ingresar los dos separados por un espacio): ")
                apellido.append(apellido_persona)
                print(" ")

                codigo = input("Ingrese el código (numero de identificación maximo 10 dígitos) de la persona: ")
                while codigo.isdigit() == False or len(codigo) > validacioon_caracteres:
                    print("El código debe tener máximo 10 dígitos y solo números.")
                    codigo = input("Ingrese el código (numero de identificación maximo 10 dígitos) de la persona: ")
                codigo_persona.append(codigo)
                print(" ")

                while True:
                    try:
                        edade = int(input("Ingrese la edad de la persona: "))
                        if edade < 14 or edade > 100:
                            print("Edad inválida. La edad mínima para inscribirse es 14 años.")
                        else:
                            break
                    except:
                        print("La edad debe ser un número.")
                edad.append(edade)
                print(" ")

                programa_formacion.append("Análisis y Desarrollo de Sistemas de Información")
                cupos_adso -= 1
                print(f"Inscripción exitosa. Cupos restantes en Análisis y Desarrollo de Sistemas de Información: {cupos_adso}")
            else:
                print("No hay cupos disponibles en Análisis y Desarrollo de Sistemas de Información.")
                desea_aumentar = input("¿Desea aumentar los cupos para este programa? (1-si/2-no): ")
                while desea_aumentar != "1" and desea_aumentar != "2":
                    print("Opción inválida. Por favor, ingrese 1 para sí o 2 para no.")
                    desea_aumentar = input("¿Desea aumentar los cupos para este programa? (1-si/2-no): ")
                if desea_aumentar == "1":
                    while True:
                        try:
                            aumento = int(input("Ingrese la cantidad de cupos a aumentar: "))
                            break
                        except:
                            print("Debe ingresar solo números.")
                    cupos_adso += aumento
                    print(f"Se han aumentado {aumento} cupos. Total de cupos disponibles en Análisis y Desarrollo de Sistemas de Información: {cupos_adso}")
                else:
                    print("No se han aumentado los cupos.")

        elif programa == 2:
            if cupos_tecnico > 0:
                nombre_persona = input("Ingrese el nombre de la persona: ")
                while nombre_persona.isalpha() == False:
                    print("El nombre solo debe contener letras.")
                    nombre_persona = input("Ingrese el nombre de la persona: ")
                nombre.append(nombre_persona)
                print(" ")

                apellido_persona = input("Ingrese los apellidos de la persona (puede ingresar los dos separados por un espacio): ")
                while apellido_persona.replace(" ", "").isalpha() == False or apellido_persona.strip() == "":
                    print("El apellido solo debe contener letras (puede ingresar los dos apellidos separados por un espacio).")
                    apellido_persona = input("Ingrese los apellidos de la persona (puede ingresar los dos separados por un espacio): ")
                apellido.append(apellido_persona)
                print(" ")

                codigo = input("Ingrese el código (numero de identificación maximo 10 dígitos) de la persona: ")
                while codigo.isdigit() == False or len(codigo) > validacioon_caracteres:
                    print("El código debe tener máximo 10 dígitos y solo números.")
                    codigo = input("Ingrese el código (numero de identificación maximo 10 dígitos) de la persona: ")
                codigo_persona.append(codigo)
                print(" ")

                while True:
                    try:
                        edade = int(input("Ingrese la edad de la persona: "))
                        if edade < 14 or edade > 100:
                            print("Edad inválida. La edad mínima para inscribirse es 14 años.")
                        else:
                            break
                    except:
                        print("La edad debe ser un número.")
                edad.append(edade)
                print(" ")

                programa_formacion.append("Técnico en programación")
                cupos_tecnico -= 1
                print(f"Inscripción exitosa. Cupos restantes en Técnico en programación: {cupos_tecnico}")
            else:
                print("No hay cupos disponibles en Técnico en programación.")
                desea_aumentar = input("¿Desea aumentar los cupos para este programa? (1-si/2-no): ")
                while desea_aumentar != "1" and desea_aumentar != "2":
                    print("Opción inválida. Por favor, ingrese 1 para sí o 2 para no.")
                    desea_aumentar = input("¿Desea aumentar los cupos para este programa? (1-si/2-no): ")
                if desea_aumentar == "1":
                    while True:
                        try:
                            aumento = int(input("Ingrese la cantidad de cupos a aumentar: "))
                            break
                        except:
                            print("Debe ingresar solo números.")
                    cupos_tecnico += aumento
                    print(f"Se han aumentado {aumento} cupos. Total de cupos disponibles en Técnico en programación: {cupos_tecnico}")
                else:
                    print("No se han aumentado los cupos.")

        else:
            if cupos_multimedia > 0:
                nombre_persona = input("Ingrese el nombre de la persona: ")
                while nombre_persona.isalpha() == False:
                    print("El nombre solo debe contener letras.")
                    nombre_persona = input("Ingrese el nombre de la persona: ")
                nombre.append(nombre_persona)
                print(" ")

                apellido_persona = input("Ingrese los apellidos de la persona (puede ingresar los dos separados por un espacio): ")
                while apellido_persona.replace(" ", "").isalpha() == False or apellido_persona.strip() == "":
                    print("El apellido solo debe contener letras (puede ingresar los dos apellidos separados por un espacio).")
                    apellido_persona = input("Ingrese los apellidos de la persona (puede ingresar los dos separados por un espacio): ")
                apellido.append(apellido_persona)
                print(" ")

                codigo = input("Ingrese el código (numero de identificación maximo 10 dígitos) de la persona: ")
                while codigo.isdigit() == False or len(codigo) > validacioon_caracteres:
                    print("El código debe tener máximo 10 dígitos y solo números.")
                    codigo = input("Ingrese el código (numero de identificación maximo 10 dígitos) de la persona: ")
                codigo_persona.append(codigo)
                print(" ")

                while True:
                    try:
                        edade = int(input("Ingrese la edad de la persona: "))
                        if edade < 14 or edade > 100:
                            print("Edad inválida. La edad mínima para inscribirse es 14 años.")
                        else:
                            break
                    except:
                        print("La edad debe ser un número.")
                edad.append(edade)
                print(" ")

                programa_formacion.append("Multimedia")
                cupos_multimedia -= 1
                print(f"Inscripción exitosa. Cupos restantes en Multimedia: {cupos_multimedia}")
            else:
                print("No hay cupos disponibles en Multimedia.")
                desea_aumentar = input("¿Desea aumentar los cupos para este programa? (1-si/2-no): ")
                while desea_aumentar != "1" and desea_aumentar != "2":
                    print("Opción inválida. Por favor, ingrese 1 para sí o 2 para no.")
                    desea_aumentar = input("¿Desea aumentar los cupos para este programa? (1-si/2-no): ")
                if desea_aumentar == "1":
                    while True:
                        try:
                            aumento = int(input("Ingrese la cantidad de cupos a aumentar: "))
                            break
                        except:
                            print("Debe ingresar solo números.")
                    cupos_multimedia += aumento
                    print(f"Se han aumentado {aumento} cupos. Total de cupos disponibles en Multimedia: {cupos_multimedia}")
                else:
                    print("No se han aumentado los cupos.")

        desea_continuar = input("¿Desea inscribir a otra persona? (1-si/2-no): ")
        while desea_continuar != "1" and desea_continuar != "2":
            print("Opción inválida. Por favor, ingrese 1 para sí o 2 para no.")
            desea_continuar = input("¿Desea inscribir a otra persona? (1-si/2-no): ")

        if desea_continuar == "2":
            print(" ")
            print("cantidad de personas inscritas en cada programa:")
            print(f"Análisis y Desarrollo de Sistemas de Información: {40 - cupos_adso}")
            print(f"Técnico en programación: {34 - cupos_tecnico}")
            print(f"Multimedia: {40 - cupos_multimedia}")
            print(" ")
            modo_inscripcion = False

    else:
        # ---------- MENU: BUSCAR / ACTUALIZAR / ELIMINAR / REGISTRAR OTRA / SALIR ----------
        if len(codigo_persona) == 0:
            print("No hay personas inscritas. Fin del programa.")
            seguir_programa = False
        else:
            print(" ")
            print("MENU DE OPCIONES: ")
            print(""" 1- BUSCAR LA INFORMACION DE UNA PERSONA POR SU CODIGO
 2- ACTUALIZAR INFORMACION DE UNA PERSONA POR SU CODIGO
 3- ELIMINAR INFORMACION DE UNA PERSONA POR SU CODIGO
 4- SALIR
 5- REGISTRAR OTRA PERSONA""")
            OPCION = input("Seleccione una opción: ")
            while OPCION != "1" and OPCION != "2" and OPCION != "3" and OPCION != "4" and OPCION != "5":
                print("Opcion no valida ingrese 1, 2, 3, 4 o 5 segun corresponda en el menu de opciones")
                OPCION = input("Seleccione una opción: ")

            if OPCION == "4":
                print("Gracias por utilizar el sistema de control de cupos del SENA.")
                seguir_programa = False

            elif OPCION == "5":
                modo_inscripcion = True

            elif OPCION == "1":
                DESEA_BUSCAR = input("Ingrese el código de la persona que desea buscar: ")
                if DESEA_BUSCAR in codigo_persona:
                    index = codigo_persona.index(DESEA_BUSCAR)
                    print("Información de la persona:")
                    print(f"Código: {codigo_persona[index]}")
                    print(f"Nombre: {nombre[index]}")
                    print(f"Apellidos: {apellido[index]}")
                    print(f"Edad: {edad[index]}")
                    print(f"Programa de formación: {programa_formacion[index]}")
                else:
                    print("No se encontró información para el código ingresado.")

            elif OPCION == "2":
                DESEA_BUSCAR = input("Ingrese el código de la persona que desea actualizar la información: ")
                if DESEA_BUSCAR in codigo_persona:
                    index = codigo_persona.index(DESEA_BUSCAR)
                    print("Información de la persona:")
                    print(f"Código: {codigo_persona[index]}")
                    print(f"Nombre: {nombre[index]}")
                    print(f"Apellidos: {apellido[index]}")
                    print(f"Edad: {edad[index]}")
                    print(f"Programa de formación: {programa_formacion[index]}")
                    print(" ")

                    while True:
                        print("""QUE DATO DESEA ACTUALIZAR?
1- CODIGO
2- NOMBRE
3- APELLIDO
4- EDAD""")
                        men = input("Seleccione una opción: ")
                        while men != "1" and men != "2" and men != "3" and men != "4":
                            print("ERROR: seleccione una opción válida 1, 2, 3 o 4")
                            men = input("Seleccione una opción: ")

                        if men == "1":
                            nuevo_codigo = input("Ingrese el nuevo código (máximo 10 dígitos): ")
                            while nuevo_codigo.isdigit() == False or len(nuevo_codigo) > validacioon_caracteres:
                                print("El código debe tener máximo 10 dígitos y solo números.")
                                nuevo_codigo = input("Ingrese el nuevo código (máximo 10 dígitos): ")
                            while nuevo_codigo in codigo_persona and nuevo_codigo != codigo_persona[index]:
                                print("Ese código ya está en uso por otra persona.")
                                nuevo_codigo = input("Ingrese el nuevo código (máximo 10 dígitos): ")
                                while nuevo_codigo.isdigit() == False or len(nuevo_codigo) > validacioon_caracteres:
                                    print("El código debe tener máximo 10 dígitos y solo números.")
                                    nuevo_codigo = input("Ingrese el nuevo código (máximo 10 dígitos): ")
                            codigo_persona[index] = nuevo_codigo

                        elif men == "2":
                            nuevo_nombre = input("Ingrese el nuevo nombre: ")
                            while nuevo_nombre.isalpha() == False:
                                print("El nombre solo debe contener letras.")
                                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                            nombre[index] = nuevo_nombre

                        elif men == "3":
                            nuevo_apellido = input("Ingrese el nuevo apellido (puede ingresar los dos separados por un espacio): ")
                            while nuevo_apellido.replace(" ", "").isalpha() == False or nuevo_apellido.strip() == "":
                                print("El apellido solo debe contener letras (puede ingresar los dos apellidos separados por un espacio).")
                                nuevo_apellido = input("Ingrese el nuevo apellido (puede ingresar los dos separados por un espacio): ")
                            apellido[index] = nuevo_apellido

                        elif men == "4":
                            while True:
                                try:
                                    nueva_edad = int(input("Ingrese la nueva edad: "))
                                    if nueva_edad < 14 or nueva_edad > 100:
                                        print("Edad inválida. La edad mínima para inscribirse es 14 años.")
                                    else:
                                        break
                                except:
                                    print("La edad debe ser un número.")
                            edad[index] = nueva_edad

                        print("Datos actualizados correctamente.")
                        print(" ")
                        print("Información de la persona:")
                        print(f"Código: {codigo_persona[index]}")
                        print(f"Nombre: {nombre[index]}")
                        print(f"Apellidos: {apellido[index]}")
                        print(f"Edad: {edad[index]}")
                        print(f"Programa de formación: {programa_formacion[index]}")
                        print(" ")

                        desea_otro_dato = input("¿Desea actualizar otro dato de esta persona? (1-si/2-no): ")
                        while desea_otro_dato != "1" and desea_otro_dato != "2":
                            print("Opción inválida. Por favor, ingrese 1 para sí o 2 para no.")
                            desea_otro_dato = input("¿Desea actualizar otro dato de esta persona? (1-si/2-no): ")
                        if desea_otro_dato == "2":
                            break
                else:
                    print("No se encontró información para el código ingresado.")

            elif OPCION == "3":
                DESEA_ELIMINAR = input("Ingrese el código de la persona que desea eliminar: ")
                if DESEA_ELIMINAR in codigo_persona:
                    index = codigo_persona.index(DESEA_ELIMINAR)
                    print("Información de la persona:")
                    print(f"Código: {codigo_persona[index]}")
                    print(f"Nombre: {nombre[index]}")
                    print(f"Apellidos: {apellido[index]}")
                    print(f"Edad: {edad[index]}")
                    print(f"Programa de formación: {programa_formacion[index]}")
                    print(" ")

                    confirmar = input("¿Está seguro de que desea eliminar a esta persona? (1-si/2-no): ")
                    while confirmar != "1" and confirmar != "2":
                        print("Opción inválida. Por favor, ingrese 1 para sí o 2 para no.")
                        confirmar = input("¿Está seguro de que desea eliminar a esta persona? (1-si/2-no): ")

                    if confirmar == "1":
                        programa_eliminado = programa_formacion[index]

                        codigo_persona.pop(index)
                        nombre.pop(index)
                        apellido.pop(index)
                        edad.pop(index)
                        programa_formacion.pop(index)

                        if programa_eliminado == "Análisis y Desarrollo de Sistemas de Información":
                            cupos_adso += 1
                        elif programa_eliminado == "Técnico en programación":
                            cupos_tecnico += 1
                        else:
                            cupos_multimedia += 1

                        print("Persona eliminada correctamente.")
                    else:
                        print("Eliminación cancelada.")
                else:
                    print("No se encontró información para el código ingresado.")
