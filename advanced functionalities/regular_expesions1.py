import re

text = "En este texto se encuentra una palabra magica"

found = re.search("magica",text)

if found is not None:
     print("Se ha encontrado la palaabra")
else:
    print("No se ha encontrado")     
    
#Modify a text using a pattern    
text2 = "Hola amigo"
print(re.sub("amigo","amiga",text2))


#Find all occurrences of pattern in string
text3 = "Hello Hola Hola Hola"
print(re.findall("Hola",text3))    