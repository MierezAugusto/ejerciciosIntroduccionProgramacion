sumamult3=0
valmult5=0
sumvalpar=0

for i in range(50):
    if i == 0:
        num=int(input("Debe ingresar 50 numeros, ingrese un numero aqui: "))
        if num % 3 == 0:
            sumamult3 += num 
        if num % 5 == 0:
            valmult5= valmult5 + 1
        if num % 2 == 0:
            sumvalpar= sumvalpar + num
    else:    
        num=int(input("Ingrese el siguiente numero aqui: "))
        if num % 3 == 0:
            sumamult3 += num 
        if num % 5 == 0:
            valmult5= valmult5 + 1
        if num % 2 == 0:
            sumvalpar= sumvalpar + num

print("La sumatoria de los valores multiplos de 3 es:",sumamult3)
print("La cantidad d valores multiplos de 5 son:",valmult5)
print("La sumatoria de los valores que se ingresan y son pares:",sumvalpar)