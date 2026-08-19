inventario = """
1 Coca-Cola 1.4L retornable = $3450
2 Powerade = $2940.99
3 Monster = $3300.99
4 Agua Ciel 1L = $1200
5 Jugos del valle 1.4L = $2500
"""

lunes_registrado = 0
martes_registrado = 0
miercoles_registrado = 0
jueves_registrado = 0
viernes_registrado = 0
sabado_registrado = 0

precio_factura = 0
total_vendido = 0
total_descuento = 0
cantidad_tiendas = 0
LIMITE_DESCUENTO = 260000

registro_total = ""

print("Coca-Cola")
print("BIENVENIDA VALLEDUPAR")
print("Esta es nuestra nueva plataforma de mercado para ustedes y de ustedes")

while True:
    print("seleccione el numero del dia que desea registrar")
    print("1 Lunes")
    print("2 Martes")
    print("3 Miercoles")
    print("4 Jueves")
    print("5 Viernes")
    print("6 Sabado")
    print("7 Domingo")
    dia = int(input())
    while dia < 1 or dia > 7:
        print("ERROR:ingrese un numero de dia valido")
        dia = int(input())

    if dia == 7:
        print("el domingo no se trabaja, seleccione otro dia")
        continue
    elif dia == 1:
        if lunes_registrado == 1:
            print("el dia Lunes ya fue registrado")
            continue
        nombre_dia = "Lunes"
        lunes_registrado = 1
    elif dia == 2:
        if martes_registrado == 1:
            print("el dia Martes ya fue registrado")
            continue
        nombre_dia = "Martes"
        martes_registrado = 1
    elif dia == 3:
        if miercoles_registrado == 1:
            print("el dia Miercoles ya fue registrado")
            continue
        nombre_dia = "Miercoles"
        miercoles_registrado = 1
    elif dia == 4:
        if jueves_registrado == 1:
            print("el dia Jueves ya fue registrado")
            continue
        nombre_dia = "Jueves"
        jueves_registrado = 1
    elif dia == 5:
        if viernes_registrado == 1:
            print("el dia Viernes ya fue registrado")
            continue
        nombre_dia = "Viernes"
        viernes_registrado = 1
    else:
        if sabado_registrado == 1:
            print("el dia Sabado ya fue registrado")
            continue
        nombre_dia = "Sabado"
        sabado_registrado = 1

    registro_total = registro_total + """Dia: """ + nombre_dia + """ """



    while True:
        print("ingrese el nombre de su tienda")
        nom_tienda = str(input())
        while nom_tienda == "":
            print("ERROR: el nombre de la tienda no puede estar vacio")
            print("ingrese el nombre de su tienda")
            nom_tienda = str(input())

        cantidad_tiendas = cantidad_tiendas + 1
        print("bienvenido", nom_tienda)
        print("tenemos para ofrecerle", inventario)

        precio_factura = 0

        while True:
            print("seleccione el numero del producto que desea agregar a su carrito")
            producto = int(input())
            while producto != 1 and producto != 2 and producto != 3 and producto != 4 and producto != 5:
                print("ERROR:ingrese un numero de producto valido")
                producto = int(input())

            if producto == 1:
                precio = 3450
            elif producto == 2:
                precio = 2940.99
            elif producto == 3:
                precio = 3300.99
            elif producto == 4:
                precio = 1200
            else:
                precio = 2500

            print("digite la cantidad deseada")
            cantidad = int(input())
            while cantidad <= 0:
                print("cantidad invalida")
                print("ingrese una cantidad mayor a 0")
                cantidad = int(input())
            if cantidad>=4:
                prom= cantidad // 4
                print("tiene una promocion, por cada 4 productos 1 le sale gratis")
                valorprom = prom * precio
                #valorp=
                print(prom)
            

            valorp = cantidad * precio
            precio_factura = precio_factura + valorp

            print("El subtotal de la factura es:", precio_factura)
            print("Desea otro producto?")
            print("1-si, 2-no")
            otro = int(input())
            while otro != 1 and otro != 2:
                print("ERROR:ingrese un numero valido")
                print("Desea otro producto?")
                print("1-si, 2-no")
                otro = int(input())

            if otro == 1:
                print(inventario)
                continue
            elif otro == 2:
                if precio_factura > LIMITE_DESCUENTO:
                    descuento = precio_factura * 0.08
                    precio_final = precio_factura - descuento
                    print("Felicidades, su compra supera los", LIMITE_DESCUENTO)
                    print("Se le aplica un descuento del 8%")
                else:
                    descuento = 0
                    precio_final = precio_factura
                    print("Su compra no supera los", LIMITE_DESCUENTO)
                    print("No aplica para descuento")

                print("Tienda:", nom_tienda)
                print("Subtotal factura:", precio_factura)
                print("Descuento aplicado:", descuento)
                print("Total a pagar por la tienda:", precio_final)

                total_descuento = total_descuento + descuento
                total_vendido = total_vendido + precio_final

                registro_total = registro_total + """Tienda: """ + nom_tienda + """

   compro por: $""" + str(precio_factura) + """

   le descontamos: $""" + str(descuento) + """

   pago en total: $""" + str(precio_final) + """"""
                break

        print("Desea registrar otra tienda para este dia?")
        print("1-si, 2-no")
        otra_tienda = int(input())
        while otra_tienda != 1 and otra_tienda != 2:
            print("ERROR:ingrese un numero valido")
            otra_tienda = int(input())

        if otra_tienda == 1:
            continue
        elif otra_tienda == 2:
            break

    print("Desea registrar otro dia?")
    print("1-si, 2-no")
    otro_dia = int(input())
    while otro_dia != 1 and otro_dia != 2:
        print("ERROR:ingrese un numero valido")
        otro_dia = int(input())

    if otro_dia == 1:
        continue
    elif otro_dia == 2:
        registro_total = registro_total + """Resumen general

   tiendas atendidas: """ + str(cantidad_tiendas) + """

   total vendido: $""" + str(total_vendido) + """

   total en descuentos: $""" + str(total_descuento) + """ """

        print("Resumen general")
        print("tiendas atendidas:", cantidad_tiendas)
        print("total vendido:", total_vendido)
        print("total en descuentos:", total_descuento)
        break

print("Este es el registro de las ventas:")
print(registro_total)
