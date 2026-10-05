print("escriba un numero menor a 1000")
num=int(input())
if num>=1 and num<=9:
    elevar=num**2
    print("el numero fue elevado al cuadrado, resulta:",elevar)
elif num>=10 and num<=99:
    multi=num*2
    print("el numero fue multiplicado por 2, resulta:",multi)
elif num>=100 and num<=999:
    resta=num - 100
    print("el numero fue restado en 100, resulta:",resta)
else:
    print("numero no valido")
    
    
