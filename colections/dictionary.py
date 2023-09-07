
'''
El siguiente ejercicio te servirá para practicar la manipulación de diccionarios.

Debes realizar las siguientes instrucciones de forma ordenada sobre la variable animales para que el ejercicio valide correctamente:

Añade al diccionario las claves perro, gato y rana con sus respectivos valores dog, cat y frog.

Modifica las claves caballo y vaca con los valores horse y cow respectivamente.

Por último elimina del diccionario las claves rana y vaca.
'''
# Variables del ejercicio (no modifiques esta línea)
animales = {"caballo":"", "vaca":""}

# completa el ejercicio
animales["perro"]="dog"
animales["gato"]="cat"
animales["rana"] = "fog"

animales["caballo"] = "horse"
animales["vaca"] = "cow"

del(animales["rana"])
del(animales["vaca"])
