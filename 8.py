print("ingrese la 1° nota parcial")
n1=float(input())
print("ingrese la 2° nota parcial")
n2=float(input())
promedion = (n1+n2)/2
if promedion < 2:
    print("no puede presentar elexamen final, REPROBADO POR BAJO RENDIMIENTO, nota:",promedion)
elif promedion>=2:
    print("puede presentar el examen final ")
    print("ingrese la nota del examen final ")
    nf=float(input())
    if nf<2:
        print("nota final",nf)
    elif nf >= 2:
        p1=n1*0.3
        p2=n2*0.3
        pf=nf*0.4
        nota=p1+p2+pf
        if nota>=3:
            print("asiganatura aprobada,nota",nota)
        else:
            print("reprueba la materia, nota:",nota)
            if nf>=2:
                print("puede habilitar la materia")
                print("escriba el resultado de la recuperacion")
                rec=float(input())
                if rec>3:
                    print("materia aprobada,nota", rec)
                else:
                    print("reprobo")
