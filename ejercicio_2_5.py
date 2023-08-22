num = int(input("Ingrese un numero entero positivo: "))
numeros = []
contador = 0

for i in range(num):    
    contador = contador + 1 
    if contador % 2 == 1:
        numeros.append(str(contador))

print(", ".join(numeros))



