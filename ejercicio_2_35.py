numero= input("ingrese un numero entero: ")
suma=0

for i in range(int(numero)):
    num_i= i + 1
    if num_i % 2 == 0:
        suma = suma + num_i 
        if num_i != int(numero):
            print(num_i,",",end="")
        else:
            print(num_i, "SON LOS NUMEROS PARES COMPRENDIDOS ENTRE EL 1 Y EL", numero)
            print("LA SUMA DE DICHOS NUMEROS ES:", suma)