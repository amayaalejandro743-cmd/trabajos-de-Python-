
print("¿Qué grupo desea registrar primero? (A / B): ")
grupo_inicial = str(input())

while grupo_inicial != "A" and grupo_inicial != "B":
    print("ERROR: Ingrese una opción válida (A o B):")
    grupo_inicial = str(input())

mejor1_a = " "
mejor2_a = " "
mejor3_a = " "
mejor4_a = " "
puntos1_a = 0
puntos2_a = 0
puntos3_a = 0
puntos4_a = 0
goles1_a = 0
goles2_a = 0
goles3_a = 0
goles4_a = 0

mejor1_b = " "
mejor2_b = " "
mejor3_b = " "
mejor4_b = " "
puntos1_b = 0
puntos2_b = 0
puntos3_b = 0
puntos4_b = 0
goles1_b = 0
goles2_b = 0
goles3_b = 0
goles4_b = 0


for iteracion in range(1, 3):
    if (iteracion == 1 and grupo_inicial == "A") or (iteracion == 2 and grupo_inicial == "B"):
        grupo_actual = "A"
    else:
        grupo_actual = "B"

    print(f" REGISTRANDO EQUIPOS - GRUPO {grupo_actual}")
 
    print("Ingrese nombre del Equipo 1: "); e1 = input()
    print("Ingrese nombre del Equipo 2: "); e2 = input()
    print("Ingrese nombre del Equipo 3: "); e3 = input()
    print("Ingrese nombre del Equipo 4: "); e4 = input()
 
    pts_e1 = 0
    pts_e2 = 0
    pts_e3 = 0
    pts_e4 = 0
    gol_e1 = 0
    gol_e2 = 0
    gol_e3 = 0
    gol_e4 = 0

    print(f"PARTIDOS TODOS CONTRA TODOS - GRUPO {grupo_actual}")
  
    for partido in range(1, 7):
        if partido == 1:
            local = e1; visitante = e2
        elif partido == 2:
            local = e1; visitante = e3
        elif partido == 3:
            local = e1; visitante = e4
        elif partido == 4:
            local = e2; visitante = e3
        elif partido == 5:
            local = e2; visitante = e4
        elif partido == 6:
            local = e3; visitante = e4

        print(f" PARTIDO #{partido}: {local} VS {visitante} ")

        print(f"Ingrese goles anotados por {local}: ")
        g_local = int(input())
        while g_local < 0:
            print("ERROR: Los goles no pueden ser negativos. Ingrese de nuevo:")
            g_local = int(input())

        print(f"Ingrese goles anotados por {visitante}: ")
        g_visita = int(input())
        while g_visita < 0:
            print("ERROR: Los goles no pueden ser negativos. Ingrese de nuevo:")
            g_visita = int(input())

        if partido == 1:
            gol_e1 += g_local; gol_e2 += g_visita
        elif partido == 2:
            gol_e1 += g_local; gol_e3 += g_visita
        elif partido == 3:
            gol_e1 += g_local; gol_e4 += g_visita
        elif partido == 4:
            gol_e2 += g_local; gol_e3 += g_visita
        elif partido == 5:
            gol_e2 += g_local; gol_e4 += g_visita
        elif partido == 6:
            gol_e3 += g_local; gol_e4 += g_visita

        if g_local > g_visita:
            print(f" Ganador: {local} (Suma 3 pts)")
            p_local = 3
            p_visita = 0
        elif g_visita > g_local:
            print(f" Ganador: {visitante} (Suma 3 pts)")
            p_local = 0
            p_visita = 3
        else:
            print(" Empate (1 pt para cada uno)")
            p_local = 1; p_visita = 1

        if partido == 1:
            pts_e1 += p_local; pts_e2 += p_visita
        elif partido == 2:
            pts_e1 += p_local; pts_e3 += p_visita
        elif partido == 3:
            pts_e1 += p_local; pts_e4 += p_visita
        elif partido == 4:
            pts_e2 += p_local; pts_e3 += p_visita
        elif partido == 5:
            pts_e2 += p_local; pts_e4 += p_visita
        elif partido == 6:
            pts_e3 += p_local; pts_e4 += p_visita

    for pos in range(1, 5):
        if pos == 1:
            nom_temp = e1;
            pts_temp = pts_e1
            gol_temp = gol_e1
        elif pos == 2:
            nom_temp = e2
            pts_temp = pts_e2
            gol_temp = gol_e2
        elif pos == 3:
            nom_temp = e3
            pts_temp = pts_e3
            gol_temp = gol_e3
        elif pos == 4:
            nom_temp = e4
            pts_temp = pts_e4
            gol_temp = gol_e4

        if grupo_actual == "A":
            if pts_temp > puntos1_a or (pts_temp == puntos1_a and gol_temp > goles1_a):
                mejor4_a = mejor3_a
                puntos4_a = puntos3_a
                goles4_a = goles3_a
                mejor3_a = mejor2_a
                puntos3_a = puntos2_a
                goles3_a = goles2_a
                mejor2_a = mejor1_a
                puntos2_a = puntos1_a
                goles2_a = goles1_a
                mejor1_a = nom_temp
                puntos1_a = pts_temp
                goles1_a = gol_temp
            elif pts_temp > puntos2_a or (pts_temp == puntos2_a and gol_temp > goles2_a):
                mejor4_a = mejor3_a
                puntos4_a = puntos3_a
                goles4_a = goles3_a
                mejor3_a = mejor2_a
                puntos3_a = puntos2_a
                goles3_a = goles2_a
                mejor2_a = nom_temp
                puntos2_a = pts_temp
                goles2_a = gol_temp
            elif pts_temp > puntos3_a or (pts_temp == puntos3_a and gol_temp > goles3_a):
                mejor4_a = mejor3_a
                puntos4_a = puntos3_a
                goles4_a = goles3_a
                mejor3_a = nom_temp
                puntos3_a = pts_temp
                goles3_a = gol_temp
            else:
                mejor4_a = nom_temp;
                puntos4_a = pts_temp;
                goles4_a = gol_temp
        else:
            if pts_temp > puntos1_b or (pts_temp == puntos1_b and gol_temp > goles1_b):
                mejor4_b = mejor3_b
                puntos4_b = puntos3_b
                goles4_b = goles3_b
                mejor3_b = mejor2_b
                puntos3_b = puntos2_b
                goles3_b = goles2_b
                mejor2_b = mejor1_b
                puntos2_b = puntos1_b
                goles2_b = goles1_b
                mejor1_b = nom_temp
                puntos1_b = pts_temp
                goles1_b = gol_temp
            elif pts_temp > puntos2_b or (pts_temp == puntos2_b and gol_temp > goles2_b):
                mejor4_b = mejor3_b
                puntos4_b = puntos3_b
                goles4_b = goles3_b
                mejor3_b = mejor2_b
                puntos3_b = puntos2_b
                goles3_b = goles2_b
                mejor2_b = nom_temp
                puntos2_b = pts_temp
                goles2_b = gol_temp
            elif pts_temp > puntos3_b or (pts_temp == puntos3_b and gol_temp > goles3_b):
                mejor4_b = mejor3_b
                puntos4_b = puntos3_b
                goles4_b = goles3_b
                mejor3_b = nom_temp
                puntos3_b = pts_temp
                goles3_b = gol_temp
            else:
                mejor4_b = nom_temp
                puntos4_b = pts_temp
                goles4_b = gol_temp

