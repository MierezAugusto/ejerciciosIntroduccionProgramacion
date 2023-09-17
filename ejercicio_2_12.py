palabra= str(input("Ingrese una palabla: "))
contador = len(palabra)

for i in range(len(palabra)+1):
    if contador != 0:
        print(palabra[contador-1])
        contador -= 1