nombre = input("Introduce el nombre ")

apellido = input("Introduce apellido ")

edad = int(input("Introduce la eddad "))

numero_magico = float(input("Introduce numero magico"))

cadena_final = nombre + " " +apellido + ": Tu número de la suerte es el "+ str((edad * numero_magico))

print(cadena_final)