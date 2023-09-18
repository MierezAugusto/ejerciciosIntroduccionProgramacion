temp_max=0
temp_min=0

for i in range(7):
    temp=float(input("ingrese temperatura del dia: "))
    if i == 0:
        temp_max= temp
        temp_min=temp
    else:    
        if temp > temp_max:
            temp_max= temp
        else: 
            if temp < temp_min:
                temp_min= temp

print("Temperatura maxima de la semana:",temp_max)
print("Temperatura minima de la semana:",temp_min)