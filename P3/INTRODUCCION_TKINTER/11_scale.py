from tkinter import *

ventana=Tk()
ventana.title("Scale")
ventana.geometry("500x500")

def mostrarValor():
    lbl_valor.config(text=f"Valor seleccionado por el usuario: {valor.get()}")

valor=IntVar()
escala=Scale(ventana, from_=0, to=100, orient="horizontal", variable=valor)
escala.pack()

btn_mostrar=Button(ventana, text="Mostrar Valor", command=mostrarValor)
btn_mostrar.pack()

lbl_valor=Label(ventana, text="")
lbl_valor.pack()

ventana.mainloop()