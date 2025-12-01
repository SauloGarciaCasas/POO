from tkinter import *

def cambiarTexto():
    lbl_titulo.config(
        text="Bienvenidos a tkinter",
        bg="#FF0000",
        fg="#04003A",
        width=50,
        height=4,
        font=("Times New Roman", 30, "bold"),
        relief=GROOVE
    )

def regresarTexto():
    lbl_titulo.config(
        text="Bienvenidos a tkinter",
        bg="#84F0F0",
        fg="#04003A",
        width=50,
        height=4,
        font=("Helvetica", 30, "italic"),
        relief=GROOVE
    )

ventana=Tk()
ventana.title("Pesonalización")
ventana.geometry("500x500")

lbl_titulo=Label(ventana, text="Bienvenidos a tkinter")
lbl_titulo.config(
    bg="#84F0F0",
    fg="#04003A",
    width=50,
    height=4,
    font=("Helvetica", 30, "italic"),
    relief=GROOVE
)
lbl_titulo.pack(pady=40)

boton_Cambiar=Button(ventana, text="Haz click aquí", command=cambiarTexto)
boton_Cambiar.config(
    fg="white",
    activeforeground="yellow",
    width=15,
    font=("Arial", 20, "bold")
)
boton_Cambiar.pack()

boton_regresar=Button(ventana, text="Regresa click aquí", command=regresarTexto)
boton_regresar.config(
    fg="black",
    activeforeground="red",
    width=15,
    font=("Arial", 20, "bold")
)
boton_regresar.pack(pady=5)

ventana.mainloop()