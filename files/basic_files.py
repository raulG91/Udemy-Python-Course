from io import open

text = "This is a new line \n"

file = open("files/file.txt","w")
file.write(text)
file.write(text)
file.close()  

file2 = open("files/file.txt","r")

lines = file2.readlines()

print(lines[0])

with open("files/file.txt","r") as f:
    for linea in f:
        print(linea)