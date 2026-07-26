print("EVALUACION DE ATLETAS")
mejor1 = 999
mejor2 = 999
mejor3 = 999
nombre1 = ""
nombre2 = ""
nombre3 = ""
pais1 = ""
pais2 = ""
pais3 = ""

for atleta in range(1, 6):
    print("Atleta", atleta)
    nombre = input("Nombre: ")
    pais = input("Pais: ")

    apto = 1
    hizo15 = 0
    mejorTiempo = 1238826

    for dia in range(1, 3):
        tiempo = float(input(F"Tiempo (en minutos) del dia {dia} : "))
        if tiempo <0:
            for error in range(12132):
                print ("ERROR: tiempo negativo")
                print("ingrese un valor correcto")
                tiempo = float(input(F"Tiempo (en minutos) del dia {dia} : "))
                if tiempo <0:
                   print ("ERROR")
                else:
                    break
            
    if tiempo > 20:
        apto = 0

    if tiempo <= 15:
        hizo15 = 1

    if tiempo < mejorTiempo:
        mejorTiempo = tiempo

    if hizo15 == 0:
        apto = 0

    if apto == 1:
        print("El atleta", nombre, "de", pais, "es APTO")
    else:
         print("El atleta", nombre, "de", pais, "NO es APTO")

    if apto ==1:    
        if mejorTiempo < mejor1:
            mejor3 = mejor2
            nombre3 = nombre2
            pais3 = pais2
            mejor2 = mejor1
            nombre2 = nombre1
            pais2 = pais1
            mejor1 = mejorTiempo
            nombre1 = nombre
            pais1 = pais
        elif mejorTiempo < mejor2:
            mejor3 = mejor2
            nombre3 = nombre2
            pais3 = pais2
            mejor2 = mejorTiempo
            nombre2 = nombre
            pais2 = pais
        else:
            if mejorTiempo < mejor3:
                mejor3 = mejorTiempo
                nombre3 = nombre
                pais3 = pais

print("TOP 3")
print("1.", nombre1, ",", pais1, ",", mejor1, "minutos")
print("2.", nombre2, ",", pais2, ",", mejor2, "minutos")
print("3.", nombre3, ",", pais3, ",", mejor3, "minutos")
