print("ingrese la tabla que necesite")
tabla=int(input())
for mul in range(1,11):
    igual= tabla*mul
    print(tabla, "*" ,mul, "=" , igual)
for intento in range(177):
    print("desea otra tabla?(1 si, 2 no)")
    ntabla=int(input())
    if ntabla==1:
        print("ingrese la tabla que necesite")
        ptabla=int(input())
        for mul in range(1,11):
            igual= ptabla*mul
            print(ptabla, "*" ,mul, "=" , igual)
    else:
        if ntabla != 2:
            for error in range (1233):
                print("ERROR: tiene que ser 1-si 2-no")
                print ("desea otra tabla?")
                ntabla=int(input())
                if ntabla==1:
                     print("ingrese la tabla que necesite")
                     ptabla=int(input())
                     for mul in range(1,11):
                         igual= ptabla*mul
                         print(ptabla, "*" ,mul, "=" , igual)
                else:
                    break 
            
        else:
            break 
        
        
       
    
