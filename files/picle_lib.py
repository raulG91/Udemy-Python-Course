import pickle

lista = [1,2,3,4,5]

fichero = open("files/lista.pckl","wb")

#Move list into the file

pickle.dump(lista,fichero)

fichero.close()
#Open the file in mode read binary
fichero = open("files/lista.pckl","rb")

lista2 = pickle.load(fichero)

print(lista2)