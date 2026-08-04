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
puntos1_a = 0
puntos2_a = 0
puntos3_a = 0
puntos4_a = 0
gf1_a = 0
gf2_a = 0
gf3_a = 0
gf4_a = 0
gc1_a = 0
gc2_a = 0
gc3_a = 0
gc4_a = 0
dg1_a = 0
dg2_a = 0
dg3_a = 0
dg4_a = 0
pg1_a = 0
pg2_a = 0
pg3_a = 0
pg4_a = 0
pe1_a = 0
pe2_a = 0
pe3_a = 0
pe4_a = 0
pp1_a = 0
pp2_a = 0
pp3_a = 0
pp4_a = 0

mejor1_b = " "
mejor2_b = " "
mejor3_b = " "
mejor4_b = " "
puntos1_b = 0
puntos2_b = 0
puntos3_b = 0
puntos4_b = 0
gf1_b = 0
gf2_b = 0
gf3_b = 0
gf4_b = 0
gc1_b = 0
gc2_b = 0
gc3_b = 0
gc4_b = 0
dg1_b = 0
dg2_b = 0
dg3_b = 0
dg4_b = 0
pg1_b = 0
pg2_b = 0
pg3_b = 0
pg4_b = 0
pe1_b = 0
pe2_b = 0
pe3_b = 0
pe4_b = 0
pp1_b = 0
pp2_b = 0
pp3_b = 0
pp4_b = 0

