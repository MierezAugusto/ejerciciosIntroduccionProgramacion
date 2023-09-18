cont_mayor=0
cont_menor=0

for i in range (10):
    num=int(input("Ingrese un numero: "))
    if num > 0:
        cont_mayor +=1
    else:
        cont_menor +=1

print(cont_mayor, cont_menor)