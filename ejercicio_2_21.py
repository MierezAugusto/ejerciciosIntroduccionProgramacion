impar=0
par=0

for i in range(20):
    num=int(input("Ingrese un numero: "))
    if num % 2 == 0:
        par += 1 
    else:
        impar += 1 

print(par, impar)