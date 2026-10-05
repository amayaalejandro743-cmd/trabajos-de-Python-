nombreg=[]
cedulag=[]

usuario=["usuario1","usuario2","suario3","usuario4","usuario5","usuario6","usuario7","usuario8","usuario9","usuario10"]
contraseña=[123,345,567,789,901,234,456,678,890,908]

mientras=[]

for us in range(1,11):
    while True:
        print(f"ingrese el nombre del usuario # {us}: " )
        nombre=str(input()).strip()
        if nombre.replace(" ", "").isalpha():
            nombreg.append(nombre)
               
            break
            print(" ")
        print("Nombre inválido. Por favor, ingrese solo letras.")
        print(" ")
        
    while True:
        try:
            print(f"ingrese la cedula del usuario # {us}: " )
            cedula =int(input())
            mientras.extend([cedula])
            cantidad=len(mientras)
            if  8 >= (cantidad) <=11:
                cedulag.append(cedula)
                break
            else:
                print("la cedula solo puede tener de 8 a 11 dijitos")
                print(" ")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
                          
for asig in usuario:
    print(f" se le asigna a {nombreg} identificado con cedula {cedulag} el usuario es {usuario} y contraseña {contraseña} ")








#prueba 


