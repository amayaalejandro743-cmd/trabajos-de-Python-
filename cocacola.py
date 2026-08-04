inventario="""
1 Coca-Cola 1.4L retornable = $3450
2 Powerade= $ 2940.99
3 Monster= $3300.99
4 Agua Ciel 1L= $1200
5 Jugos del valle 1.4L= $2500
"""
precio_factura=0
total_vendido=0
cantidad_tiendas=0

print("Coca-Cola")
print("BIENVENIDA VALLEDUPAR ")
print("Esta es nuetra nueva plataforma de mercado para ustedes y de ustedes ")

while True:
    print("ingrese el nombre de su tienda")
    nom_tienda=str(input())
    cantidad_tiendas+=1
    print ("bienvenido", nom_tienda )
    print("tenemos para ofrecerle",
          inventario)
    while True:
        print ("seleccione el numero del producto que desea agregar a su carrito")
        producto=int(input())
        while producto !=1 and producto !=2 and producto !=3 and producto !=4 and producto !=5:
            print("ERROR:ingrese un numero de producto valido")
            producto=int(input())
            if producto ==1 or producto ==2 or producto ==3 or producto ==4 or producto ==5:
                break
        if producto ==1:
            print("dijite la cantidad deseada")
            cantidad=int(input())
            while cantidad<=0:
                print("cantidad invalida")
                print("ingrese una cantidad mayor a 0 ")
                cantidad=int(input())
                if cantidad>0:
                    break
            precio = 3450
            valorp=cantidad*precio
            precio_factura= precio_factura + valorp
        elif producto ==2:
            print("dijite la cantidad deseada")
            cantidad=int(input())
            while cantidad<=0:
                print("cantidad invalida")
                print("ingrese una cantidad mayor a 0 ")
                cantidad=int(input())
                if cantidad>0:
                    break 
            precio = 2940.99
            valorp=cantidad*precio
            precio_factura= precio_factura + valorp
        elif producto ==3:
            print("dijite la cantidad deseada")
            cantidad=int(input())
            while cantidad<=0:
                print("cantidad invalida")
                print("ingrese una cantidad mayor a 0 ")
                cantidad=int(input())
                if cantidad>0:
                    break 
            precio = 3300.99
            valorp=cantidad*precio
            precio_factura= precio_factura + valorp
        elif producto ==4:
            print("dijite la cantidad deseada")
            cantidad=int(input())
            while cantidad<=0:
                print("cantidad invalida")
                print("ingrese una cantidad mayor a 0 ")
                cantidad=int(input())
                if cantidad>0:
                    break    
            precio = 1200
        valorp=cantidad*precio
        precio_factura= precio_factura + valorp
    else :
        print("dijite la cantidad deseada")
        cantidad=int(input())
        while cantidad<=0:
            print("cantidad invalida")
            print("ingrese una cantidad mayor a 0 ")
            cantidad=int(input())
            if cantidad>0:
                break 
        precio = 2500
        valorp=cantidad*precio
        precio_factura= precio_factura + valorp
    
    print("El total de la factura es:" , precio_factura)
    print ("")


    
   
   
    
