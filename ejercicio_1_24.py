num1 = float(input("Ingrese primer nummero: "))
num2 = float(input("Ingrese segundo nummero: "))
num3 = float(input("Ingrese tercer nummero: "))

print(f"{num1} - {num2} - {num3}")

if num1 < num2 < num3:
    print("Estan ordenados de menor a mayor")
else:
    print("No estan ordenados de menor a mayor")