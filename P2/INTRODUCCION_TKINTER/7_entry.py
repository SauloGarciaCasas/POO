from tkinter import *

def entrar():
    lbl_resultado.config(
        text="Bienvenido"
    )

def borrar():
    lbl_resultado.config(
        text=""
    )

ventana=Tk()
ventana.title("Entry")
ventana.geometry("500x500")

lbl_titulo=Label(ventana, text="Acceso al sistema")
lbl_titulo.config(
    bg="#84F0F0",
    fg="#04003A",
    width=50,
    height=4,
    font=("Helvetica", 30, "italic"),
    relief=GROOVE
)
lbl_titulo.pack(pady=40)

lbl_nombre=Label(ventana, text="Ingrese el nombre: ")
lbl_nombre.pack(pady=5)
lbl_pass=Label(ventana, text="Ingrese la contraseña: ")
lbl_pass.pack(pady=5)

txt_nombre=Entry(ventana)
txt_nombre.pack()
txt_pass=Entry(ventana, show="*")
txt_pass.pack()


boton_entrar=Button(ventana, text="Entrar", command=entrar)
boton_entrar.pack()

boton_borrar=Button(ventana, text="Borrar", command=borrar)
boton_borrar.pack(pady=5)

lbl_resultado=Label(ventana, text="")
lbl_resultado.pack(pady=5)

ventana.mainloop()