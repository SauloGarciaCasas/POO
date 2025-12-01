from tkinter import *
from tkinter import ttk, messagebox
from controller import funciones

class Vista:
    def __init__(self, ventana):
        self.ventana = ventana
        ventana.title("Calculadora Básica")
        ventana.geometry("800x500")
        ventana.resizable(False, False)

        self.crear_menu()

        self.frame_calculadora = Frame(self.ventana)
        self.frame_consultar = Frame(self.ventana)
        self.frame_cambiar = Frame(self.ventana)
        self.frame_borrar = Frame(self.ventana)

        self.crear_vista_calculadora(self.frame_calculadora)
        self.crear_vista_consultar(self.frame_consultar)
        self.crear_vista_borrar(self.frame_borrar)
        self.crear_vista_cambiar(self.frame_cambiar)

        self.mostrar_vista_calculadora()

    def crear_menu(self):
        menu_bar = Menu(self.ventana)
        self.ventana.config(menu=menu_bar)

        menu_operaciones = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Operaciones", menu=menu_operaciones)

        menu_operaciones.add_command(label="Agregar", command=self.mostrar_vista_calculadora)
        menu_operaciones.add_command(label="Consultar", command=self.mostrar_vista_consultar)
        menu_operaciones.add_command(label="Cambiar", command=self.mostrar_vista_cambiar)
        menu_operaciones.add_command(label="Borrar", command=self.mostrar_vista_borrar)
        menu_operaciones.add_separator()
        menu_operaciones.add_command(label="Salir", command=self.ventana.quit)
    
    def ocultar_vistas(self):
        self.frame_calculadora.pack_forget()
        self.frame_consultar.pack_forget()
        self.frame_cambiar.pack_forget()
        self.frame_borrar.pack_forget()

    def mostrar_vista_calculadora(self):
        self.ocultar_vistas()
        self.frame_calculadora.pack(fill="both", expand=True)
        self.ventana.title("Calculadora Básica - Agregar")

    def mostrar_vista_consultar(self):
        self.ocultar_vistas()
        
        for item in self.tree_consulta.get_children():
            self.tree_consulta.delete(item)
        
        datos = funciones.Operaciones.consultar_operaciones_datos()
        if datos:
            for fila in datos:
                self.tree_consulta.insert("", "end", values=fila)
        
        self.frame_consultar.pack(fill="both", expand=True)
        self.ventana.title("Calculadora Básica - Consultar")

    def mostrar_vista_cambiar(self):
        self.ocultar_vistas()
        self.frame_cambiar.pack(fill="both", expand=True)
        self.ventana.title("Calculadora Básica - Cambiar")

    def mostrar_vista_borrar(self):
        self.ocultar_vistas()
        self.frame_borrar.pack(fill="both", expand=True)
        self.ventana.title("Calculadora Básica - Borrar")

    def crear_vista_calculadora(self, frame):
        Label(frame, text="Calculadora Básica", font=("Arial", 14)).pack(pady=10)
        
        self.n1_calc = IntVar()
        self.n2_calc = IntVar()
        
        Label(frame, text="Número 1:").pack()
        Entry(frame, textvariable=self.n1_calc, width=10, justify="center").pack()
        
        Label(frame, text="Número 2:").pack()
        Entry(frame, textvariable=self.n2_calc, width=10, justify="center").pack(pady=5)

        btn_frame = Frame(frame)
        btn_frame.pack(pady=10)
        
        Button(btn_frame, text="+", command=lambda: funciones.Operaciones.caja("+", self.n1_calc.get(), self.n2_calc.get()), width=5).grid(row=0, column=0, padx=5)
        Button(btn_frame, text="-", command=lambda: funciones.Operaciones.caja("-", self.n1_calc.get(), self.n2_calc.get()), width=5).grid(row=0, column=1, padx=5)
        Button(btn_frame, text="*", command=lambda: funciones.Operaciones.caja("*", self.n1_calc.get(), self.n2_calc.get()), width=5).grid(row=1, column=0, padx=5, pady=5)
        Button(btn_frame, text="/", command=lambda: funciones.Operaciones.caja("/", self.n1_calc.get(), self.n2_calc.get()), width=5).grid(row=1, column=1, padx=5, pady=5)

    def crear_vista_borrar(self, frame):
        Label(frame, text="..:: Borrar una Operación ::..", font=("Arial", 14)).pack(pady=20)
        
        Label(frame, text="ID de la Operación:").pack(pady=5)
        
        self.id_borrar_entry = IntVar()
        Entry(frame, textvariable=self.id_borrar_entry, width=20, justify="center").pack(pady=5)
        
        Button(frame, text="Eliminar", width=10, command=lambda: funciones.Operaciones.eliminar_operacion_form(self.id_borrar_entry.get())).pack(pady=10)
        
        Button(frame, text="Volver", width=10, command=self.mostrar_vista_calculadora).pack(pady=5)

    def crear_vista_consultar(self, frame):
        Label(frame, text="..:: Consultar Operaciones ::..", font=("Arial", 14)).pack(pady=10)

        tree_frame = Frame(frame)
        tree_frame.pack(fill="x", padx=10, pady=5)
        
        self.tree_consulta = ttk.Treeview(tree_frame, columns=("ID", "Fecha", "Num1", "Num2", "Op", "Res"), show="headings")
        self.tree_consulta.heading("ID", text="ID")
        self.tree_consulta.heading("Fecha", text="Fecha")
        self.tree_consulta.heading("Num1", text="Número 1")
        self.tree_consulta.heading("Num2", text="Número 2")
        self.tree_consulta.heading("Op", text="Operación")
        self.tree_consulta.heading("Res", text="Resultado")

        scrollbarx = ttk.Scrollbar(tree_frame, orient="horizontal", command=self.tree_consulta.xview)
        self.tree_consulta.configure(xscrollcommand=scrollbarx.set)
        scrollbary = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree_consulta.yview)
        self.tree_consulta.configure(yscrollcommand=scrollbary.set)
        
        scrollbarx.pack(side="bottom", fill="x")
        scrollbary.pack(side="right", fill="y")
        self.tree_consulta.pack(side="left", fill="both", expand=True)

        Button(frame, text="Volver", width=10, command=self.mostrar_vista_calculadora).pack(pady=10)

    def crear_vista_cambiar(self, frame):
        Label(frame, text="..:: Cambiar una Operación ::..", font=("Arial", 14)).pack(pady=20)
        
        frame_busqueda = Frame(frame)
        frame_busqueda.pack(pady=10)

        Label(frame_busqueda, text="Ingrese ID a modificar:").pack()
        self.id_cambiar_var = IntVar()
        self.id_cambiar_var.set(0) 
        Entry(frame_busqueda, textvariable=self.id_cambiar_var, justify="center").pack(pady=5)
        
        Button(frame_busqueda, text="Buscar ID", command=self.verificar_y_mostrar_formulario).pack(pady=5)

        self.frame_form_datos = Frame(frame)
        
        self.n1_cambiar_var = IntVar()
        self.n2_cambiar_var = IntVar()
        self.op_cambiar_var = StringVar()
        
        Label(self.frame_form_datos, text="Nuevo Número 1:").pack()
        Entry(self.frame_form_datos, textvariable=self.n1_cambiar_var, justify="center").pack(pady=2)

        Label(self.frame_form_datos, text="Nuevo Número 2:").pack()
        Entry(self.frame_form_datos, textvariable=self.n2_cambiar_var, justify="center").pack(pady=2)

        Label(self.frame_form_datos, text="Nuevo Operador (+, -, *, /):").pack()
        Entry(self.frame_form_datos, textvariable=self.op_cambiar_var, justify="center").pack(pady=2)

        Button(self.frame_form_datos, text="Guardar", width=15, command=lambda: funciones.Operaciones.actualizar_operacion_form(
            self.id_cambiar_var.get(),
            self.n1_cambiar_var.get(),
            self.n2_cambiar_var.get(),
            self.op_cambiar_var.get()
        )).pack(pady=15)
        
        Button(frame, text="Volver", width=15, command=self.mostrar_vista_calculadora).pack(side="bottom", pady=20)

    def verificar_y_mostrar_formulario(self):
        try:
            id_buscado = self.id_cambiar_var.get()
        except:
            messagebox.showerror("Error", "Por favor ingrese un número válido.")
            return
        datos = funciones.Operaciones.buscar_operacion(id_buscado)

        if datos:
            self.n1_cambiar_var.set(datos[2])
            self.n2_cambiar_var.set(datos[3])
            self.op_cambiar_var.set(datos[4])

            self.frame_form_datos.pack(pady=10)
        else:
            self.frame_form_datos.pack_forget()
            messagebox.showwarning("Atención", "El ID de la operación no existe.")