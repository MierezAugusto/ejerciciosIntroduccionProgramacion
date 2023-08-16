letra = input("Ingrese la primera letra: ")
letra2 = input("Ingrese la segunda letra: ")

letrasOrdenadas= [letra[0], letra2[0]]

letrasOrdenadas.sort()

letra = letrasOrdenadas[0]
letra2 = letrasOrdenadas[1]

print(letra, letra2)