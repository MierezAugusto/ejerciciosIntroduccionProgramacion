num1= int(input("INGRESE UN NUMERO DE INICIO: "))
num2= int(input("INGRESE UN NUMERO DEL FINAL: "))
num_i=0
suma=0
if num1 == num2 or num1 > num2:
    print("EL NUMERO DE INICIO DEBE SER MENOR AL NUMERO DEL FINAL")
else:
    for i in range(num2-num1+1):
        num_i= num1 + i
        suma += num_i
        

print(suma)