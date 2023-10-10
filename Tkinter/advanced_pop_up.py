
from tkinter import *
from tkinter import filedialog as FileDialog

def test():
    fichero = FileDialog.askopenfilename(title="Abrir un fichero")
    print(fichero)
    
root = Tk()

Button(root, text = "Clícame", command=test).pack()

root.mainloop()