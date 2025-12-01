from tkinter import *
from tkinter import messagebox
from controller import controlador1

id_user = None
nom_user = None
ape_user = None

class View:
    def __init__(self, ventana):
        self.ventana = ventana 
        ventana.title("Gestión de notas")
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
        lbl_titulo = Label(ventana, text=".:: Menú Principal ::.", justify="center", font=("Arial", 14, "bold"))
        lbl_titulo.pack(pady=20)

        btn_registro = Button(ventana, text="Registro", command=lambda:View.registro(ventana), width=15, height=2)
        btn_registro.pack(pady=10)

        btn_login = Button(ventana, text="Login", command=lambda: View.login(ventana), width=15, height=2)
        btn_login.pack(pady=10)

        btn_salir = Button(ventana, text="Salir", command=ventana.quit, width=15, height=2)
        btn_salir.pack(pady=10)

    @staticmethod
    def registro(ventana):
        View.borrarPantalla(ventana)
        lbl_titulore = Label(ventana, text=".:: Registro en el sistema ::.", justify="center", font=("Arial", 12, "bold"))
        lbl_titulore.pack(pady=10)

        Label(ventana, text="Nombre:").pack(pady=5)
        txt_nombre = Entry(ventana, width=30)
        txt_nombre.pack(pady=5)

        Label(ventana, text="Apellido:").pack(pady=5)
        txt_apellido = Entry(ventana, width=30)
        txt_apellido.pack(pady=5)

        Label(ventana, text="E-Mail:").pack(pady=5)
        txt_correo = Entry(ventana, width=30)
        txt_correo.pack(pady=5)

        Label(ventana, text="Contraseña:").pack(pady=5)
        txt_contraseña = Entry(ventana, width=30, show="*")
        txt_contraseña.pack(pady=5)

        def procesar_registro():
            if controlador1.Controlador.registro(txt_nombre.get(), txt_apellido.get(), txt_correo.get(), txt_contraseña.get()):
                messagebox.showinfo(icon='info', message="Acción realizada con éxito", title="Éxito")
                View.interfaz_principal(ventana)
            else:
                messagebox.showerror(icon='error', message="Error al registrar", title="Error")

        btn_registro = Button(ventana, text="Registrar", width=15, command=procesar_registro)
        btn_registro.pack(pady=15)
        btn_volver = Button(ventana, text="Volver", width=15, command=lambda:View.interfaz_principal(ventana))
        btn_volver.pack(pady=5)

    @staticmethod
    def login(ventana):
        View.borrarPantalla(ventana)
        lbl_titulogin = Label(ventana, text=".:: Inicio de sesión ::.", justify="center", font=("Arial", 12, "bold"))
        lbl_titulogin.pack(pady=10)

        Label(ventana, text="E-Mail:").pack(pady=5)
        txt_correo = Entry(ventana, width=30)
        txt_correo.pack(pady=5)

        Label(ventana, text="Contraseña:").pack(pady=5)
        txt_contraseña = Entry(ventana, width=30, show="*")
        txt_contraseña.pack(pady=5)

        def procesar_login():
            user = controlador1.Controlador.login(txt_correo.get(), txt_contraseña.get())
            if user:
                global id_user, nom_user, ape_user
                id_user = user[0]
                nom_user = user[1]
                ape_user = user[2]
                View.menu_notas(ventana)
            else:
                messagebox.showerror(icon='error', message="Datos incorrectos", title="Error")

        btn_entrar = Button(ventana, text="Entrar", width=15, command=procesar_login)
        btn_entrar.pack(pady=15)
        btn_volver = Button(ventana, text="Volver", width=15, command=lambda:View.interfaz_principal(ventana))
        btn_volver.pack(pady=5)

    @staticmethod
    def menu_notas(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo = Label(ventana, text=f"Bienvenido {nom_user} {ape_user}, has iniciado sesión", justify="center", font=("Arial", 12, "bold"))
        lbl_titulo.pack(pady=10)

        btn_crear = Button(ventana, text="Crear Nota", command=lambda:View.crear(ventana), width=15)
        btn_crear.pack(pady=5)

        btn_mostrar = Button(ventana, text="Ver Notas", command=lambda: View.mostrar(ventana), width=15)
        btn_mostrar.pack(pady=5)

        btn_cambiar = Button(ventana, text="Modificar Nota", command=lambda: View.cambiar(ventana), width=15)
        btn_cambiar.pack(pady=5)

        btn_eliminar = Button(ventana, text="Eliminar Nota", command=lambda: View.eliminar(ventana), width=15)
        btn_eliminar.pack(pady=5)

        btn_regresar = Button(ventana, text="Cerrar Sesión", command=lambda: View.interfaz_principal(ventana), width=15)
        btn_regresar.pack(pady=20)

    @staticmethod
    def crear(ventana):
        View.borrarPantalla(ventana)
        Label(ventana, text=".:: Crear Nota ::.", font=("Arial", 12, "bold")).pack(pady=10)

        Label(ventana, text="Título:").pack(pady=5)
        txt_titulo = Entry(ventana, width=30)
        txt_titulo.pack(pady=5)

        Label(ventana, text="Descripción:").pack(pady=5)
        txt_desc = Entry(ventana, width=30)
        txt_desc.pack(pady=5)

        def guardar():
            if controlador1.Controlador.crear_nota(id_user, txt_titulo.get(), txt_desc.get()):
                messagebox.showinfo("Éxito", "Acción realizada con éxito")
                View.menu_notas(ventana)
            else:
                messagebox.showerror("Error", "No se pudo guardar la nota")

        Button(ventana, text="Guardar", width=10, command=guardar).pack(pady=15)
        Button(ventana, text="Volver", width=10, command=lambda:View.menu_notas(ventana)).pack(pady=5)

    @staticmethod
    def mostrar(ventana):
        View.borrarPantalla(ventana)
        Label(ventana, text=f"{nom_user} {ape_user}, tus notas son:", font=("Arial", 12, "bold")).pack(pady=10)

        frame_notas = Frame(ventana)
        frame_notas.pack(fill=BOTH, expand=True, padx=20, pady=10)
        
        scrollbar = Scrollbar(frame_notas)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        lista_notas = Listbox(frame_notas, yscrollcommand=scrollbar.set, width=80, height=20)
        
        notas = controlador1.Controlador.mostrar_notas(id_user)
        if notas:
            for n in notas:
                lista_notas.insert(END, f"ID: {n[0]} | Fecha: {n[4]} | Título: {n[2]}")
                lista_notas.insert(END, f"   Desc: {n[3]}")
                lista_notas.insert(END, "-"*60)
        else:
            lista_notas.insert(END, "No tienes notas guardadas.")

        lista_notas.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=lista_notas.yview)

        Button(ventana, text="Volver", width=10, command=lambda:View.menu_notas(ventana)).pack(pady=10)

    @staticmethod
    def cambiar(ventana):
        View.borrarPantalla(ventana)
        Label(ventana, text=f"{nom_user} {ape_user}, vamos a modificar una nota", font=("Arial", 12, "bold")).pack(pady=10)

        Label(ventana, text="ID de la nota:").pack(pady=5)
        txt_id = Entry(ventana, width=30)
        txt_id.pack(pady=5)

        Label(ventana, text="Nuevo Título:").pack(pady=5)
        txt_titulo = Entry(ventana, width=30)
        txt_titulo.pack(pady=5)

        Label(ventana, text="Nueva Descripción:").pack(pady=5)
        txt_desc = Entry(ventana, width=30)
        txt_desc.pack(pady=5)

        def actualizar():
            if controlador1.Controlador.actualizar_nota(txt_id.get(), txt_titulo.get(), txt_desc.get()):
                messagebox.showinfo("Éxito", "Acción realizada con éxito")
                View.menu_notas(ventana)
            else:
                messagebox.showerror("Error", "No se pudo actualizar (Verifica el ID)")

        Button(ventana, text="Actualizar", width=10, command=actualizar).pack(pady=15)
        Button(ventana, text="Volver", width=10, command=lambda:View.menu_notas(ventana)).pack(pady=5)

    @staticmethod
    def eliminar(ventana):
        View.borrarPantalla(ventana)
        Label(ventana, text=f"{nom_user} {ape_user}, vamos a eliminar una nota", font=("Arial", 12, "bold")).pack(pady=10)

        Label(ventana, text="ID de la nota a eliminar:").pack(pady=5)
        txt_id = Entry(ventana, width=30)
        txt_id.pack(pady=5)

        def borrar():
            if controlador1.Controlador.eliminar_nota(txt_id.get()):
                messagebox.showinfo("Éxito", "Acción realizada con éxito")
                View.menu_notas(ventana)
            else:
                messagebox.showerror("Error", "No se pudo eliminar (Verifica el ID)")

        Button(ventana, text="Eliminar", width=10, command=borrar).pack(pady=15)
        Button(ventana, text="Volver", width=10, command=lambda:View.menu_notas(ventana)).pack(pady=5)