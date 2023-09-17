num = int(input("Ingrese un numero entero positivo: "))

for i in range(num + 1):
    if i == 10:
        print(num)
    else:
        print(num, end=", ")
        num= num - 1 

"""numeros = []
contador = 0

for i in range(num + 1):    
    numeros.append(contador)
    contador = contador + 1 

numeros=sorted(numeros, reverse=True)

print(numeros)"""