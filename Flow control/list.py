'''
Pide al usuario que introduzca un número entero por teclado entre 1 y 9 (ambos incluidos) y guárdalo en la variable numero. Debes asegurarte de que esa variable numero contiene un numero entero del 1 al 9, utiliza un bucle para repetir la lectura hasta que se cumpla esa condición.

Genera una lista llamada multiplos que contenga los múltiplos de numero en el rango de 1 a 100 (ambos incluidos) utilizando la conversión de un range a list con un paso: list(range(Min,Max,Paso)).

'''

multiplos = []

numero = int(input("Introduzca un numero entre 1 y 9 "))

while(numero< 1 or numero > 9):
    numero = int(input("Introduzca un numero entre 1 y 9 "))
    

for value in range(1,101):
   
   if(value%numero ==0):
       multiplos.append(value) 
 
 
print(multiplos)   