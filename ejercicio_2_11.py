num = 0
max_num = 0
contador = 0
max_contador= 0
for i in range (10):
    if i == 0:
        num= int(input("Debe ingresar 10 numeros, ingrese el primer: "))
        max_num = num
        contador = contador+1 
    else: 
        num = int(input("ingrese otro numero: "))
        contador = contador+1
        if num > max_num:
            max_num = num
            max_contador = contador

print("Numero maximo de ingresado es:", max_num, " en la posicion:", max_contador)

