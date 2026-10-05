print("ingrese la 1 nota")
n1=float(input()
print ("ingrese la 2 nota")
n2=float(input())
print ("ingrese la 3 nota")
n3=float(input())
promedio= (n1+n2+n3)/3
if promedio<3:
    print("reprobo")
    print (promedio)
elif promedio >=3 and promedio<4:
    print("regular")
    print (promedio)
else:
    print("exelente")
    print (promedio)
    
