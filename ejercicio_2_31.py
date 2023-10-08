numMax=0
numMenor=0
vueltas= True

while vueltas:
    num=int(input("ingresar numeros mayores a cero o ingrese 0 para finalizar: "))
    if num != 0:
        if num > numMax:
            numMax= num
        if numMenor == 0 or num < numMenor:
            numMenor = num
    else:
        vueltas = False        
        
print("El numero maximo ingresado es:",numMax,"y","El numero menor ingresado es:", numMenor)