num = int(input("Ingresa un numero: "))
contador = 0

while num > 0:

    contador += 1

    num = num // 10

print(contador)

print("___________________")

num = str(input("Ingresa un numero: "))

print(len(num))

print("___________________")

num = str(input("Ingresa un numero: "))
contador = 0

for i in range (len(num)):
    contador += 1 

print(contador)
