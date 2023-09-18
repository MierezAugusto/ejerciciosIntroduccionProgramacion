max_nota = 0 
max_edad= 0

for i in range(5):
    if i == 0:
        max_nota= float(input("Ingrese Nota de alumno: " ))
        max_edad= int(input("Ingrese Edad del alumno: "))
        
        
    else:
        nota= float(input("Ingrese Nota de alumno: " ))
        edad= int(input("Ingrese Edad del alumno: "))
        if max_nota < nota:
            max_nota = nota
            max_edad = edad

print(" Nota: ",max_nota,"\n","Edad: ", max_edad)