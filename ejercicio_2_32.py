encuesta="Usted debe encuestar un total de 40 personas detallando sexo, edad y altura de cada una de ellas"

print(encuesta)

mujermayores=0
varonmenor=0
mayorAltura=0


for i in range(40):
    sexo=input("Ingrese sexo del escuestado: ")
    edad=int(input("Ingrese la edad del encuestado: "))
    altura=int(input("ingrese la Altura en cm del encuestado: "))
    print("-------------------------------------------------------------------")
    if sexo == "mujer" and edad > 25:
        mujermayores += 1
    elif sexo == "hombre" and edad < 18:
        varonmenor+=1
    elif sexo == "hombre" and altura > 170:
        mayorAltura+=1

porcmujeres= mujermayores / 40 * 100
porcVaronAlt= mayorAltura / 40 * 100

print("El porcentaje de mujeres mayores de 25 años es:", porcmujeres)
print("La cantidad de varones menor a 18 es:",varonmenor)
print("El porcentaje de hombres mayores de 18 años cuya altura supera 170cm es:", porcVaronAlt)
