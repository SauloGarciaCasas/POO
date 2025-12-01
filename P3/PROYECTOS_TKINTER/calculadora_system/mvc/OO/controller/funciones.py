from tkinter import messagebox
from model import operaciones

class Operaciones:
    @staticmethod
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
            
            respuesta=messagebox.askquestion(title="Resultado", message=f"{texto}\n¿Deseas guardar en la base de datos?",icon="question")
            if respuesta=="yes":
                messagebox.showinfo(icon="info", title="Alerta", message="Registro insertado correctamente.")
                operaciones.Operaciones.insertar(numero1, numero2, op, resultado)
        except Exception as e:
            messagebox.showerror(title="Error", message=str(e))

    @staticmethod
    def consultar_operaciones_datos():
        try:
            return operaciones.Operaciones.consultar()
        except Exception as e:
            messagebox.showerror(title="Error", message=f"No se pudieron consultar los datos: {e}")
            return []

    @staticmethod
    def actualizar_operacion_form(id_op, numero1, numero2, signo):
        try:
            if id_op == 0 or signo not in ["+", "-", "*", "/"]:
                messagebox.showerror("Error", "ID no válido o Operador no válido (+, -, *, /)")
                return
            
            if signo == "+":
                resultado = numero1 + numero2
            elif signo == "-":
                resultado = numero1 - numero2
            elif signo == "*":
                resultado = numero1 * numero2
            elif signo == "/":
                if numero2 == 0:
                    messagebox.showerror(title="Error", message="División por cero")
                    return
                resultado = numero1 / numero2
            
            if operaciones.Operaciones.actualizar(numero1, numero2, signo, resultado, id_op):
                messagebox.showinfo("Alerta", "Registro actualizado correctamente.")
            else:
                messagebox.showerror("Error", "No se pudo actualizar el registro.")
        except Exception as e:
            messagebox.showerror(title="Error", message=f"Error al actualizar: {e}")

    @staticmethod
    def eliminar_operacion_form(id_op):
        try:
            if id_op == 0:
                messagebox.showerror("Error", "Por favor, introduce un ID válido.")
                return

            registro = operaciones.Operaciones.consultar_por_id(id_op)
            
            if not registro:
                messagebox.showerror("Error", f"El ID {id_op} no existe en la base de datos.")
                return

            respuesta = messagebox.askyesno("Confirmar", f"¿Estás seguro de que deseas eliminar el registro con ID {id_op}?")
            if respuesta:
                if operaciones.Operaciones.eliminar(id_op):
                    messagebox.showinfo("Éxito", "Registro eliminado correctamente.")
                else:
                    messagebox.showerror("Error", "No se pudo eliminar el registro (Error de BD).")
        except Exception as e:
            messagebox.showerror(title="Error", message=f"Error al eliminar: {e}")

    @staticmethod
    def buscar_operacion(id_op):
        try:
            if not isinstance(id_op, int) and not str(id_op).isdigit():
                return None
            return operaciones.Operaciones.consultar_por_id(id_op)
        except Exception as e:
            messagebox.showerror(title="Error", message=f"Error al buscar: {e}")
            return None