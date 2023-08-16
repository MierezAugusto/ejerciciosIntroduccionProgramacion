def sumar(a, b):
    return a + b

suma = 0

num = float(input("Ingrese otro número (0 para terminar): "))

while num != 0:
    suma = sumar(suma, num)
    print("La suma de todos los números es:", suma)
    num = float(input("Ingrese otro número (0 para terminar): "))
print(suma)