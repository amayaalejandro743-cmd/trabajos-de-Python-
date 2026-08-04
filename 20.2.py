print(" BIENVENIDO ")

print("¿Qué grupo desea registrar primero? (A / B): ")
grupo_inicial = input()

while grupo_inicial != "A" and grupo_inicial != "B":
    print("ERROR: Ingrese una opción válida (A o B):")
    grupo_inicial = input()

mejor1_a = " "
mejor2_a = " "
mejor3_a = " "
mejor4_a = " "
mejor5_a = " "
mejor6_a = " "
puntos1_a = 0
puntos2_a = 0
puntos3_a = 0
puntos4_a = 0
puntos5_a = 0
puntos6_a = 0

mejor1_b = " "
mejor2_b = " "
mejor3_b = " "
mejor4_b = " "
mejor5_b = " "
mejor6_b = " "
puntos1_b = 0
puntos2_b = 0
puntos3_b = 0
puntos4_b = 0
puntos5_b = 0
puntos6_b = 0


for iteracion in range(1, 3):
    if (iteracion == 1 and grupo_inicial == "A") or (iteracion == 2 and grupo_inicial == "B"):
        grupo_actual = "A"
    else:
        grupo_actual = "B"

    print(f"REGISTRANDO DATOS-GRUPO {grupo_actual}")
   
    equipos = 0
    entra = False

    while equipos <= 5:
        equipos += 1
        puntos = 0
        print(f"Ingrese el nombre del equipo #{equipos} del Grupo {grupo_actual}: ")
        nom = str(input())

        for juegos in range(1, 6):
            print("ingrese reultado del juego: ", juegos, "°")
            print("1-victoria, 2-empate, 3-derrota")
            resultado = int(input())
            if resultado != 1 and resultado != 2 and resultado != 3:
                entra = True
                while entra:
                    print("ERROR:ingrese un dato valido")
                    print("ingrese reultado del juego: ", juegos, "°")
                    print("1-victoria, 2-empate, 3-derrota")
                    resultado = int(input())
                    if resultado == 1 or resultado == 2 or resultado == 3:
                        break
                    else:
                        print(" ")
            if resultado == 1:
                print(f"partido #{juegos} ganado")
                print("suma 3 puntos")
                puntos = puntos + 3
            elif resultado == 2:
                print(f"partido #{juegos} empatado")
                print("suma 1 puntos")
                puntos = puntos + 1
            else:
                print(f"partido #{juegos} perdido")
                print("suma 0 puntos")
                puntos = puntos + 0
            print(f"puntos del equipo {nom} son {puntos} ")

  
        if grupo_actual == "A":
            if puntos > puntos1_a:
                mejor6_a = mejor5_a; puntos6_a = puntos5_a
                mejor5_a = mejor4_a; puntos5_a = puntos4_a
                mejor4_a = mejor3_a; puntos4_a = puntos3_a
                mejor3_a = mejor2_a; puntos3_a = puntos2_a
                mejor2_a = mejor1_a; puntos2_a = puntos1_a
                mejor1_a = nom;       puntos1_a = puntos
            elif puntos > puntos2_a:
                mejor6_a = mejor5_a; puntos6_a = puntos5_a
                mejor5_a = mejor4_a; puntos5_a = puntos4_a
                mejor4_a = mejor3_a; puntos4_a = puntos3_a
                mejor3_a = mejor2_a; puntos3_a = puntos2_a
                mejor2_a = nom;       puntos2_a = puntos
            elif puntos > puntos3_a:
                mejor6_a = mejor5_a; puntos6_a = puntos5_a
                mejor5_a = mejor4_a; puntos5_a = puntos4_a
                mejor4_a = mejor3_a; puntos3_a = puntos3_a
                mejor3_a = nom;       puntos3_a = puntos
            elif puntos > puntos4_a:
                mejor6_a = mejor5_a; puntos6_a = puntos5_a
                mejor5_a = mejor4_a; puntos5_a = puntos4_a
                mejor4_a = nom;       puntos4_a = puntos
            elif puntos > puntos5_a:
                mejor6_a = mejor5_a; puntos6_a = puntos5_a
                mejor5_a = nom;       puntos5_a = puntos
            else:
                mejor6_a = nom
                puntos6_a = puntos
        else:
            if puntos > puntos1_b:
                mejor6_b = mejor5_b; puntos6_b = puntos5_b
                mejor5_b = mejor4_b; puntos5_b = puntos4_b
                mejor4_b = mejor3_b; puntos4_b = puntos3_b
                mejor3_b = mejor2_b; puntos3_b = puntos2_b
                mejor2_b = mejor1_b; puntos2_b = puntos1_b
                mejor1_b = nom;       puntos1_b = puntos
            elif puntos > puntos2_b:
                mejor6_b = mejor5_b; puntos6_b = puntos5_b
                mejor5_b = mejor4_b; puntos5_b = puntos4_b
                mejor4_b = mejor3_b; puntos4_b = puntos3_b
                mejor3_b = mejor2_b; puntos3_b = puntos2_b
                mejor2_b = nom;       puntos2_b = puntos
            elif puntos > puntos3_b:
                mejor6_b = mejor5_b; puntos6_b = puntos5_b
                mejor5_b = mejor4_b; puntos5_b = puntos4_b
                mejor4_b = mejor3_b; puntos3_b = puntos3_b
                mejor3_b = nom;       puntos3_b = puntos
            elif puntos > puntos4_b:
                mejor6_b = mejor5_b; puntos6_b = puntos5_b
                mejor5_b = mejor4_b; puntos5_b = puntos4_b
                mejor4_b = nom;       puntos4_b = puntos
            elif puntos > puntos5_b:
                mejor6_b = mejor5_b; puntos6_b = puntos5_b
                mejor5_b = nom;       puntos5_b = puntos
            else:
                mejor6_b = nom
                puntos6_b = puntos


