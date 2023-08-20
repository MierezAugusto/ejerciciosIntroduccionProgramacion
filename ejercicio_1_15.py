num_1 = int(input("Ingrese el primer numero: "))
num_2 = int(input("Ingrese el segundo numero: "))

if num_1 % 3 == 0  and num_2 % 3 == 0 :
    print(f"{num_1} y {num_2} son  divisible por 3")
elif num_1 % 3 == 0:
    print(f"{num_1} es divisible por 3 y {num_2} no es divisible por 3" )
elif num_2 % 3 == 0:
    print(f"{num_1} no es divisible por 3 y {num_2} es divisible por 3" )
else:
    print(f"{num_1}  y {num_2} no son divisible por 3" )