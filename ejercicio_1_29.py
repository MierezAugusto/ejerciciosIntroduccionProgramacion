cateto_a= float(input("Ingrese la longitud de primer cateto: "))
cateto_b= float(input("Ingrese la longitud de segundo cateto: "))

catsAlCuadrado = cateto_a **2 + cateto_b ** 2 

hipot = catsAlCuadrado ** 0.5

print("La hipotenusa del triangulo recto es: {:.2f}".format(hipot))