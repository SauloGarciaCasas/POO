from tkinter import messagebox

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