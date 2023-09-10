'''
Realiza una función llamada recortar(numero, minimo, maximo) que reciba tres argumentos:

El primero es el número a recortar

El segundo es el límite inferior

El tercero el límite superior.

La función tendrá que cumplir lo siguiente:

Devolver el límite inferior si el número es menor que éste

Devolver el límite superior si el número es mayor que éste.

Devolver el número sin cambios si no se supera ningún límite.


'''

def recortar(numero,minimo,maximo):
    return_value  = numero

    if numero < minimo:
        return_value = minimo
    elif numero > maximo:
        return_value = maximo

    return return_value


print(recortar(-4,0,4))