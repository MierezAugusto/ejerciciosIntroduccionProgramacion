numero=int(input("Ingrese un numero: "))
if numero != 0:
    for divisor in range(1, numero + 1):
        if numero % divisor == 0:
            print(divisor)
else:
        print("El numero 0 no tiene divisores")

