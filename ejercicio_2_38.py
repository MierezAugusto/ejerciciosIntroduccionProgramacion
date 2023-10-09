cant_A=0
cant_E=0
cant_I=0
cant_O=0
cant_U=0
vocales=["A","E","I","O","U"]
caracter=""

while caracter != "*":
    print("Para finalizar ingrese *")
    caracter=input("Ingrese un caracter:")
    if caracter == "a" or caracter == "A":
        cant_A +=1
    elif caracter == "e" or caracter == "E":
        cant_E +=1
    elif caracter == "i" or caracter == "I":
        cant_I +=1
    elif caracter == "o" or caracter == "O":
        cant_O +=1
    elif caracter == "u" or caracter == "U":
        cant_U +=1

imprimir=[cant_A,cant_E,cant_I,cant_O,cant_U]

for i in range(5):
    print("LA CANTIDAD DE VOCALES ",vocales[i]," INGRESADAS:",imprimir[i])
