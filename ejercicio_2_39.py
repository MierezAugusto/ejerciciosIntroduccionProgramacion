num= int(input("¿Que tabla de multiplicar quieres practicar?: "))
correctos=0
incorrectos=0
for i in range(1,11):
    resultado = i * num
    print(num, "*", i, "= ",end="")
    respuesta=int(input())
    if respuesta == resultado:
        print("Valor correcto")
        correctos+=1
    else:
        print("Lo siento se a equivocado")
        print("La respuesta correcta es",resultado)
        incorrectos+=1

print("Has acertado",correctos,"veces de 10")