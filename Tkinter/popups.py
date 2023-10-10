from tkinter import *
from tkinter import messagebox as MessageBox

def test():
   # MessageBox.showinfo("Hola!", "Hola mundo") # título, mensaje
   #MessageBox.showwarning("Alerta", "No autorizado") 
   MessageBox.showerror("Error", "Ha ocurrido un error") 

root = Tk()

Button(root, text = "Clícame", command=test).pack()

root.mainloop()