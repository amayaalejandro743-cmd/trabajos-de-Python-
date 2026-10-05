nombre = []
kms = []
total_kms = []
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

print("Ingrese la cantidad de conductores: ")
condustores = int(input())  
while condustores < 1:
    print("la cantidad de conductores no puede ser menor a 1, ingrese nuevamente")
    condustores = int(input())
print(" ")

for i in range(1, condustores + 1):
    
    print(F"Ingrese el nombre del { i } conductor: ")
    nombre_conductor = str(input()) 
    nombre.append(nombre_conductor)
    print(" ")

    km_dia = []  # Reiniciar la lista para cada conductor
    for dia in dias:
        print(f"Ingrese los kilometros que ha conducido el conductor el {dia}: ")
        km = float(input())
        while km < 0:
            print("los kilometros no pueden ser negativos, ingrese nuevamente")
            km = float(input()) 
        km_dia.append(km)
    kms.append(km_dia)
    total_kms.append(sum(km_dia))  # Calcular el total de kilómetros para el conductor actual
    print(" ")

for j in range (len(nombre)):
    print(f"El conductor {nombre[j]} ha conducido un total de {total_kms[j]} kilometros en la semana.") 
    j = j + 1
