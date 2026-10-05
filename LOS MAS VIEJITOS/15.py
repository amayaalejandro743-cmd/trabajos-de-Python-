for i in range(1,6):
    print("ingrese el nombre del estudiante")
    nm=str(input())
    print(f"ingres la nota 1 de {nm}")
    n1=float(input())
    print(f"ingres la nota 2 de {nm}")
    n2=float(input())
    print(f"ingres la nota 2 de {nm}")
    n3=float(input())
    prom=(n1+n2+n3)/3

    if prom>3:
        print("aprobado")
    else:
        print("reprobo")
