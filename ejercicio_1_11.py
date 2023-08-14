horas = int(input("Cantidad de Horas Trabajadas por dia: "))
pagaPorHora = int(input("¿Cuanto es la paga por hora trabajada?: "))
cantidadDeDias = int(input("¿Que cantidad de dias Trabajas al mes?: "))

sueldoDiario = horas * pagaPorHora

print("Su sueldo diario es de: $"+ str(sueldoDiario))

sueldoMensual = sueldoDiario * cantidadDeDias

print("Su sueldo mensual por "+ str(cantidadDeDias) + " dias es de $" + str(sueldoMensual))

