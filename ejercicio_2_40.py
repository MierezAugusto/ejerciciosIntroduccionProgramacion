cantidades= int(input("Ingresar cantidad de numeros que desea ingresar: "))

numMax=0
numMenor=0
sumar=0
for i in range(cantidades):
    numeros=int(input("Ingrese un numero:"))
    sumar+=numeros
    if numeros > numMax:
        numMax= numeros
    elif numMenor == 0 or numeros < numMenor:
        numMenor = numeros
promedio= sumar / cantidades

print("El numero mayor introducido es",numMax,", el numero menor",numMenor,"y el promedio de todos los numeros es", promedio )