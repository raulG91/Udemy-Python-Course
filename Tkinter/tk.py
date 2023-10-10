from tkinter import *

#Create root 

root = Tk()

root.title("Hola Mundo")
root.iconbitmap('@Tkinter/hola.xbm')

#Create a frame and config dimensions
frame = Frame(root,width=480, height=320)

#Pack the frame
frame.pack()
#Anchor to north west and on the left side
#frame.pack(side="left",anchor="nw")
#frame.config(bg="lightblue")

label = Label(frame,text="Hola mundo")
#label.pack()
label.place(x=0,y=0)
label.config(bg="green")
label.config(fg="orange")
#Create main window
root.mainloop()

