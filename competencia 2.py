baja=[]
media=[]
alta=[]
emer=[]
pasiente=0
while True:
    pasiente+=1
    print(f"ingrese el estado del pasiente {pasiente}")
    print("""1- atencion baja
2-atencion media
3-atencion alta
4 emergencia""")
    estado=int(input())
    if estado== 1:
        pri="baja"
        baja.append((pasiente,pri))
    elif estado==2:
        pri="media"
        media.append((pasiente,pri))
        
   
        
