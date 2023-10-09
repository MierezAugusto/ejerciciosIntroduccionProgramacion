cantidad_A=0

while cantidad_A !=10:
    print("Debe ingresar caracteres, al ingresar 10 letras A/a finaliza el programa ")
    caracter=input("Ingrese un caracter aqui: ")
    if caracter == "a" or caracter == "A":
        cantidad_A+=1
        print("Cantidad de A ingresadas:",cantidad_A)
    else:
        print("-----NO ES LA LETRA A-----")

print("PROGRAMA FINALIZADO")