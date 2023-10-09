num=int(input("INGRESE UN NUMERO MAYOR A 0: "))
contador=0

for i in range(2, num):
    print(i)
    if num % i == 0:
        contador+=1
        print("Es divisible por:", i)
if contador >= 1:
    print("Es divisible por 1 y",num)
    print(num,"NO ES UN NUMER PRIMO")
else:
    print("Es divisible solo por 1 y",num)
    print(num,"ES UN NUMERO PRIMO")