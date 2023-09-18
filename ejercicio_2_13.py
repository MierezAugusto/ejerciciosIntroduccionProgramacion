frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")
contador = 0
posicion = 0

for i in range(len(frase)):
    if letra == frase[posicion-1]:
        contador = contador + 1
    posicion = posicion + 1

print("La letra ingresada aparece:",contador)