from math import pi

radio = float(input("Ingrese el radio del ciculo: "))

area = pi * radio ** 2

print("El area del circulo es igual a {:.2f}".format(area) )

circunferencia = 2 * pi * radio

print("La circunferencia del circulo es igual a: {:.2f}".format(circunferencia))