'''Realiza un programa que lea un número por teclado y lo almacene en una variable llamada numero.

Si ese número introducido por teclado no es múltiple de 5 debe repetirse de nuevo la lectura hasta que lo sea.

Notas:

Debes asegurarte de que la variable numero es un número entero introducido con la instrucción input.

Si intentas asignar un múltiple de 5 manualmente a la variable numero la solución fallará.'''



while True:
    numero = int(input("Intorduzca un numero "))
    if(numero%5==0):
        print("Se ha introducido un numero multiplo de 5")
        break
    