print("ingrese el primer numero")
n1=float(input())
print("ingrese el segundo numero")
n2=float(input())
if n1>n2:
    suma=n1+n2
    print("la suma de los numeros es:",suma)
elif n2>n1:
    cuadrado1=n1**2
    cuadrado2=n2**2
    suma=cuadrado1+cuadrado2
    print("la suma de los 2 cuadrados de los numeros es",suma)
else:
    print("los numeros son iguales")
