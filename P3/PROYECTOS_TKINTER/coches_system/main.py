from view import interfaces
from tkinter import *

class App:
    @staticmethod
    def main(ventana):
        view=interfaces.View(ventana)


if __name__=="__main__":
    ventana=Tk()
    App.main(ventana)
    ventana.mainloop()