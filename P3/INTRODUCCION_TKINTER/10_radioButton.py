from tkinter import *

def mostrarSeleccion():
    lbl_seleccion.config(text=f"Opción seleccionada: {opcion.get()}")

ventana=Tk()
ventana.title("RadioButton")
ventana.geometry("500x500")

opcion=StringVar()
opcion1=Radiobutton(ventana, text="Opción 1", variable=opcion, value="opcion1")
opcion1.pack()
opcion2=Radiobutton(ventana, text="Opción 2", variable=opcion, value="opcion2")
opcion2.pack()
opcion3=Radiobutton(ventana, text="Opción 3", variable=opcion, value="opcion3")
opcion3.pack()

btn_mostrar=Button(ventana, text="Mostrar Selección", command=mostrarSeleccion)
btn_mostrar.pack()

lbl_seleccion=Label(ventana, text="")
lbl_seleccion.pack()

ventana.mainloop()