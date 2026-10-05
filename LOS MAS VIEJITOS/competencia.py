import random
posiciones=[1,2,3,4,5]
acumulacion=[]
ronda=0
cor1=0
cor2=0
cor3=0
cor4=0
cor5=0
while True:
    ronda+= 1
    for corredor in range(1,6):
        if corredor== 1:
            pos=random.choice(posiciones)
            print(pos)
            cor1=cor1+pos
            continue
        elif corredor ==2:
            pos=random.choice(posiciones)
            print(pos)
            cor2=cor2+pos
            continue
        elif corredor== 3:
            pos=random.choice(posiciones)
            print(pos)
            cor3=cor3+pos
            continue
        elif corredor== 4:
            pos=random.choice(posiciones)
            print(pos)
            cor4=cor4+pos
            continue
        else:
            pos=random.choice(posiciones)
            print(pos)
            cor5=cor5+pos
            continue
    if cor1 >= 100 or cor2 >= 100 or cor3 >= 100 or cor4 >= 100 or cor5 >= 100:
        acumulacion.append(("corredor1", cor1))
        acumulacion.append(("corredor2", cor2))
        acumulacion.append(("corredor3", cor3))
        acumulacion.append(("corredor4", cor4))
        acumulacion.append(("corredor5", cor5))

        ordenados = sorted(acumulacion, key=lambda x: x[1])
        print(ordenados)

        ganador = ordenados[0]
        print(f"Gana {ganador[0]} con {ganador[1]} puntos")

        print("cerrando")
        break
