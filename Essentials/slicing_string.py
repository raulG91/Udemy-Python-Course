'''
 Al parecer contiene el nombre de un alumno, la nota de un exámen y la materia. Realiza lo siguiente:
Voltea la cadena y guárdala en una variable llamada cadena_volteada. Puedes devolver una cadena volteada usando un tercer índice negativo con slicing tal que así: cadena[::-1]

Extrae el nombre y apellido del alumno y almacénalos en una variable llamada nombre.

Extrae la nota y almacénala en una variable llamada nota.

Extrae la materia y almacénala en una variable llamada materia.

Genera exactamente la siguiente estructura formateando las anteriores variables en una cadena llamada cadena_formateada donde nombre, nota y materia hacen referencia a las variables extraídas:

{nombre} ha sacado un {nota} en {materia}
Ejemplo:

Ramón García ha sacado un 8.1 en Matemáticas
Notas y consejos:

Todas las variables del enunciado deben existir y contener el valor correcto para pasar las pruebas.

Utiliza slicing para extraer las porciones de la cadena que te interesan.

Crea tantas variables como necesites para hacerlo más sencillo.
'''

# Variables del ejercicio (no las modifiques)
cadena_corrupta = "airotsiH,6.7,aícraG nómaR"

# Completa el ejercicio
#Transform the string
cadena_volteada = cadena_corrupta[::-1]
print(cadena_volteada)
#Extract name using Slice
nombre = cadena_volteada[:12]
nota = cadena_volteada[13:16]
asignatura = cadena_volteada[17:]
cadena_formateada = nombre + " ha sacado un "+nota +" en "+ asignatura
print(cadena_formateada)



