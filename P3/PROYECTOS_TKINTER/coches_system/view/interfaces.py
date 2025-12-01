from tkinter import *
from tkinter import ttk

class View:
    def __init__(self, ventana):
        self.ventana = ventana 
        ventana.title("Gestión de Vehículos")
        ventana.geometry("600x600")
        ventana.resizable(False, False)
        self.interfaz_principal(ventana) 

    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def interfaz_principal(ventana):
        View.borrarPantalla(ventana)
        
        lbl_titulo = Label(ventana, text=".:: Menú Principal ::.", justify="center", font=("Arial", 16, "bold"))
        lbl_titulo.pack(pady=30)

        btn_autos = Button(ventana, text="Gestión de Autos", command=lambda: View.menu_acciones(ventana, "Autos"), width=20, height=2, bg="#ddd")
        btn_autos.pack(pady=10)

        btn_camionetas = Button(ventana, text="Gestión de Camionetas", command=lambda: View.menu_acciones(ventana, "Camionetas"), width=20, height=2, bg="#ddd")
        btn_camionetas.pack(pady=10)

        btn_camiones = Button(ventana, text="Gestión de Camiones", command=lambda: View.menu_acciones(ventana, "Camiones"), width=20, height=2, bg="#ddd")
        btn_camiones.pack(pady=10)

        btn_salir = Button(ventana, text="Salir", command=ventana.quit, width=20, height=2, bg="#ffcccc")
        btn_salir.pack(pady=30)

    @staticmethod
    def menu_acciones(ventana, tipo_vehiculo):
        """
        Recibe 'tipo_vehiculo' para personalizar el título (Autos, Camiones, etc.)
        """
        View.borrarPantalla(ventana)
        
        lbl_titulo = Label(ventana, text=f".:: Menú de {tipo_vehiculo} ::.", justify="center", font=("Arial", 14, "bold"))
        lbl_titulo.pack(pady=20)

        btn_insertar = Button(ventana, text="Insertar Nuevo", command=lambda: View.insertar_autos(ventana, tipo_vehiculo), width=20, height=2)
        btn_insertar.pack(pady=10)

        btn_consultar = Button(ventana, text="Consultar Todos", command=lambda: View.consultar_autos(ventana, tipo_vehiculo), width=20, height=2)
        btn_consultar.pack(pady=10)

        btn_actualizar = Button(ventana, text="Actualizar Registro", command=lambda: View.cambiar_autos(ventana, tipo_vehiculo), width=20, height=2)
        btn_actualizar.pack(pady=10)

        btn_eliminar = Button(ventana, text="Eliminar Registro", command=lambda: View.borrar_autos(ventana, tipo_vehiculo), width=20, height=2)
        btn_eliminar.pack(pady=10)

        btn_regresar = Button(ventana, text="Regresar al Menú", command=lambda: View.interfaz_principal(ventana), width=20, height=2, fg="blue")
        btn_regresar.pack(pady=20)

    @staticmethod
    def insertar_autos(ventana, tipo_vehiculo):
        View.borrarPantalla(ventana)
        
        lbl_titulo = Label(ventana, text=f"Insertar: {tipo_vehiculo}", font=("Arial", 12, "bold"))
        lbl_titulo.pack(pady=10)

        frame_form = Frame(ventana)
        frame_form.pack(pady=10)

        Label(frame_form, text="Marca:").grid(row=0, column=0, padx=5, pady=5, sticky=E)
        Entry(frame_form, width=30).grid(row=0, column=1, padx=5, pady=5)

        Label(frame_form, text="Color:").grid(row=1, column=0, padx=5, pady=5, sticky=E)
        Entry(frame_form, width=30).grid(row=1, column=1, padx=5, pady=5)

        Label(frame_form, text="Modelo:").grid(row=2, column=0, padx=5, pady=5, sticky=E)
        Entry(frame_form, width=30).grid(row=2, column=1, padx=5, pady=5)

        Label(frame_form, text="Velocidad:").grid(row=3, column=0, padx=5, pady=5, sticky=E)
        Entry(frame_form, width=30).grid(row=3, column=1, padx=5, pady=5)

        Label(frame_form, text="Caballaje:").grid(row=4, column=0, padx=5, pady=5, sticky=E)
        Entry(frame_form, width=30).grid(row=4, column=1, padx=5, pady=5)

        Label(frame_form, text="Plazas:").grid(row=5, column=0, padx=5, pady=5, sticky=E)
        Entry(frame_form, width=30).grid(row=5, column=1, padx=5, pady=5)

        btn_guardar = Button(ventana, text="Guardar", bg="#ccffcc", width=15)
        btn_guardar.pack(pady=15)

        btn_volver = Button(ventana, text="Volver", width=15, command=lambda: View.menu_acciones(ventana, tipo_vehiculo))
        btn_volver.pack(pady=5)

    @staticmethod
    def consultar_autos(ventana, tipo_vehiculo):
        View.borrarPantalla(ventana)
        
        lbl_titulo = Label(ventana, text=f"Listado de: {tipo_vehiculo}", font=("Arial", 12, "bold"))
        lbl_titulo.pack(pady=10)

        frame_tabla = Frame(ventana)
        frame_tabla.pack(pady=10, padx=20, fill=BOTH, expand=True)

        tabla = ttk.Treeview(frame_tabla, columns=("ID", "Marca", "Color", "Modelo", "Velocidad"), show='headings')
        
        tabla.heading("ID", text="ID")
        tabla.heading("Marca", text="Marca")
        tabla.heading("Color", text="Color")
        tabla.heading("Modelo", text="Modelo")
        tabla.heading("Velocidad", text="Velocidad")
        
        tabla.column("ID", width=30)
        tabla.column("Marca", width=100)
        
        scrollbar = Scrollbar(frame_tabla, orient=VERTICAL, command=tabla.yview)
        tabla.configure(yscroll=scrollbar.set)
        
        tabla.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        btn_volver = Button(ventana, text="Volver", width=15, command=lambda: View.menu_acciones(ventana, tipo_vehiculo))
        btn_volver.pack(pady=20)

    @staticmethod
    def cambiar_autos(ventana, tipo_vehiculo):
        View.borrarPantalla(ventana)
        
        lbl_titulo = Label(ventana, text=f"Actualizar: {tipo_vehiculo}", font=("Arial", 12, "bold"))
        lbl_titulo.pack(pady=5)

        frame_buscar = Frame(ventana)
        frame_buscar.pack(pady=10)
        Label(frame_buscar, text="ID a modificar:").pack(side=LEFT, padx=5)
        Entry(frame_buscar, width=10).pack(side=LEFT, padx=5)
        Button(frame_buscar, text="Buscar", bg="#ffffcc").pack(side=LEFT, padx=5)

        frame_form = Frame(ventana)
        frame_form.pack(pady=10)

        Label(frame_form, text="Nueva Marca:").grid(row=0, column=0, sticky=E)
        Entry(frame_form).grid(row=0, column=1, pady=3)

        Label(frame_form, text="Nuevo Modelo:").grid(row=1, column=0, sticky=E)
        Entry(frame_form).grid(row=1, column=1, pady=3)

        Label(frame_form, text="Nuevo Color:").grid(row=2, column=0, sticky=E)
        Entry(frame_form).grid(row=2, column=1, pady=3)

        btn_actualizar = Button(ventana, text="Confirmar Cambios", bg="#ccffcc", width=20)
        btn_actualizar.pack(pady=15)

        btn_volver = Button(ventana, text="Volver", width=15, command=lambda: View.menu_acciones(ventana, tipo_vehiculo))
        btn_volver.pack(pady=5)

    @staticmethod
    def borrar_autos(ventana, tipo_vehiculo):
        View.borrarPantalla(ventana)
        
        lbl_titulo = Label(ventana, text=f"Eliminar: {tipo_vehiculo}", font=("Arial", 12, "bold"))
        lbl_titulo.pack(pady=20)

        Label(ventana, text="Ingrese el ID del registro a eliminar:", font=("Arial", 10)).pack(pady=5)
        
        txt_id = Entry(ventana, width=20)
        txt_id.pack(pady=5)

        btn_borrar = Button(ventana, text="Eliminar", bg="red", fg="white", width=25)
        btn_borrar.pack(pady=20)

        btn_volver = Button(ventana, text="Volver", width=15, command=lambda: View.menu_acciones(ventana, tipo_vehiculo))
        btn_volver.pack(pady=10)