for iteracion in range(1, 3):
    if (iteracion == 1 and grupo_inicial == "A") or (iteracion == 2 and grupo_inicial == "B"):
        grupo_actual = "A"
    else:
        grupo_actual = "B"

    print(f"REGISTRANDO DATOS - GRUPO {grupo_actual}")


    print(f"Ingrese el nombre del equipo #1 del Grupo {grupo_actual}: ")
    eq1 = input()
    print(f"Ingrese el nombre del equipo #2 del Grupo {grupo_actual}: ")
    eq2 = input()
    print(f"Ingrese el nombre del equipo #3 del Grupo {grupo_actual}: ")
    eq3 = input()
    print(f"Ingrese el nombre del equipo #4 del Grupo {grupo_actual}: ")
    eq4 = input()

    pts_e1 = 0
    pts_e2 = 0
    pts_e3 = 0
    pts_e4 = 0
    gf_e1 = 0
    gf_e2 = 0
    gf_e3 = 0
    gf_e4 = 0
    gc_e1 = 0
    gc_e2 = 0
    gc_e3 = 0
    gc_e4 = 0
    pg_e1 = 0
    pg_e2 = 0
    pg_e3 = 0
    pg_e4 = 0
    pe_e1 = 0
    pe_e2 = 0
    pe_e3 = 0
    pe_e4 = 0
    pp_e1 = 0
    pp_e2 = 0
    pp_e3 = 0
    pp_e4 = 0

    print(f"PARTIDOS TODOS CONTRA TODOS (GRUPO {grupo_actual})")
 
    for juego in range(1, 7):
        if juego == 1:
            local = eq1
            visitante = eq2
        elif juego == 2:
            local = eq1
            visitante = eq3
        elif juego == 3:
            local = eq1
            visitante = eq4
        elif juego == 4:
            local = eq2
            visitante = eq3
        elif juego == 5:
            local = eq2
            visitante = eq4
        elif juego == 6:
            local = eq3
            visitante = eq4

        print(f"JUEGO #{juego}: {local} VS {visitante}")
        
        print(f"Ingrese goles anotados por {local}: ")
        goles_loc = int(input())
        if goles_loc < 0:
            while True:
                print("ERROR: ingrese cantidades positivas y validas ")
                goles_loc = int(input())
                if goles_loc >= 0:
                    break

        print(f"Ingrese goles anotados por {visitante}: ")
        goles_vis = int(input())
        if goles_vis < 0:
            while True:
                print("ERROR: ingrese cantidades positivas y validas ")
                goles_vis = int(input())
                if goles_vis >= 0:
                    break

        if juego == 1:
            gf_e1 += goles_loc
            gc_e1 += goles_vis
            gf_e2 += goles_vis
            gc_e2 += goles_loc
        elif juego == 2:
            gf_e1 += goles_loc
            gc_e1 += goles_vis
            gf_e3 += goles_vis
            gc_e3 += goles_loc
        elif juego == 3:
            gf_e1 += goles_loc
            gc_e1 += goles_vis
            gf_e4 += goles_vis
            gc_e4 += goles_loc
        elif juego == 4:
            gf_e2 += goles_loc
            gc_e2 += goles_vis
            gf_e3 += goles_vis
            gc_e3 += goles_loc
        elif juego == 5:
            gf_e2 += goles_loc
            gc_e2 += goles_vis
            gf_e4 += goles_vis
            gc_e4 += goles_loc
        elif juego == 6:
            gf_e3 += goles_loc
            gc_e3 += goles_vis
            gf_e4 += goles_vis
            gc_e4 += goles_loc


        if goles_loc > goles_vis:
            p_loc = 3
            p_vis = 0
            res_loc = "G"
            res_vis = "P"
        elif goles_vis > goles_loc:
            p_loc = 0
            p_vis = 3
            res_loc = "P"
            res_vis = "G"
        else:
            p_loc = 1
            p_vis = 1
            res_loc = "E"
            res_vis = "E"

        if juego == 1:
            pts_e1 += p_loc
            pts_e2 += p_vis
            if res_loc == "G":
                pg_e1 += 1
                pp_e2 += 1
            elif res_loc == "P":
                pp_e1 += 1
                pg_e2 += 1
            else:
                pe_e1 += 1
                pe_e2 += 1
        elif juego == 2:
            pts_e1 += p_loc
            pts_e3 += p_vis
            if res_loc == "G":
                pg_e1 += 1
                pp_e3 += 1
            elif res_loc == "P":
                pp_e1 += 1
                pg_e3 += 1
            else:
                pe_e1 += 1
                pe_e3 += 1
        elif juego == 3:
            pts_e1 += p_loc
            pts_e4 += p_vis
            if res_loc == "G":
                pg_e1 += 1
                pp_e4 += 1
            elif res_loc == "P":
                pp_e1 += 1
                pg_e4 += 1
            else:
                pe_e1 += 1
                pe_e4 += 1
        elif juego == 4:
            pts_e2 += p_loc
            pts_e3 += p_vis
            if res_loc == "G":
                pg_e2 += 1
                pp_e3 += 1
            elif res_loc == "P":
                pp_e2 += 1
                pg_e3 += 1
            else:
                pe_e2 += 1
                pe_e3 += 1
        elif juego == 5:
            pts_e2 += p_loc
            pts_e4 += p_vis
            if res_loc == "G":
                pg_e2 += 1
                pp_e4 += 1
            elif res_loc == "P":
                pp_e2 += 1
                pg_e4 += 1
            else:
                pe_e2 += 1
                pe_e4 += 1
        elif juego == 6:
            pts_e3 += p_loc
            pts_e4 += p_vis
            if res_loc == "G":
                pg_e3 += 1
                pp_e4 += 1
            elif res_loc == "P":
                pp_e3 += 1
                pg_e4 += 1
            else:
                pe_e3 += 1
                pe_e4 += 1
   
    for pos in range(1, 5):
        if pos == 1:
            nom_temp = eq1
            pts_temp = pts_e1
            gf_temp = gf_e1
            gc_temp = gc_e1
            pg_temp = pg_e1
            pe_temp = pe_e1
            pp_temp = pp_e1
        elif pos == 2:
            nom_temp = eq2;
            pts_temp = pts_e2;
            gf_temp = gf_e2
            gc_temp = gc_e2
            pg_temp = pg_e2
            pe_temp = pe_e2
            pp_temp = pp_e2
        elif pos == 3:
            nom_temp = eq3
            pts_temp = pts_e3
            gf_temp = gf_e3
            gc_temp = gc_e3
            pg_temp = pg_e3
            pe_temp = pe_e3
            pp_temp = pp_e3
        elif pos == 4:
            nom_temp = eq4
            pts_temp = pts_e4
            gf_temp = gf_e4
            gc_temp = gc_e4
            pg_temp = pg_e4
            pe_temp = pe_e4
            pp_temp = pp_e4
            
        dg_temp = gf_temp - gc_temp

        if grupo_actual == "A":
            if pts_temp > puntos1_a or (pts_temp == puntos1_a and dg_temp > dg1_a):
                mejor4_a = mejor3_a
                puntos4_a = puntos3_a
                gf4_a = gf3_a
                gc4_a = gc3_a
                dg4_a = dg3_a
                pg4_a = pg3_a
                pe4_a = pe3_a
                pp4_a = pp3_a
                mejor3_a = mejor2_a
                puntos3_a = puntos2_a
                gf3_a = gf2_a
                gc3_a = gc2_a
                dg3_a = dg2_a
                pg3_a = pg2_a
                pe3_a = pe2_a
                pp3_a = pp2_a
                mejor2_a = mejor1_a
                puntos2_a = puntos1_a
                gf2_a = gf1_a
                gc2_a = gc1_a
                dg2_a = dg1_a
                pg2_a = pg1_a
                pe2_a = pe1_a
                pp2_a = pp1_a
                mejor1_a = nom_temp
                puntos1_a = pts_temp
                gf1_a = gf_temp
                gc1_a = gc_temp
                dg1_a = dg_temp
                pg1_a = pg_temp
                pe1_a = pe_temp
                pp1_a = pp_temp
            elif pts_temp > puntos2_a or (pts_temp == puntos2_a and dg_temp > dg2_a):
                mejor4_a = mejor3_a
                puntos4_a = puntos3_a
                gf4_a = gf3_a
                gc4_a = gc3_a
                dg4_a = dg3_a
                pg4_a = pg3_a
                pe4_a = pe3_a
                pp4_a = pp3_a
                mejor3_a = mejor2_a
                puntos3_a = puntos2_a
                gf3_a = gf2_a
                gc3_a = gc2_a
                dg3_a = dg2_a
                pg3_a = pg2_a
                pe3_a = pe2_a
                pp3_a = pp2_a
                mejor2_a = nom_temp
                puntos2_a = pts_temp
                gf2_a = gf_temp
                gc2_a = gc_temp
                dg2_a = dg_temp
                pg2_a = pg_temp
                pe2_a = pe_temp
                pp2_a = pp_temp
            elif pts_temp > puntos3_a or (pts_temp == puntos3_a and dg_temp > dg3_a):
                mejor4_a = mejor3_a
                puntos4_a = puntos3_a
                gf4_a = gf3_a
                gc4_a = gc3_a
                dg4_a = dg3_a
                pg4_a = pg3_a
                pe4_a = pe3_a
                pp4_a = pp3_a
                mejor3_a = nom_temp
                puntos3_a = pts_temp
                gf3_a = gf_temp
                gc3_a = gc_temp
                dg3_a = dg_temp
                pg3_a = pg_temp
                pe3_a = pe_temp
                pp3_a = pp_temp
            else:
                mejor4_a = nom_temp
                puntos4_a = pts_temp
                gf4_a = gf_temp
                gc4_a = gc_temp
                dg4_a = dg_temp
                pg4_a = pg_temp
                pe4_a = pe_temp
                pp4_a = pp_temp
        else:
            if pts_temp > puntos1_b or (pts_temp == puntos1_b and dg_temp > dg1_b):
                mejor4_b = mejor3_b
                puntos4_b = puntos3_b
                gf4_b = gf3_b
                gc4_b = gc3_b
                dg4_b = dg3_b
                pg4_b = pg3_b
                pe4_b = pe3_b
                pp4_b = pp3_b
                mejor3_b = mejor2_b
                puntos3_b = puntos2_b
                gf3_b = gf2_b
                gc3_b = gc2_b
                dg3_b = dg2_b
                pg3_b = pg2_b
                pe3_b = pe2_b
                pp3_b = pp2_b
                mejor2_b = mejor1_b
                puntos2_b = puntos1_b
                gf2_b = gf1_b
                gc2_b = gc1_b
                dg2_b = dg1_b
                pg2_b = pg1_b
                pe2_b = pe1_b
                pp2_b = pp1_b
                mejor1_b = nom_temp
                puntos1_b = pts_temp
                gf1_b = gf_temp
                gc1_b = gc_temp
                dg1_b = dg_temp
                pg1_b = pg_temp
                pe1_b = pe_temp
                pp1_b = pp_temp
            elif pts_temp > puntos2_b or (pts_temp == puntos2_b and dg_temp > dg2_b):
                mejor4_b = mejor3_b
                puntos4_b = puntos3_b
                gf4_b = gf3_b
                gc4_b = gc3_b
                dg4_b = dg3_b
                pg4_b = pg3_b
                pe4_b = pe3_b
                pp4_b = pp3_b
                mejor3_b = mejor2_b
                puntos3_b = puntos2_b
                gf3_b = gf2_b
                gc3_b = gc2_b
                dg3_b = dg2_b
                pg3_b = pg2_b
                pe3_b = pe2_b
                pp3_b = pp2_b
                mejor2_b = nom_temp
                puntos2_b = pts_temp
                gf2_b = gf_temp
                gc2_b = gc_temp
                dg2_b = dg_temp
                pg2_b = pg_temp
                pe2_b = pe_temp
                pp2_b = pp_temp
            elif pts_temp > puntos3_b or (pts_temp == puntos3_b and dg_temp > dg3_b):
                mejor4_b = mejor3_b
                puntos4_b = puntos3_b
                gf4_b = gf3_b
                gc4_b = gc3_b
                dg4_b = dg3_b
                pg4_b = pg3_b
                pe4_b = pe3_b
                pp4_b = pp3_b
                mejor3_b = nom_temp
                puntos3_b = pts_temp
                gf3_b = gf_temp
                gc3_b = gc_temp
                dg3_b = dg_temp
                pg3_b = pg_temp
                pe3_b = pe_temp
                pp3_b = pp_temp
            else:
                mejor4_b = nom_temp
                puntos4_b = pts_temp
                gf4_b = gf_temp
                gc4_b = gc_temp
                dg4_b = dg_temp
                pg4_b = pg_temp
                pe4_b = pe_temp
                pp4_b = pp_temp



