vueltas=1
while vueltas == 1:
    numero=int(input("Ingrese un numero: "))
    if numero > 0:
        cuadrado = numero * numero
        print(cuadrado)
    elif numero < 0:
            print("ERROR, El numero debe ser mayor que 0 o 0 para finalizar")
    elif numero == 0:
        vueltas= 0