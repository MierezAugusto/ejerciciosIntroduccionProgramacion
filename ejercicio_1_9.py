fruta = input("Ingrese una fruta:")
cantidadDeFrutas = int(input("ingrese una cantidad de "+ fruta+":"))
frutasPorChico = cantidadDeFrutas // 3
if frutasPorChico > 1:
    fruta= fruta+"s"

print("Cada chico recibira "+ str(frutasPorChico)+" "+ fruta)