if puntos1_a == puntos2_a and dg1_a == dg2_a:
    
    print(f"EMPATE EN PUNTOS Y DIFERENCIA DE GOLES EN EL GRUPO A")
    print(f"PARTIDO DE DESEMPATE: {mejor1_a} VS {mejor2_a}")

    print(f"Ingrese goles anotados por {mejor1_a}: ")
    g_des_a1 = int(input())
    if g_des_a1 < 0:
        while True:
            print("ERROR: ingrese cantidades positivas y validas ")
            g_des_a1 = int(input())
            if g_des_a1 >= 0: break

    print(f"Ingrese goles anotados por {mejor2_a}: ")
    g_des_a2 = int(input())
    if g_des_a2 < 0:
        while True:
            print("ERROR: ingrese cantidades positivas y validas ")
            g_des_a2 = int(input())
            if g_des_a2 >= 0: break

    if g_des_a2 > g_des_a1:
        temp_nom = mejor1_a
        mejor1_a = mejor2_a
        mejor2_a = temp_nom
    elif g_des_a1 == g_des_a2:
        print("EMPATE EN DESEMPATE DE GRUPO A, SE DEFINE POR PENALES.")
        print(f"Ingrese penales anotados por {mejor1_a}: ")
        p_des_a1 = int(input())
        if p_des_a1 < 0:
            while True:
                print("ERROR: ingrese cantidades positivas y validas ")
                p_des_a1 = int(input())
                if p_des_a1 >= 0: break

        print(f"Ingrese penales anotados por {mejor2_a}: ")
        p_des_a2 = int(input())
        if p_des_a2 < 0:
            while True:
                print("ERROR: ingrese cantidades positivas y validas ")
                p_des_a2 = int(input())
                if p_des_a2 >= 0: break

        while p_des_a1 == p_des_a2:
            print("Empate en penales! Nueva ronda:")
            print(f"Ingrese penales de {mejor1_a}: ")
            p_des_a1 = int(input())
            print(f"Ingrese penales de {mejor2_a}: ")
            p_des_a2 = int(input())

        if p_des_a2 > p_des_a1:
            temp_nom = mejor1_a
            mejor1_a = mejor2_a
            mejor2_a = temp_nom

