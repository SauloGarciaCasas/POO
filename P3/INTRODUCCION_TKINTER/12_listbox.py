from tkinter import *

ventana=Tk()
ventana.title("ListBox")
ventana.geometry("500x500")

def mostrarValor():
    valor=lista.get(lista.curselection())
    lbl_seleccion.config(text=f"Seleccionaste: {valor}")

lista=Listbox(ventana, width=50, height=5, selectmode="single")
lista.pack()

opciones=["Azul", "Rojo", "Negro", "Amarillo"]
for i in opciones:
    lista.insert(END, i)

btn_mostrar=Button(ventana, text="Mostrar selección del usuario", command=mostrarValor)
btn_mostrar.pack()

lbl_seleccion=Label(ventana, text="")
lbl_seleccion.pack()

ventana.mainloop()