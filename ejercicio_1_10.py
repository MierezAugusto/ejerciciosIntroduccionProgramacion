edad= int(input("Ingresa tu edad:"))

if edad < 0:
    print("Ingreso mal su edad")
elif edad >= 0 and edad < 18:
    print("Tu eres menor de edad")
else:
    print("Tu eres mayor de edad"); 