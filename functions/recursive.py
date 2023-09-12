def sumatorio(numero):
    if numero == 0:
        return numero
    else:    
        return numero+sumatorio(numero -1)


print(sumatorio(5))