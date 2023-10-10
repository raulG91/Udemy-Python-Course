from tkinter import *

root = Tk()
'''
#Create a frame for each field
frame = Frame()
frame.pack()
entry = Entry(frame)
entry.pack(side="right")

label = Label(frame,text="Nombre")
label.pack(side="left")

frame2 = Frame()
frame2.pack()
entry2 = Entry(frame2)
entry2.pack(side="right")

label2 = Label(frame2,text="Apellidos")
label2.pack(side="left") '''

# Create using grid

label3 = Label(root,text="Nombre ")
label3.grid(row="0",column="0")

entry3 = Entry(root)
entry3.grid(row="0",column="1")

label4 = Label(root,text="Apellidos")
label4.grid(row="1",column="0")

entry4 = Entry(root)
entry4.grid(row="1",column="1")




#Set main loop
root.mainloop()
