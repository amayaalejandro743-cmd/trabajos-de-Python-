acumuladors=0

print("ingrese nombre del admin del sistema")
us=str(input())
print(f"bienvenido {us}  este es tu sistema de confianza")

for i in range(1,3):
    print("ingrese el nombre del trabajador")
    trabajador=str(input())
    print(f"bienvenido {trabajador}  este es tu sistema de confianza")
    print(f"ingrese el salario su salario señor/ar {trabajador} ")
    salario=int(input())
    if salario<0:
        print("salario no valido")
    else:
        acumuladors=acumuladors + salario
    
prom=(acumuladors)/i
print(f"promedio de los salarios {prom}")
    