if puntos1_b == puntos2_b and dg1_b == dg2_b:
    print(f"EMPATE EN PUNTOS Y DIFERENCIA DE GOLES EN EL GRUPO B")
    print(f"PARTIDO DE DESEMPATE: {mejor1_b} VS {mejor2_b}")


    print(f"Ingrese goles anotados por {mejor1_b}: ")
    g_des_b1 = int(input())
    if g_des_b1 < 0:
        while True:
            print("ERROR: ingrese cantidades positivas y validas ")
            g_des_b1 = int(input())
            if g_des_b1 >= 0:
                break

    print(f"Ingrese goles anotados por {mejor2_b}: ")
    g_des_b2 = int(input())
    if g_des_b2 < 0:
        while True:
            print("ERROR: ingrese cantidades positivas y validas ")
            g_des_b2 = int(input())
            if g_des_b2 >= 0:
                break

    if g_des_b2 > g_des_b1:
        temp_nom = mejor1_b; mejor1_b = mejor2_b; mejor2_b = temp_nom
    elif g_des_b1 == g_des_b2:
        print("\EMPATE EN DESEMPATE DE GRUPO B, SE DEFINE POR PENALES.")
        print(f"Ingrese penales anotados por {mejor1_b}: ")
        p_des_b1 = int(input())
        if p_des_b1 < 0:
            while True:
                print("ERROR: ingrese cantidades positivas y validas ")
                p_des_b1 = int(input())
                if p_des_b1 >= 0:
                    break

        print(f"Ingrese penales anotados por {mejor2_b}: ")
        p_des_b2 = int(input())
        if p_des_b2 < 0:
            while True:
                print("ERROR: ingrese cantidades positivas y validas ")
                p_des_b2 = int(input())
                if p_des_b2 >= 0:
                    break

        while p_des_b1 == p_des_b2:
            print("Empate en penales! Nueva ronda:")
            print(f"Ingrese penales de {mejor1_b}: ")
            p_des_b1 = int(input())
            print(f"Ingrese penales de {mejor2_b}: ")
            p_des_b2 = int(input())

        if p_des_b2 > p_des_b1:
            temp_nom = mejor1_b
            mejor1_b = mejor2_b
            mejor2_b = temp_nom



