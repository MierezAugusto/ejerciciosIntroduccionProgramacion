num = input("Ingresa un numero: ")
par=0
impar=0
posicion = 0
for i in range(len(num)):
    digito= int(num[posicion])
    if digito % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1
    posicion += 1 

print("Del numero ingresado de sus digitos",par, "son pares y", impar, "son impares")

