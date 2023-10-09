produc_neg=1
sumarpos=0

for i in range(10):
    num=int(input("Ingrese un numero negativo o positivo diferente de 0: "))
    if num == 0:
        print("El numero ingresado debe ser difente de 0")
    else:
        if num > 0:
            sumarpos = sumarpos + num
        else:
            produc_neg = produc_neg * num

print("La suma de los numeros positivos es:", sumarpos)
print("el producto de los numeros negativos es:", produc_neg)