print("\n TABLA DE POSICIONES GRUPO A")
print(f"1° LUGAR | {mejor1_a} | {puntos1_a} pts | GF: {gf1_a} | GC: {gc1_a} | DG: {dg1_a} | PG: {pg1_a} | PE: {pe1_a} | PP: {pp1_a}")
print(f"2° LUGAR | {mejor2_a} | {puntos2_a} pts | GF: {gf2_a} | GC: {gc2_a} | DG: {dg2_a} | PG: {pg2_a} | PE: {pe2_a} | PP: {pp2_a}")
print(f"3° LUGAR | {mejor3_a} | {puntos3_a} pts | GF: {gf3_a} | GC: {gc3_a} | DG: {dg3_a} | PG: {pg3_a} | PE: {pe3_a} | PP: {pp3_a}")
print(f"4° LUGAR | {mejor4_a} | {puntos4_a} pts | GF: {gf4_a} | GC: {gc4_a} | DG: {dg4_a} | PG: {pg4_a} | PE: {pe4_a} | PP: {pp4_a}")

print("\n TABLA DE POSICIONES GRUPO B")
print(f"1° LUGAR | {mejor1_b} | {puntos1_b} pts | GF: {gf1_b} | GC: {gc1_b} | DG: {dg1_b} | PG: {pg1_b} | PE: {pe1_b} | PP: {pp1_b}")
print(f"2° LUGAR | {mejor2_b} | {puntos2_b} pts | GF: {gf2_b} | GC: {gc2_b} | DG: {dg2_b} | PG: {pg2_b} | PE: {pe2_b} | PP: {pp2_b}")
print(f"3° LUGAR | {mejor3_b} | {puntos3_b} pts | GF: {gf3_b} | GC: {gc3_b} | DG: {dg3_b} | PG: {pg3_b} | PE: {pe3_b} | PP: {pp3_b}")
print(f"4° LUGAR | {mejor4_b} | {puntos4_b} pts | GF: {gf4_b} | GC: {gc4_b} | DG: {dg4_b} | PG: {pg4_b} | PE: {pe4_b} | PP: {pp4_b}")



