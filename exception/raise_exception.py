def funcion(value=None):
    if value == None:
        raise ValueError("Param could not be None")
    
    return value
try:
    print(funcion(3))
except ValueError:
    print("Incorrect value")    