print(" TABLA DE POSICIONES GRUPO A")
print(f"1° LUGAR  {mejor1_a}  {puntos1_a} pts")
print(f"2° LUGAR  {mejor2_a}  {puntos2_a} pts")
print(f"3° LUGAR  {mejor3_a}  {puntos3_a} pts")
print(f"4° LUGAR  {mejor4_a}  {puntos4_a} pts")
print(f"5° LUGAR  {mejor5_a}  {puntos5_a} pts")
print(f"6° LUGAR  {mejor6_a}  {puntos6_a} pts")

print("TABLA DE POSICIONES GRUPO B ")
print(f"1° LUGAR  {mejor1_b}  {puntos1_b} pts")
print(f"2° LUGAR  {mejor2_b}  {puntos2_b} pts")
print(f"3° LUGAR  {mejor3_b}  {puntos3_b} pts")
print(f"4° LUGAR  {mejor4_b}  {puntos4_b} pts")
print(f"5° LUGAR  {mejor5_b}  {puntos5_b} pts")
print(f"6° LUGAR  {mejor6_b}  {puntos6_b} pts")



print(" GRAN FINAL DE TORNEO")
print(f"   {mejor1_a} (1° Grupo A) VS {mejor1_b} (1° Grupo B)   ")


print(f"Ingrese los goles anotados por {mejor1_a}: ")
goles_a = int(input())
if goles_a <0:
    while True:
        print("ERROR: ingrese cantidades positivas y validas ")
        goles_a = int(input())
        if goles_a >=0:
            break
        else:
            print("")
            
print(f"Ingrese los goles anotados por {mejor1_b}: ")
goles_b = int(input())
if goles_b <0:
    while True:
        print("ERROR: ingrese cantidades positivas y validas ")
        goles_b = int(input())
        if goles_b >=0:
            break
        else:
            print("")

if goles_a > goles_b:
    print(f"EL CAMPEÓN ES {mejor1_a} CON {goles_a} GOLES A FAVOR!")
elif goles_b > goles_a:
    print(f"EL CAMPEÓN ES {mejor1_b} CON {goles_b} GOLES A FAVOR!")
else:
    print("EMPATE EN GOLES! El partido se define por PENALES.")
    print(f"Ingrese los penales anotados por {mejor1_a}: ")
    penales_a = int(input())
    if goles_a <0:
        while True:
            print("ERROR: ingrese cantidades positivas y validas ")
            goles_a = int(input())
            if goles_a >=0:
                break
            else:
                print("")
            
    print(f"Ingrese los penales anotados por {mejor1_b}: ")
    penales_b = int(input())
    if goles_b <0:
        while True:
            print("ERROR: ingrese cantidades positivas y validas ")
            goles_b = int(input())
            if goles_b >=0:
                break
            else:
                print("")
    

    while penales_a == penales_b:
        print("Empate en penales! Se ejecuta una nueva ronda:")
        print(f"Ingrese los penales anotados por {mejor1_a}: ")
        penales_a = int(input())
        if goles_a <0:
            while True:
                print("ERROR: ingrese cantidades positivas y validas ")
                goles_a = int(input())
                if goles_a >=0:
                    break
                else:
                    print("")
        
        print(f"Ingrese los penales anotados por {mejor1_b}: ")
        penales_b = int(input())
        if goles_b <0:
            while True:
                print("ERROR: ingrese cantidades positivas y validas ")
                goles_b = int(input())
                if goles_b >=0:
                    break
                else:
                    print("")

    if penales_a > penales_b:
        print(f"EL CAMPEÓN ES {mejor1_a} GANANDO EN PENALES ({penales_a} a {penales_b})")
    else:
        print(f"\n¡EL CAMPEÓN ES {mejor1_b} GANANDO EN PENALES ({penales_b} a {penales_a})")
        
