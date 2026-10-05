t_maxima = []
t_minimo = []
temperatura_media = []
dias = 0

while True:
    dias += 1
    print(f"ingrese la temperatura maxima en grados(°) del dia {dias}")
    maxima = float(input())
    while maxima < 0:
        print("la temperatura ingresada no puede ser menor a 0")
        print("ingresela nuevamente")
        maxima = float(input())
    t_maxima.append(maxima)
    print(" ")

    print(f"ingrese la temperatura minima en grados(°) del dia {dias}")
    minimo = float(input())
    while minimo < 0 or minimo > maxima:
        if minimo < 0:
            print("la temperatura ingresada no puede ser menor a 0")
            print("ingresela nuevamente")
            minimo = float(input())
        else:
            print("la temperatura menor no puede ser mayor a la ya registrada como mayor")
            print("ingrese la temperatura menor otra vez")
            minimo = float(input())
    t_minimo.append(minimo)
    print(" ")

    # temperatura media del dia
    media = (maxima + minimo) / 2
    temperatura_media.append(media)

    print("digite 1-si quiere registrar otro dia, 2-si no quiere registrar mas dias")
    con = int(input())
    while con != 1 and con != 2:
        print("ingrese una opcion valida 1-si quiere registrar otro dia, 2-si no quiere registrar mas dias")
        con = int(input())
    if con == 2:
        break


print(" Temperatura media de cada dia ")
for i in range(dias):
    print(f"Dia {i+1}: {temperatura_media[i]}°")


temp_min = min(temperatura_media)
temp_max = max(temperatura_media)

menos_temperatura = []
mas_temperatura = []
for i in range(dias):
    if temperatura_media[i] == temp_min:
        menos_temperatura.append(i + 1)
    if temperatura_media[i] == temp_max:
        mas_temperatura.append(i + 1)

print(" Dias con menor temperatura ")
print(f"Temperatura minima: {temp_min}° -> dia(s): {menos_temperatura}")

print(" Dias con mayor temperatura ")
print(f"Temperatura maxima: {temp_max}° -> dia(s): {mas_temperatura}")


print("ingrese una temperatura para buscar los dias cuya temperatura maxima coincide con ella")
buscar = float(input())
encontrados = []
for i in range(dias):
    if t_maxima[i] == buscar:
        encontrados.append(i + 1)

if len(encontrados) == 0:
    print(f"No existe ningun dia con temperatura maxima de {buscar}°")
else:
    print(f"Los dias con temperatura maxima de {buscar}° son: {encontrados}")


print("Clasificacion de los dias")
for i in range(dias):
    if 0 <= temperatura_media[i] <= 15:
        clasificacion = "frio"
    elif 16 <= temperatura_media[i] <= 26:
        clasificacion = "templado"
    else:
        clasificacion = "calido"
    print(f"Dia {i+1}: {temperatura_media[i]}° -> {clasificacion}")
        

    
    
