print("ingrese la cantidad de panes")
cantidad=int(input())
print("ingrese el precio de los panes")
precio=int(input())
totalp=cantidad*precio
if cantidad>200:
    decuento=totalp*0.3
    de="30%"
elif cantidad > 100:
    descuento=totalp*0.2
    de="20%"
else:
    descuento=totalp*0.1
    de="10%"
totalpp = totalp - descuento
print("valor del descuento:", de)
print("valor del descuento",descuento)
print("valor a pagar",totalpp)

