from tkinter import *
from controller import funciones

def interfaz_principal():
    ventana=Tk()
    ventana.title("Calculadora")
    ventana.geometry("600x400")
    ventana.resizable(False,False)

    n1=IntVar()
    n2=IntVar()
    numero1=Entry(ventana, textvariable=n1, width=10, justify="center")
    numero1.pack(side="top", anchor="center")
    numero2=Entry(ventana, textvariable=n2, width=10, justify="center")
    numero2.pack(side="top", anchor="center")

    suma=Button(ventana, text="+", command=lambda: funciones.caja("+", n1.get(), n2.get()), width=5)
    suma.pack()

    resta=Button(ventana, text="-", command=lambda: funciones.caja("-", n1.get(), n2.get()), width=5)
    resta.pack()

    mult=Button(ventana, text="*", command=lambda: funciones.caja("*", n1.get(), n2.get()), width=5)
    mult.pack()

    div=Button(ventana, text="/", command=lambda: funciones.caja("/", n1.get(), n2.get()), width=5)
    div.pack()

    salir=Button(ventana, text="Salir", command=ventana.quit)
    salir.pack()

    ventana.mainloop()