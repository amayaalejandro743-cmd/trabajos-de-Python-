print("ingrese la cantidad de camisas")
camisa=int(input())
print("ingrese el precio de la camisa")
precio=float(input())
vpagar = camisa * precio
if camisa >= 3:
    descuento = vpagar * 0.2
elif camisa < 3:
    descuento =vpagar* 0.1
else:
    descuento=0
nvpagar=vpagar - descuento
print("descuento es de:",descuento)
print("valor a pagar:", nvpagar)
    
    
    