print(" TABLA DE POSICIONES GRUPO A ")
print(f"1° LUGAR  {mejor1_a}  {puntos1_a} pts  {goles1_a} goles")
print(f"2° LUGAR  {mejor2_a}  {puntos2_a} pts  {goles2_a} goles")
print(f"3° LUGAR  {mejor3_a}  {puntos3_a} pts  {goles3_a} goles")
print(f"4° LUGAR  {mejor4_a}  {puntos4_a} pts  {goles4_a} goles")

print(" TABLA DE POSICIONES GRUPO B ")
print(f"1° LUGAR  {mejor1_b}  {puntos1_b} pts  {goles1_b} goles")
print(f"2° LUGAR  {mejor2_b}  {puntos2_b} pts  {goles2_b} goles")
print(f"3° LUGAR  {mejor3_b}  {puntos3_b} pts  {goles3_b} goles")
print(f"4° LUGAR  {mejor4_b}  {puntos4_b} pts  {goles4_b} goles")


print(" GRAN FINAL DE TORNEO ")
print(f" {mejor1_a} (1° Grupo A) VS {mejor1_b} (1° Grupo B) ")


print(f"Ingrese los goles anotados por {mejor1_a}: ")
goles_final_a = int(input())
while goles_final_a < 0:
    print("ERROR: Los goles no pueden ser negativos. Ingrese de nuevo:")
    goles_final_a = int(input())

print(f"Ingrese los goles anotados por {mejor1_b}: ")
goles_final_b = int(input())
while goles_final_b < 0:
    print("ERROR: Los goles no pueden ser negativos. Ingrese de nuevo:")
    goles_final_b = int(input())

if goles_final_a > goles_final_b:
    print(f"EL CAMPEÓN ES {mejor1_a} CON {goles_final_a} GOLES A FAVOR")
elif goles_final_b > goles_final_a:
    print(f"EL CAMPEÓN ES {mejor1_b} CON {goles_final_b} GOLES A FAVOR")
else:
    print("EMPATE EN GOLES, El partido se define por PENALES.")
    
    print(f"Ingrese los penales anotados por {mejor1_a}: ")
    penales_a = int(input())
    while penales_a < 0:
        print("ERROR: Los penales no pueden ser negativos. Ingrese de nuevo:")
        penales_a = int(input())

    print(f"Ingrese los penales anotados por {mejor1_b}: ")
    penales_b = int(input())
    while penales_b < 0:
        print("ERROR: Los penales no pueden ser negativos. Ingrese de nuevo:")
        penales_b = int(input())

    while penales_a == penales_b:
        print("Empate en penales! Se ejecuta una nueva ronda:")
        print(f"Ingrese los penales anotados por {mejor1_a}: ")
        penales_a = int(input())
        while penales_a < 0:
            print("ERROR: No se permiten números negativos:")
            penales_a = int(input())

        print(f"Ingrese los penales anotados por {mejor1_b}: ")
        penales_b = int(input())
        while penales_b < 0:
            print("ERROR: No se permiten números negativos:")
            penales_b = int(input())

    if penales_a > penales_b:
        print(f"EL CAMPEÓN ES {mejor1_a} GANANDO EN PENALES ({penales_a} a {penales_b})")
    else:
        print(f"EL CAMPEÓN ES {mejor1_b} GANANDO EN PENALES ({penales_b} a {penales_a})")
