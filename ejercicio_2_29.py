numPositivos= 0
numNegativos= 0
listanum=[]
for i in range(20):
    if i == 0:
        numero=int(input("Debe ingresar 20 numeros, ingrese un numero aqui: "))
        listanum.append(numero)
    else:    
        numero=int(input("Ingrese el siguiente numero aqui: "))
        listanum.append(numero)
    if listanum[i] % 2 == 0:
        numPositivos = numPositivos+1
    else:
        numNegativos = numNegativos+1
print(" La cantidad de numeros positivos son", numPositivos,"\n","La cantidad de numeros negativos son:", numNegativos)