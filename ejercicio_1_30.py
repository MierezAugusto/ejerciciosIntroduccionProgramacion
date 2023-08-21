tarifa = float(input("Ingrese tarifa salarial por hora: "))
horas = float(input("ingrese cantidad de horas trabajadas: "))

salario = horas * tarifa

incremento = salario * 50 / 100

if horas <= 40:
    print(f"Salario por horas trabajadas es: {salario}")
else:
    print(f"Salario por horas trabajadas es: {salario + incremento}")