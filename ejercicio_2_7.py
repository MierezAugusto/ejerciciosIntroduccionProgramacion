altura = int(input("Introduce la altura del triángulo: "))
if altura > 0:
    for i in range(altura):
        for ii in range(i+1):
            print("*", end="")
        print("")
else: 
    print("Debe ser un numero entero y positivo inicia otra vez")