from tkinter import *

def select():
    monitor.config(text = "Opción {}".format(opcion.get() ) )

root = Tk()


opcion = IntVar() # Como StrinVar pero en entero agrupa los radiobuttons

Radiobutton(root, text="Opción 1", variable=opcion, 
            value=1,command=select).pack() # Cada radio button tiene un valor
Radiobutton(root, text="Opción 2", variable=opcion,
            value=2,command=select).pack()
Radiobutton(root, text="Opción 3", variable=opcion, 
            value=3,command=select).pack()  

monitor = Label(root)
monitor.pack()

root.mainloop()