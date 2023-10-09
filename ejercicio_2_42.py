nombre=input("Ingrese Apellido y nombre del alumno: ")
materia=input("Ingrese materia cursada: ")
sumaNota=0
vueltas=True
contador=0

while vueltas == True:
    nota=int(input("Ingrese notas del Alumno: "))
    sumaNota = sumaNota + nota
    contador+=1
    if contador == 6 or nota == 0:
        vueltas=False

promedio= sumaNota / contador

print("APELLIDO Y NOMBRE DE ALUMNO:", nombre, "PROMEDIO:", promedio)

print("PROGAMA FINALIZADO")