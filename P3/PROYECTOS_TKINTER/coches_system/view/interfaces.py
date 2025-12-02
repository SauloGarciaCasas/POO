from tkinter import *
from tkinter import ttk 
from tkinter import messagebox

class View:
    def __init__(self, ventana):
        self.ventana = ventana 
        ventana.title("Gestión de Vehículos")
        ventana.geometry("700x700") 
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

        btn_autos = Button(ventana, text="Gestión de Autos", command=lambda: View.menu_acciones(ventana, "Autos"), width=25, height=2, bg="#ddd")
        btn_autos.pack(pady=10)

        btn_camionetas = Button(ventana, text="Gestión de Camionetas", command=lambda: View.menu_acciones(ventana, "Camionetas"), width=25, height=2, bg="#ddd")
        btn_camionetas.pack(pady=10)

        btn_camiones = Button(ventana, text="Gestión de Camiones", command=lambda: View.menu_acciones(ventana, "Camiones"), width=25, height=2, bg="#ddd")
        btn_camiones.pack(pady=10)

        btn_salir = Button(ventana, text="Salir", command=ventana.quit, width=25, height=2, bg="#ffcccc")
        btn_salir.pack(pady=30)

    @staticmethod
    def menu_acciones(ventana, tipo_vehiculo):
        View.borrarPantalla(ventana)
        
        lbl_titulo = Label(ventana, text=f".:: Menú de {tipo_vehiculo} ::.", justify="center", font=("Arial", 14, "bold"))
        lbl_titulo.pack(pady=20)

        if tipo_vehiculo == "Autos":
            cmd_insertar = lambda: View.insertar_autos(ventana)
            cmd_consultar = lambda: View.consultar_autos(ventana)
            cmd_actualizar = lambda: View.cambiar_autos(ventana)
            cmd_borrar = lambda: View.borrar_autos(ventana)
        
        elif tipo_vehiculo == "Camionetas":
            cmd_insertar = lambda: View.insertar_camionetas(ventana)
            cmd_consultar = lambda: View.consultar_camionetas(ventana)
            cmd_actualizar = lambda: View.cambiar_camionetas(ventana)
            cmd_borrar = lambda: View.borrar_camionetas(ventana)
            
        elif tipo_vehiculo == "Camiones":
            cmd_insertar = lambda: View.insertar_camiones(ventana)
            cmd_consultar = lambda: View.consultar_camiones(ventana)
            cmd_actualizar = lambda: View.cambiar_camiones(ventana)
            cmd_borrar = lambda: View.borrar_camiones(ventana)

        btn_insertar = Button(ventana, text="Insertar", command=cmd_insertar, width=20, height=2)
        btn_insertar.pack(pady=10)

        btn_consultar = Button(ventana, text="Consultar", command=cmd_consultar, width=20, height=2)
        btn_consultar.pack(pady=10)

        btn_actualizar = Button(ventana, text="Actualizar", command=cmd_actualizar, width=20, height=2)
        btn_actualizar.pack(pady=10)

        btn_eliminar = Button(ventana, text="Eliminar", command=cmd_borrar, width=20, height=2)
        btn_eliminar.pack(pady=10)

        btn_regresar = Button(ventana, text="Regresar al Menú", command=lambda: View.interfaz_principal(ventana), width=20, height=2, fg="blue")
        btn_regresar.pack(pady=20)

    @staticmethod
    def insertar_autos(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo = Label(ventana, text="Insertar: Autos", font=("Arial", 12, "bold"))
        lbl_titulo.pack(pady=10)

        frame_form = Frame(ventana)
        frame_form.pack(pady=10)

        campos = ["Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas"]
        
        for i, campo in enumerate(campos):
            Label(frame_form, text=f"{campo}:").grid(row=i, column=0, padx=5, pady=5, sticky=E)
            Entry(frame_form, width=30).grid(row=i, column=1, padx=5, pady=5)

        Button(ventana, text="Insertar", bg="#ccffcc", width=15).pack(pady=15)
        Button(ventana, text="Volver", width=15, command=lambda: View.menu_acciones(ventana, "Autos")).pack(pady=5)

    @staticmethod
    def consultar_autos(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo = Label(ventana, text="Listado de Autos", font=("Arial", 12, "bold"))
        lbl_titulo.pack(pady=10)

        frame_tabla = Frame(ventana)
        frame_tabla.pack(pady=10, padx=20, fill=BOTH, expand=True)

        cols = ("ID", "Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas")
        tabla = ttk.Treeview(frame_tabla, columns=cols, show='headings')
        for col in cols:
            tabla.heading(col, text=col)
            tabla.column(col, width=80)
        
        tabla.pack(side=LEFT, fill=BOTH, expand=True)
        Button(ventana, text="Volver", width=15, command=lambda: View.menu_acciones(ventana, "Autos")).pack(pady=10)

    @staticmethod
    def cambiar_autos(ventana):
        View.borrarPantalla(ventana)
        Label(ventana, text="Actualizar Auto", font=("Arial", 12, "bold")).pack(pady=10)
        
        frame_buscar = Frame(ventana)
        frame_buscar.pack(pady=5)
        Label(frame_buscar, text="ID Auto:").pack(side=LEFT, padx=5)
        ent_id = Entry(frame_buscar, width=10)
        ent_id.pack(side=LEFT, padx=5)

        frame_edicion = Frame(ventana)
        frame_edicion.pack(pady=10)

        def mostrar_formulario():
            for widget in frame_edicion.winfo_children():
                widget.destroy()
            
            if ent_id.get():
                campos = ["Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas"]
                for i, campo in enumerate(campos):
                    Label(frame_edicion, text=f"Nuevo {campo}:").grid(row=i, column=0, padx=5, pady=5, sticky=E)
                    Entry(frame_edicion, width=30).grid(row=i, column=1, padx=5, pady=5)
                
                Button(frame_edicion, text="Guardar", bg="#ccffcc").grid(row=len(campos), columnspan=2, pady=15)

        Button(frame_buscar, text="Buscar", command=mostrar_formulario).pack(side=LEFT, padx=5)

        Button(ventana, text="Volver", width=15, command=lambda: View.menu_acciones(ventana, "Autos")).pack(pady=20)

    @staticmethod
    def borrar_autos(ventana):
        View.borrarPantalla(ventana)
        Label(ventana, text="Eliminar Auto", font=("Arial", 12, "bold")).pack(pady=10)
        Label(ventana, text="ID:").pack()
        Entry(ventana).pack()
        Button(ventana, text="Eliminar", bg="red", fg="white").pack(pady=10)
        Button(ventana, text="Volver", width=15, command=lambda: View.menu_acciones(ventana, "Autos")).pack(pady=10)

    @staticmethod
    def insertar_camionetas(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo = Label(ventana, text="Insertar: Camioneta", font=("Arial", 12, "bold"))
        lbl_titulo.pack(pady=10)

        frame_form = Frame(ventana)
        frame_form.pack(pady=10)
        campos = ["Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas", "Tracción", "Cerrada (1/0)"]
        
        for i, campo in enumerate(campos):
            Label(frame_form, text=f"{campo}:").grid(row=i, column=0, padx=5, pady=5, sticky=E)
            Entry(frame_form, width=30).grid(row=i, column=1, padx=5, pady=5)

        Button(ventana, text="Insertar", bg="#ccffcc", width=20).pack(pady=15)
        Button(ventana, text="Volver", width=15, command=lambda: View.menu_acciones(ventana, "Camionetas")).pack(pady=5)

    @staticmethod
    def consultar_camionetas(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo = Label(ventana, text="Listado de Camionetas", font=("Arial", 12, "bold"))
        lbl_titulo.pack(pady=10)

        frame_tabla = Frame(ventana)
        frame_tabla.pack(pady=10, padx=20, fill=BOTH, expand=True)
        cols = ("ID", "Marca", "Modelo", "Plazas", "Tracción", "Cerrada")
        tabla = ttk.Treeview(frame_tabla, columns=cols, show='headings')
        for col in cols:
            tabla.heading(col, text=col)
            tabla.column(col, width=90)
        
        scrollbar = Scrollbar(frame_tabla, orient=VERTICAL, command=tabla.yview)
        tabla.configure(yscroll=scrollbar.set)
        tabla.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        Button(ventana, text="Volver", width=15, command=lambda: View.menu_acciones(ventana, "Camionetas")).pack(pady=20)

    @staticmethod
    def cambiar_camionetas(ventana):
        View.borrarPantalla(ventana)
        Label(ventana, text="Actualizar Camioneta", font=("Arial", 12, "bold")).pack(pady=10)
        
        frame_buscar = Frame(ventana)
        frame_buscar.pack(pady=5)
        Label(frame_buscar, text="ID Camioneta:").pack(side=LEFT, padx=5)
        ent_id = Entry(frame_buscar, width=10)
        ent_id.pack(side=LEFT, padx=5)
        
        frame_edicion = Frame(ventana)
        frame_edicion.pack(pady=10)

        def mostrar_formulario():
            for widget in frame_edicion.winfo_children():
                widget.destroy()
            
            if ent_id.get():
                campos = ["Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas", "Tracción", "Cerrada"]
                for i, campo in enumerate(campos):
                    Label(frame_edicion, text=f"Nuevo {campo}:").grid(row=i, column=0, padx=5, pady=5, sticky=E)
                    Entry(frame_edicion, width=30).grid(row=i, column=1, padx=5, pady=5)
                
                Button(frame_edicion, text="Guardar", bg="#ccffcc").grid(row=len(campos), columnspan=2, pady=15)

        Button(frame_buscar, text="Buscar", command=mostrar_formulario).pack(side=LEFT, padx=5)
        Button(ventana, text="Volver", width=15, command=lambda: View.menu_acciones(ventana, "Camionetas")).pack(pady=20)

    @staticmethod
    def borrar_camionetas(ventana):
        View.borrarPantalla(ventana)
        Label(ventana, text="Eliminar Camioneta", font=("Arial", 12, "bold")).pack(pady=20)
        Label(ventana, text="Ingrese ID:").pack()
        Entry(ventana, width=20).pack(pady=5)
        Button(ventana, text="Eliminar", bg="red", fg="white", width=15).pack(pady=10)
        Button(ventana, text="Volver", width=15, command=lambda: View.menu_acciones(ventana, "Camionetas")).pack(pady=10)


    @staticmethod
    def insertar_camiones(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo = Label(ventana, text="Insertar: Camión", font=("Arial", 12, "bold"))
        lbl_titulo.pack(pady=10)

        frame_form = Frame(ventana)
        frame_form.pack(pady=10)
        campos = ["Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas", "Ejes", "Capacidad Carga"]
        
        for i, campo in enumerate(campos):
            Label(frame_form, text=f"{campo}:").grid(row=i, column=0, padx=5, pady=5, sticky=E)
            Entry(frame_form, width=30).grid(row=i, column=1, padx=5, pady=5)

        Button(ventana, text="Insertar", bg="#ccffcc", width=20).pack(pady=15)
        Button(ventana, text="Volver", width=15, command=lambda: View.menu_acciones(ventana, "Camiones")).pack(pady=5)

    @staticmethod
    def consultar_camiones(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo = Label(ventana, text="Listado de Camiones", font=("Arial", 12, "bold"))
        lbl_titulo.pack(pady=10)

        frame_tabla = Frame(ventana)
        frame_tabla.pack(pady=10, padx=20, fill=BOTH, expand=True)
        cols = ("ID", "Marca", "Modelo", "Plazas", "Ejes", "Carga")
        tabla = ttk.Treeview(frame_tabla, columns=cols, show='headings')
        for col in cols:
            tabla.heading(col, text=col)
            tabla.column(col, width=90)
        
        scrollbar = Scrollbar(frame_tabla, orient=VERTICAL, command=tabla.yview)
        tabla.configure(yscroll=scrollbar.set)
        tabla.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        Button(ventana, text="Volver", width=15, command=lambda: View.menu_acciones(ventana, "Camiones")).pack(pady=20)

    @staticmethod
    def cambiar_camiones(ventana):
        View.borrarPantalla(ventana)
        Label(ventana, text="Actualizar Camión", font=("Arial", 12, "bold")).pack(pady=10)
        
        frame_buscar = Frame(ventana)
        frame_buscar.pack(pady=5)
        Label(frame_buscar, text="ID Camión:").pack(side=LEFT, padx=5)
        ent_id = Entry(frame_buscar, width=10)
        ent_id.pack(side=LEFT, padx=5)
        
        frame_edicion = Frame(ventana)
        frame_edicion.pack(pady=10)

        def mostrar_formulario():
            for widget in frame_edicion.winfo_children():
                widget.destroy()
            
            if ent_id.get():
                campos = ["Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas", "Ejes", "Capacidad"]
                for i, campo in enumerate(campos):
                    Label(frame_edicion, text=f"Nuevo {campo}:").grid(row=i, column=0, padx=5, pady=5, sticky=E)
                    Entry(frame_edicion, width=30).grid(row=i, column=1, padx=5, pady=5)
                
                Button(frame_edicion, text="Guardar", bg="#ccffcc").grid(row=len(campos), columnspan=2, pady=15)

        Button(frame_buscar, text="Buscar", command=mostrar_formulario).pack(side=LEFT, padx=5)
        Button(ventana, text="Volver", width=15, command=lambda: View.menu_acciones(ventana, "Camiones")).pack(pady=20)

    @staticmethod
    def borrar_camiones(ventana):
        View.borrarPantalla(ventana)
        Label(ventana, text="Eliminar Camión", font=("Arial", 12, "bold")).pack(pady=20)
        Label(ventana, text="Ingrese ID:").pack()
        Entry(ventana, width=20).pack(pady=5)
        Button(ventana, text="Eliminar", bg="red", fg="white", width=15).pack(pady=10)
        Button(ventana, text="Volver", width=15, command=lambda: View.menu_acciones(ventana, "Camiones")).pack(pady=10)