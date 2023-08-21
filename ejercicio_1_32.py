num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

numeros = [num1, num2, num3]

numeros.sort()

a = numeros[0]
b = numeros[1]
c = numeros[2]

if a + b < c:
    c = int(input(f"Ingrese un numero menor o igual a {a+b}: "))
else:
    c = c
    
def tipoDeTriangulos (a, b, c):
    if a == b and a == c:
        return "Se forma un triangulo Equilatero"
    elif a != b and a != c:
        return "Se forma un triangulo Escaleno"
    else:
        return "Se forma un triangulo Isosceles" 
    
print(tipoDeTriangulos(a, b, c))
