from tkinter import *

ventana=Tk()
ventana.title("Uso del Frame o Marcos")
ventana.geometry("1920x1080")

#Marcos o Frames
marco=Frame(ventana, width=1280, height=720, bg="silver", border=2, relief=SOLID)
marco.pack_propagate(False)
marco.pack(pady=50)

marco2=Frame(marco,  width=640, height=480, bg="red", border=4, relief=GROOVE).pack(padx=50, pady=100)

ventana.mainloop()