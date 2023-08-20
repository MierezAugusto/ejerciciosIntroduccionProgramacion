corredor1 = float(input("Ingrese el tiempo del primer corredor: "))
corredor2 = float(input("Ingrese el tiempo del segundo corredor: "))

tiempos_corredores= [corredor1, corredor2]

tiempos_corredores.sort()

corredor_ganador= tiempos_corredores[0]

print(f"El ganador es el corredor con un tiempo de {corredor_ganador} ")