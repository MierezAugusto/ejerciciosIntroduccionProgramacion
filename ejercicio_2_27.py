par=0
suma_par=0

for i in range(10):
    num=int(input("Ingrese un numero: "))
    if num % 2 == 0:
        par += 1 
        suma_par += num
        
promedio = suma_par/par

print(promedio)