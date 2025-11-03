import os
import getpass
from model import modelos, modelosBD

class App:
    def __init__(self):
        self.main()

    def borrarPantalla(self):
        os.system("cls")

    def esperarTecla(self):
        input("\n\t\t ... Oprima cualquier tecla para continuar ...")

    def respuesta_sql(self, respuesta):
        if respuesta:
            print("\n\t... ¡ Accion realizada con Éxito !...")
        else:
            print("\n\t... ¡ No fue posible realizar la acción, vuelva a intentar por favor ! ...") 

    def menu_usuarios(self):
       print("\n \t.:: Sistema de Gestión de Notas ::.. \n\t\t1.-  Registro  \n\t\t2.-  Login \n\t\t3.- Salir ")
       opcion=input("\t\t Elige una opción: ").upper().strip() 
       return opcion

    def menu_notas(self):
       print("\n \t .::  Menu Notas ::. \n\t1.- Crear \n\t2.- Mostrar \n\t3.- Cambiar \n\t4.- Eliminar \n\t5.- Salir ")
       opcion = input("\t\t Elige una opción: ").upper().strip()
       return opcion

    def handle_registro(self):
        self.borrarPantalla()
        print("\n \t ..:: Registro en el Sistema ::..")
        nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
        apellidos=input("\t ¿Cuales son tus apellidos?: ").upper().strip()
        email=input("\t Ingresa tu email: ").lower().strip()
        password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
        
        usuario = modelos.Usuario(nombre, apellidos, email, password)
        
        respuesta = modelosBD.UsuarioBD.registrar(
            usuario.nombre, usuario.apellidos, usuario.email, password 
        )
        
        if respuesta:
            print(f"\n\t{usuario.nombre} {usuario.apellidos} se registró correctamente con el email: {usuario.email}")
        else:
            print("\n\t ...Por favor inténtelo de nuevo, no fue posible registrar al usuario")
        self.esperarTecla()

    def handle_login(self):
        self.borrarPantalla()
        print("\n \t ..:: Inicio de Sesión ::.. ")     
        email=input("\t Ingresa tu E-mail: ").lower().strip()
        password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
        
        registro = modelosBD.UsuarioBD.iniciar_sesion(email, password)
        
        if registro:
            self.run_notas_menu(registro) 
        else:
            print(f"\n\t E-Mail y/o contraseña incorrectas, vuelve a intentarlo ...")
            self.esperarTecla()

    def run_notas_menu(self, usuario_logueado):
        usuario_id = usuario_logueado[0]
        nombre = usuario_logueado[1]
        apellidos = usuario_logueado[2]

        while True:
            self.borrarPantalla()
            print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
            opcion = self.menu_notas()

            if opcion == '1' or opcion=="CREAR":
                self.borrarPantalla()
                print(f"\n \t .:: Crear Nota ::. ")
                titulo=input("\tTitulo: ")
                descripcion=input("\tDescripción: ")
                
                nota = modelos.Nota(usuario_id, titulo, descripcion)
                respuesta = modelosBD.NotaBD.crear(nota.usuario_id, nota.titulo, nota.descripcion)
                self.respuesta_sql(respuesta)
                self.esperarTecla()    
                
            elif opcion == '2' or opcion=="MOSTRAR":
                self.borrarPantalla()
                lista_notas = modelosBD.NotaBD.mostrar(usuario_id)
                
                if len(lista_notas)>0:
                    print(f"\n\tMostrar las Notas")
                    print(f"{'ID':<10}{'Titulo':<15}{'Descripcion':<15}{'Fecha':<15}")
                    print(f"-"*80)
                    for fila in lista_notas:
                        print(f"{fila[0]:<10}{fila[2]:<15}{fila[3]:<15}{fila[4]}")
                    print(f"-"*80) 
                else:
                    print(f"\n \t No existen notas para mostrar") 
                self.esperarTecla()
                
            elif opcion == '3' or opcion == "CAMBIAR":
                self.borrarPantalla()
                print(f"\n \t .:: {nombre} {apellidos}, estas son tus notas actuales ::. \n")
                lista_notas = modelosBD.NotaBD.mostrar(usuario_id)
                
                if len(lista_notas) > 0:
                    print(f"{'ID':<10}{'Titulo':<15}{'Descripcion':<25}{'Fecha':<20}")
                    print("-" * 70)
                    for fila in lista_notas:
                        print(f"{fila[0]:<10}{fila[2]:<15}{fila[3]:<25}{fila[4]}")
                    print("-" * 70)
                    try:
                        id_nota = int(input("\n\tID de la nota a actualizar: ").strip())
                        titulo = input("\tNuevo título: ").strip()
                        descripcion = input("\tNueva descripción: ").strip()
                        
                        respuesta = modelosBD.NotaBD.cambiar(id_nota, titulo, descripcion)
                        self.respuesta_sql(respuesta)
                    except ValueError:
                        print("\nEl ID debe ser un número entero.")
                else:
                    print("\nNo hay notas registradas ...")
                self.esperarTecla()     
                
            elif opcion == '4' or opcion == "ELIMINAR":
                self.borrarPantalla()
                print(f"\n \t .:: {nombre} {apellidos}, estas son tus notas actuales ::. \n")
                lista_notas = modelosBD.NotaBD.mostrar(usuario_id)
                
                if len(lista_notas) > 0:
                    print(f"{'ID':<10}{'Titulo':<15}{'Descripcion':<25}{'Fecha':<20}")
                    print("-" * 70)
                    for fila in lista_notas:
                        print(f"{fila[0]:<10}{fila[2]:<15}{fila[3]:<25}{fila[4]}")
                    print("-" * 70)
                    try:
                        id_nota = int(input("\n\tID de la nota a eliminar: ").strip())
                        respuesta = modelosBD.NotaBD.borrar(id_nota)
                        self.respuesta_sql(respuesta)
                    except ValueError:
                        print("\nEl ID debe ser un número entero.")
                else:
                    print("\nNo hay notas registradas ...")
                self.esperarTecla()
                
            elif opcion == '5' or opcion=="SALIR":
                break
                
            else:
                print("\n \t \t Opción no válida. Intenta de nuevo.")
                self.esperarTecla()

    def main(self):
        opcion = True
        while opcion:
            self.borrarPantalla()
            opcion = self.menu_usuarios()

            if opcion == "1" or opcion == "REGISTRO":
                self.handle_registro()
            elif opcion == "2" or opcion == "LOGIN":
                self.handle_login()
            elif opcion == "3" or opcion == "SALIR":
                print("\n\t\t¡Gracias por utilizar el sistema!")
                self.esperarTecla()
                opcion = False
            else:
                input("\nOpcion invalidad ... vuelva a intertarlo ... ")

if __name__ == "__main__":
    app = App()