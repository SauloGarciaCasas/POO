"""
Tkinter trabaja a través de interfaces, es una biblioteca de Python que
permite crear aplicaciones en Python para escritorio
"""
import tkinter as tk

ventana = tk.Tk()
ventana.title("Ventana de Prueba con Tkinter")
ventana.geometry("1280x720")
ventana.resizable(True, True) #Método para redimensionar el tamaño de la ventana
ventana.mainloop() #Metodo que permite tener la ventana abierta e interactuar con ella
