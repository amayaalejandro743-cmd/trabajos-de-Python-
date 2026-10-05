cupos_adso = 40
cupos_tecnico = 34
cupos_multimedia = 40

codigo_persona = [] 
nombre=[]
apellido=[]
edad=[]
programa_formacion=[]
validacioon_caracteres = 10

print("Bienvenido al sistema de control de cupos del SENA")
print(" seleccione el programa de formación al que desea inscribirse:")
print("1. Análisis y Desarrollo de Sistemas de Información")
print("2. Técnico en programación")
print("3. Multimedia")  
while True:
    programa = int(input("Ingrese el número del programa a inscribirse: "))
    while programa < 1 or programa > 3: 
        print("Opción inválida. Por favor, seleccione un programa válido.")
        programa = int(input("Ingrese el número del programa a inscribirse: "))

    if programa == 1:
        if cupos_adso > 0:
            nombre.append(input("Ingrese el nombre de la persona: "))
            print(" ")
            apellido.append(input("Ingrese los apellidos de la persona: "))
            print(" ")
            codigo = input("Ingrese el código (numero de identificación maximo 10 dígitos) de la persona: ")
            while len(codigo) > validacioon_caracteres:
                print("El código debe tener maximo 10 dígitos.")
                codigo = input("Ingrese el código (numero de identificación maximo 10 dígitos) de la persona: ")
            codigo_persona.append(codigo)
            print(" ")
            print("Ingrese la edad de la persona: ")
            edade=int(input())
            while edade < 0 or edade > 100:
                print("Edad inválida. Por favor, ingrese una edad válida.")
                edade=int(input("Ingrese la edad de la persona: "))
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
                aumento = int(input("Ingrese la cantidad de cupos a aumentar: "))
                cupos_adso += aumento
                print(f"Se han aumentado {aumento} cupos. Total de cupos disponibles en Análisis y Desarrollo de Sistemas de Información: {cupos_adso}")
            else:
                print("No se han aumentado los cupos.")
    elif programa == 2: 
        if cupos_tecnico > 0:
            nombre.append(input("Ingrese el nombre de la persona: "))
            print(" ")
            apellido.append(input("Ingrese los apellidos de la persona: "))
            print(" ")
            codigo = input("Ingrese el código (numero de identificación maximo 10 dígitos) de la persona: ")
            while len(codigo) > validacioon_caracteres:
                print("El código debe tener maximo 10 dígitos.")
                codigo = input("Ingrese el código (numero de identificación maximo 10 dígitos) de la persona: ")
            codigo_persona.append(codigo)
            print(" ")
            print("Ingrese la edad de la persona: ")
            edade=int(input())
            while edade < 0 or edade > 100:
                print("Edad inválida. Por favor, ingrese una edad válida.")
                edade=int(input("Ingrese la edad de la persona: "))
            edad.append(edade)               
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
                aumento = int(input("Ingrese la cantidad de cupos a aumentar: "))
                cupos_tecnico += aumento
                print(f"Se han aumentado {aumento} cupos. Total de cupos disponibles en Técnico en programación: {cupos_tecnico}")
            else:
                print("No se han aumentado los cupos.")
    else:
        if cupos_multimedia > 0:
            nombre.append(input("Ingrese el nombre de la persona: "))
            print(" ")
            apellido.append(input("Ingrese los apellidos de la persona: "))
            print(" ")
            codigo = input("Ingrese el código (numero de identificación maximo 10 dígitos) de la persona: ")
            while len(codigo) > validacioon_caracteres:
                print("El código debe tener maximo 10 dígitos.")
                codigo = input("Ingrese el código (numero de identificación maximo 10 dígitos) de la persona: ")
            codigo_persona.append(codigo)
            print(" ")
            print("Ingrese la edad de la persona: ")
            edade=int(input())
            while edade < 0 or edade > 100:
                print("Edad inválida. Por favor, ingrese una edad válida.")
                edade=int(input("Ingrese la edad de la persona: "))
            edad.append(edade)               
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
                aumento = int(input("Ingrese la cantidad de cupos a aumentar: "))
                cupos_multimedia += aumento
                print(f"Se han aumentado {aumento} cupos. Total de cupos disponibles en Multimedia: {cupos_multimedia}")
            else:
                print("No se han aumentado los cupos.")
    desea_continuar = input("¿Desea inscribir a otra persona? (1-si/2-no): ")
    while desea_continuar != "1" and desea_continuar != "2":
        print("Opción inválida. Por favor, ingrese 1 para sí o 2 para no.")
        desea_continuar = input("¿Desea inscribir a otra persona? (1-si/2-no): ")   
    if desea_continuar == "2":
        break
    else:
        print(" ")
        print("Seleccione el programa de formación al que desea inscribirse:")
        print("1. Análisis y Desarrollo de Sistemas de Información")
        print("2. Técnico en programación")
        print("3. Multimedia")

print("cantidad de personas inscritas en cada programa:")
print(f"Análisis y Desarrollo de Sistemas de Información: {40 - cupos_adso}")
print(f"Técnico en programación: {34 - cupos_tecnico}")
print(f"Multimedia: {40 - cupos_multimedia}")
print(" ")

OPCION = input("¿Desea buscar la información de una persona por su código? (1-si/2-no): ")
while OPCION != "1" and OPCION != "2":
    print("Opción inválida. Por favor, ingrese 1 para sí o 2 para no.")
    OPCION = input("¿Desea buscar la información de una persona por su código? (1-si/2-no): ")
if OPCION == "1":
    while True:
        DESEA_BUSCAR = input("Ingrese el código de la persona que desea buscar: ")
        if DESEA_BUSCAR in codigo_persona:
            index = codigo_persona.index(DESEA_BUSCAR)
            print("Información de la persona:")
            print(f"Código: {codigo_persona[index]}")
            print(f"Nombre: {nombre[index]}")
            print(f"Apellidos: {apellido[index]}")
            print(f"Edad: {edad[index]}")
            print(f"Programa de formación: {programa_formacion[index]}")
            print(" ")
        else:
            print("No se encontró información para el código ingresado.")
            print(" ")
        DESEA_BUSCAR_OTRA = input("¿Desea buscar otra persona? (1-si/2-no): ")
        while DESEA_BUSCAR_OTRA != "1" and DESEA_BUSCAR_OTRA != "2":
            print("Opción inválida. Por favor, ingrese 1 para sí o 2 para no.")
            DESEA_BUSCAR_OTRA = input("¿Desea buscar otra persona? (1-si/2-no): ")
        if DESEA_BUSCAR_OTRA == "2":
            print("Gracias por utilizar el sistema de control de cupos del SENA.")
            break
else:
    print("Gracias por utilizar el sistema de control de cupos del SENA.")
    
    
