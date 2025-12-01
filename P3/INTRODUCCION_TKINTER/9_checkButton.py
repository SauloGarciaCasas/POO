from tkinter import *

def mostrarEstado():
    if opcion.get() == 1:
        lbl_notif.config(text=f"Notificaciones Activadas")
    else:
        lbl_notif.config(text=f"Notificaciones Desactivadas")

ventana=Tk()
ventana.title("CheckButton")
ventana.geometry("500x500")

opcion=IntVar()
checkboton=Checkbutton(ventana, text="Deseas recibir notificaciones?", variable=opcion, onvalue=1, offvalue=0)
checkboton.pack()

btn_confirmar=Button(ventana, text="Confirmar", command=mostrarEstado)
btn_confirmar.pack()

lbl_notif=Label(ventana, text="")
lbl_notif.pack()

ventana.mainloop()