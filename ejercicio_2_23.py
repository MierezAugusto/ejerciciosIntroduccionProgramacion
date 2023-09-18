vueltas=1 
menor_treita= 0
mayor_ochenta= 0 
entre_cinc_seten=0
while vueltas == 1:
    num= int(input("Ingrese numero: "))
    if num != 0:
        if num > 80:
            mayor_ochenta+=1
        elif num < 30:
            menor_treita +=1
        elif num >= 50 and num <= 75:
            entre_cinc_seten +=1
    else:
        vueltas=0
print("Cantidad de numeros entre 50 y 75: ",entre_cinc_seten)
print("Cantidad de numeros mayores de 80",mayor_ochenta)
print("Cantidad de numeros menores de 30:",menor_treita)