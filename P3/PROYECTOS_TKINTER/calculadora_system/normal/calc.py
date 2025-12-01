"""
Crear una calculadora:
1.- Dos campos de texto
2.- 4 botones para las Operaciones
3.- Mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox

ventana=Tk()
ventana.title("Calculadora")
ventana.geometry("600x400")
ventana.resizable(False,False)

def caja(op, numero1, numero2):
    try:
        if op == "+":
            resultado = numero1 + numero2
            texto = f"{numero1} + {numero2} = {resultado}"
        elif op == "-":
            resultado = numero1 - numero2
            texto = f"{numero1} - {numero2} = {resultado}"
        elif op == "*":
            resultado = numero1 * numero2
            texto = f"{numero1} x {numero2} = {resultado}"
        elif op == "/":
            if numero2 == 0:
                messagebox.showerror(title="Error", message="División por cero")
                return
            resultado = numero1 / numero2
            texto = f"{numero1} / {numero2} = {resultado}"
        else:
            return
        messagebox.showinfo(title="Resultado", message=texto)
    except Exception as e:
        messagebox.showerror(title="Error", message=str(e))


n1=IntVar()
n2=IntVar()
numero1=Entry(ventana, textvariable=n1, width=10, justify="center")
numero1.pack(side="top", anchor="center")
numero2=Entry(ventana, textvariable=n2, width=10, justify="center")
numero2.pack(side="top", anchor="center")

suma=Button(ventana, text="+", command=lambda: caja("+", n1.get(), n2.get()), width=5)
suma.pack()

resta=Button(ventana, text="-", command=lambda: caja("-", n1.get(), n2.get()), width=5)
resta.pack()

mult=Button(ventana, text="*", command=lambda: caja("*", n1.get(), n2.get()), width=5)
mult.pack()

div=Button(ventana, text="/", command=lambda: caja("/", n1.get(), n2.get()), width=5)
div.pack()

salir=Button(ventana, text="Salir", command=ventana.quit)
salir.pack()

ventana.mainloop()