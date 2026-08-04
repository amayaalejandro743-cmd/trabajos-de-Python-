print("CAJERO AUTOMATICO")
SALDO=500000
OPCION=1
while OPCION != 4:
    print("ingrese la opcion 1-consultar saldo, 2-retirar dinero, 3-depositar dinero, 4-salir")
    OPCION=int(input())
    if OPCION!=1 and OPCION!=2 and OPCION!=3 and OPCION!=4:
        while OPCION!=1 and OPCION!=2 and OPCION!=3 and OPCION!=4:
            print("opcion invalida")
            print("ingrese 1-consultar saldo, 2-retirar dinero, 3-depositar dinero, 4-salir ")
            OPCION=int(input())
            if OPCION==1 or OPCION==2 or OPCION==3 or OPCION==4:
                break
            else:
                print("ERROR")
    if OPCION==1:
        print(f"su saldo es saldo {SALDO}")
    elif OPCION==2:
        print("ingrese la cantidad a retirar")
        RETIRO=float(input())
        while RETIRO<=0:
            print("cantidad invalida")
            print("ingrese la cantidad a retirar")
            RETIRO=float(input())
            if RETIRO>0:
                break   
            else:
                print("ERROR")
        if RETIRO>SALDO:
            print("saldo insuficiente")
        else:
            SALDO=SALDO-RETIRO
            print(f"su saldo es {SALDO}")
    elif OPCION==3:
        print("ingrese la cantidad a depositar")
        DEPOSITO=float(input())
        while DEPOSITO<=0:
            print("cantidad invalida")
            print("ingrese la cantidad a depositar")
            DEPOSITO=float(input())
            if DEPOSITO>0:
                break   
            else:
                print("ERROR")
        SALDO=SALDO+DEPOSITO
        print(f"su saldo es {SALDO}")
    else:
        print("gracias por usar el cajero automatico")  



    

