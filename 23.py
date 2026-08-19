l_asignatura=[]
l_nota=[]
#aqui se hace el registro de las asignaturas y notas
while True:
    print("escriba la asignatura a registrar")
    asignatura=str(input())
    print("digite la nota de la asignatura")
    nota=float(input())
    while nota<0 or nota>5:
        print("ERROR: dijite una nota valida")
        nota=float(input())

    l_asignatura.append(asignatura)
    l_nota.append(nota)

    print("desea registrar otra asignatura?  1-si 2-no")
    continua=int(input())
    while continua!=1 and continua!=2:
        print("ERROR: dijiete una opcion valida")
        continua=int(input())
    if continua==2:
        break
# aqui se hace el analisis de las asignaturas que debe repetir el estudiante
l_repetir=[]
i=0
while i<len(l_asignatura):
    if l_nota[i]<3:
        l_repetir.append(l_asignatura[i])
    i=i+1

print("las asignaturas que debe repetir son", l_repetir)
    
            
           
        
