contador = 0

for i in range(10):
    num = int(input("Ingrese un numero: "))
    if num % 2 == 0:
        contador = contador + 1 

print("Se ingresaron "+ str(contador) + " numeros pares")
