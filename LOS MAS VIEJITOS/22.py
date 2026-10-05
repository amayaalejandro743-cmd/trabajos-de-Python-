#diseñar un programa que pida el ingreso de una frace, despues el ingreso de una letra y contar cuantas beses la letra aparece dentro de la frace
frace=[]
cont=0
print("ingrese una frace")
fras=str(input())
frace.extend(fras)

print("ingrese una letra para contar cuantas veces esta en la frace ingresada")
letra=str(input())
for veces in frace:
    print(veces)
    if veces == letra:
        cont=cont+1
        
print(f"la letra ingresada :{letra}, esta {cont} en la frace {frace}")




