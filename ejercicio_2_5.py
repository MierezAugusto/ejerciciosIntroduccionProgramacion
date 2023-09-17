num = int(input("Ingrese un numero entero positivo: "))
numeros = []
contador = 0

for i in range(num):    
    contador = contador + 1 
    if contador % 2 == 1:
        numeros.append(str(contador))

print(", ".join(numeros))

print("_________________________________________________")

num = int(input("Ingrese un numero entero positivo: "))
contador = 0

while contador != 10:    
    contador = contador + 1 
    if contador % 2 == 1:
        if contador == 9:
            print(contador)
        else:
            print(contador, end=", ")
