from tkinter import *

def cambiarTexto():
    mensajeCambiante.config(
        text="Bienvenido"
    )
    mensajeCambiante2.config(
        text="Has iniciado sesión"
    )

def regresarTexto():
    mensajeCambiante.config(
        text="Nombre"
    )
    mensajeCambiante2.config(
        text="Contraseña"
    )

ventana=Tk()
ventana.title("Botones")
ventana.geometry("800x600")

frame_principal=Frame(ventana)
frame_principal.config(
    bg="#A7A7A7", 
    width=800,
    height=50,
    border=2,
    relief=GROOVE
)
frame_principal.pack_propagate(False)
frame_principal.pack(pady=10)
lbl_titulo=Label(frame_principal, text="Uso de botones")
lbl_titulo.config(
    bg="#A7A7A7",
    width=20,
)
lbl_titulo.pack(pady=10)

mensajeCambiante=Label(ventana, text="Nombre")
mensajeCambiante.pack()
mensajeCambiante2=Label(ventana, text="Contraseña")
mensajeCambiante2.pack()

boton_Cambiar=Button(ventana, text="Iniciar sesión", command=cambiarTexto)
boton_Cambiar.pack()

boton_Cambiar=Button(ventana, text="Cerrar", command=regresarTexto)
boton_Cambiar.pack()

ventana.mainloop()