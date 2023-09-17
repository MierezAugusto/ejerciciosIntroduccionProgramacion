num = input("ingrese un numero: ")
if num == "":
    print("Debe ingresar un numero inicie nuevamente")
else:
    contador = 0
    for i in num :
        contador += 1
    
    print(num[contador-1:contador])
