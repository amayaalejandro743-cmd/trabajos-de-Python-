mejor1=" "
mejor2=" "
mejor3=" "
mejor4=" "
mejor5=" "
mejor6=" "
puntos1= 0
puntos2=0
puntos3=0
puntos4=0
puntos5=0
puntos6=0
equipos=0
entra=False
while equipos <= 5:
    equipos +=1
    puntos=0
    print("ingrese el nombre del equipo: ",equipos)
    nom=str(input())
    for juegos in range(1,6):
        print("ingrese reultado del juego: ",juegos, "°")
        print ("1-victoria, 2-empate, 3-derrota")
        resultado=int(input())
        if resultado != 1 and resultado != 2 and resultado !=3:
            entra=True
            while entra :
                print ("ERROR:ingrese un dato valido")
                print("ingrese reultado del juego: ",juegos, "°")
                print ("1-victoria, 2-empate, 3-derrota")
                resultado=int(input())
                if  resultado == 1 or resultado ==2 or resultado ==3:
                    break
                else:
                    print(" ")
        if resultado ==1 :
            print(f"partido #{juegos} ganado")
            print("suma 3 puntos")
            puntos=puntos+3
        elif resultado == 2:
             print(f"partido #{juegos} empatado")
             print("suma 1 puntos")
             puntos=puntos+1
        else:
            print(f"partido #{juegos} perdido")
            print("suma 0 puntos")
            puntos=puntos+0
        print(f"puntos del equipo {nom} son {puntos} ")


        if puntos < puntos1:
            mejor6 = mejor5; puntos6 = puntos5
            mejor5 = mejor4; puntos5 = puntos4
            mejor4 = mejor3; puntos4 = puntos3
            mejor3 = mejor2; puntos3 = puntos2
            mejor2 = mejor1; puntos2 = puntos1
            mejor1 = nom;    puntos1 = puntos
        elif puntos < puntos2:
            mejor6 = mejor5; puntos6 = puntos5
            mejor5 = mejor4; puntos5 = puntos4
            mejor4 = mejor3; puntos4 = puntos3
            mejor3 = mejor2; puntos3 = puntos2
            mejor2 = nom;    puntos2 = puntos
        elif puntos < puntos3:
            mejor6 = mejor5; puntos6 = puntos5
            mejor5 = mejor4; puntos5 = puntos4
            mejor4 = mejor3; puntos3 = puntos3
            mejor3 = nom;    puntos3 = puntos
        elif puntos < puntos4:
            mejor6 = mejor5; puntos6 = puntos5
            mejor5 = mejor4; puntos5 = puntos4
            mejor4 = nom;    puntos4 = puntos
        elif puntos < puntos5:
            mejor6 = mejor5; puntos6 = puntos5
            mejor5 = nom;    puntos5 = puntos
        else:
            mejor6 = nom
            puntos6 = puntos


print("       TABLA DE POSICIONES       ")

print(f"1° LUGAR | {mejor1} | {puntos1} pts")
print(f"2° LUGAR | {mejor2} | {puntos2} pts")
print(f"3° LUGAR | {mejor3} | {puntos3} pts")
print(f"4° LUGAR | {mejor4} | {puntos4} pts")
print(f"5° LUGAR | {mejor5} | {puntos5} pts")
print(f"6° LUGAR | {mejor6} | {puntos6} pts")

                
