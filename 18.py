hombre=0
mujer =0
ach=0
acm=0
notanovalida= True
for i in range (1,21):
    print("dijite si es 1-hombres, o  2-mujeres")
    sex=int(input())
    if sex == 1:
        hombre+=1
        print("ingrese la nota", i)
        notah=float(input())
        if notah<0 or notah>5:
            while notanovalida:
                print("ERROR:nota no valida ")
                print("ingrese otra vez la nota de 1 a 5")
                notah=float(input())
                if notah>0 and notah<=5:
                     break
                else:
                    print("ERROR")
                    i=i-2
        else:
            ach=ach+notah
            promh=ach/ach

    elif sex == 2:
        mujer+=1
        print("ingrese la nota", i)
        notam=float(input())
        if notam<0 or notam>5:
            while notanovalida:
                print("ERROR:nota no valida ")
                print("ingrese otra vez la nota de 1 a 5")
                notam=float(input())
                if notam>0 and notam<=5:
                     break
                else:
                    print("ERROR")
                    i=i-2
        else:
            acm=acm+notam
            promm=acm/acm
    else:
        print("ERROR")
        i=i-2
print(f"promedio de las notas de los hombres es: {promh}")
print(f"promedio de las notas de las mujeres es: {promm}")
        
if promh>promm:
    print("mejor promedio fue el de los hombres")
else:
    print("mejor promedio fue el de las mujeres")

    
    
