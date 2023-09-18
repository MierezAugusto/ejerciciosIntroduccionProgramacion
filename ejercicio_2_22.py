nota = float(input("Ingrese Nota del Alumno: "))

if nota < 5:
    print("En suspenso")
elif nota >= 5 and nota < 7:
    print("Aprobado")
elif nota >= 7 and nota < 9:
    print("Notable")
elif nota >= 9 and nota < 10:
    print("Sobresaliente")
else:
    print("Matricula de Honor")
