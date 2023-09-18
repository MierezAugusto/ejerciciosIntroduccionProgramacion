vueltas=1
while vueltas == 1:
    nota = int(input("Ingrese Nota del Alumno: "))
    if nota !=0:
        if nota == 10:
            print("A")
        elif nota == 8 or nota == 9:
            print("B")
        elif nota == 6 or nota == 7:
            print("C")
        elif nota == 4 or nota == 5:
            print("D")
        elif nota > 0 and nota < 4:
            print("E")
        else:
            print("Rango nota invalido")
    else:
        vueltas=0