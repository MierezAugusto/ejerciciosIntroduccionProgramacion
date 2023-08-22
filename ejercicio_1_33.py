tarifa = float(input("Ingrese tarifa salarial por hora: "))
nombre= input("Apellido y nombre: ")
antiguedad = int(input("Ingresar antigüedad laboral: "))
horas = float(input("ingrese cantidad de horas trabajadas: "))
salarioBruto = horas * tarifa
incremento = 30 * antiguedad
subTotal = salarioBruto + incremento 
descuentos = subTotal * 0.13
salarioNeto = subTotal - descuentos

print("\nApellido y nombre:",nombre,"\nAntigüedad laboral:",antiguedad,"\nRemuneracion por hora:",tarifa,"\nSueldo Bruto:",subTotal,"\nDescuento 13%: ",descuentos,"\nSueldo Neto: ",salarioNeto)  