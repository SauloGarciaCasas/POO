from tkinter import *

ventana=Tk()
ventana.title("Menú")
ventana.geometry("500x500")

def mensaje(tipo):
    resultado.config(text=f"{tipo}")

menuBar = Menu(ventana)
ventana.config(menu=menuBar)

archivoMenu = Menu(menuBar , tearoff=1)
menuBar.add_cascade(label="Archivo" , menu=archivoMenu)
archivoMenu.add_command(label="Nuevo Archivo",command=lambda: mensaje("Nuevo Archivo"))
archivoMenu.add_command(label="Guardar Archivo",command=lambda: mensaje("Guardar Archivo"))
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir",command=ventana.quit)

archivoEdicion = Menu(menuBar , tearoff=1)
menuBar.add_cascade(label="Edicion" , menu=archivoEdicion)
archivoEdicion.add_command(label="Copiar",command=lambda: mensaje("Copiar"))
archivoEdicion.add_command(label="Recortar",command=lambda: mensaje("Recortar"))
archivoEdicion.add_separator()
archivoEdicion.add_command(label="Salir",command=ventana.quit)

resultado=Label(ventana, text="")
resultado.pack()

ventana.mainloop()