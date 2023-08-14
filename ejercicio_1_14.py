num = int(input("Ingrese un Numero Entero para saber si es multiplo de 5:"))

if num == 0:
    print(str(num) + " no es multiplo de 5")

elif num % 5 == 0:
    print(str(num) + " es multiplo de 5")
else:
    print(str(num) + " no es multiplo de 5")