num_1 = int(input("Ingrese el primer numero: "))
num_2 = int(input("Ingrese el segundo numero: "))

if num_1 % 3 == 0:
    num1= str(num_1) +" es divisible"
else:
    num1 = str(num_1) +" no es divisible"

if num_2 % 3 == 0:
    num2= str(num_2) + " es divisible"
else:
    num2 = str(num_2) +" no es divisible"
    
print(num1 + " y " + num2 +" por 3")