print("GRAN FINAL DE TORNEO")
print(f"   {mejor1_a} (1° Grupo A) VS {mejor1_b} (1° Grupo B)   ")

print(f"Ingrese los goles anotados por {mejor1_a}: ")
goles_a = int(input())
if goles_a < 0:
    while True:
        print("ERROR: ingrese cantidades positivas y validas ")
        goles_a = int(input())
        if goles_a >= 0:
            break

print(f"Ingrese los goles anotados por {mejor1_b}: ")
goles_b = int(input())
if goles_b < 0:
    while True:
        print("ERROR: ingrese cantidades positivas y validas ")
        goles_b = int(input())
        if goles_b >= 0:
            break

if goles_a > goles_b:
    print(f"EL CAMPEÓN ES {mejor1_a} CON {goles_a} GOLES A FAVOR!")
elif goles_b > goles_a:
    print(f"EL CAMPEÓN ES {mejor1_b} CON {goles_b} GOLES A FAVOR!")
else:
    print("EMPATE EN GOLES! El partido se define por PENALES.")
    print(f"Ingrese los penales anotados por {mejor1_a}: ")
    penales_a = int(input())
    if penales_a < 0:
        while True:
            print("ERROR: ingrese cantidades positivas y validas ")
            penales_a = int(input())
            if penales_a >= 0:
                break

    print(f"Ingrese los penales anotados por {mejor1_b}: ")
    penales_b = int(input())
    if penales_b < 0:
        while True:
            print("ERROR: ingrese cantidades positivas y validas ")
            penales_b = int(input())
            if penales_b >= 0:
                break

    while penales_a == penales_b:
        print("Empate en penales! Se ejecuta una nueva ronda:")
        print(f"Ingrese los penales anotados por {mejor1_a}: ")
        penales_a = int(input())
        if penales_a < 0:
            while True:
                print("ERROR: ingrese cantidades positivas y validas ")
                penales_a = int(input())
                if penales_a >= 0:
                    break

        print(f"Ingrese los penales anotados por {mejor1_b}: ")
        penales_b = int(input())
        if penales_b < 0:
            while True:
                print("ERROR: ingrese cantidades positivas y validas ")
                penales_b = int(input())
                if penales_b >= 0:
                    break

    if penales_a > penales_b:
        print(f"EL CAMPEÓN ES {mejor1_a} GANANDO EN PENALES ({penales_a} a {penales_b})")
    else:
        print(f"\n¡EL CAMPEÓN ES {mejor1_b} GANANDO EN PENALES ({penales_b} a {penales_a})")
