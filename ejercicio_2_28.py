numero= input("ingrese un numero entero natural: ")
suma=0

for i in range(int(numero)):
    indice= i + 1
    suma= suma + indice
    if indice != int(numero):
        print(indice,"+ ",end="")
    else:
        print(indice, "=", suma)
