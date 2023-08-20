num_1 = float(input("Ingrese el primer numero: "))
num_2 = float(input("Ingrese el segundo numero: "))

numeros= [num_1, num_2]

numeros.sort(reverse=True)

num_1 = numeros[0]
num_2 = numeros[1]

print(num_1, num_2)