from estudiantes.estudiante import Estudiante
import os

class App:
    def __init__(self):
        self.main()

    def borrarPantalla(self):
        os.system("cls")

    def esperarTecla(self):
        input("\n \t \tOprima tecla para continuar... ")

    def datos_estudiante(self, tipo):
        self.borrarPantalla()
        print(f"\n\t ...Ingresa los siguientes datos del: '{tipo}' ...")
        nombre=input("Nombre: ").upper()
        nota=float(input("Nota: "))
        return nombre, nota

    def menu_acciones(self, tipo):
        print(f"\n\t\t.::  Menu de {tipo} ::.\n\t1.- Insertar \n\t2.- Consultar\n\t3.- Actualizar\n\t4.- Eliminar\n\t5.- Regresar ")
        opcion = input("\t\t Elige una opción: ").upper().strip()
        return opcion

    def respuesta_sql(self, respuesta):
        if respuesta:
            print("\n\t... ¡ Accion realizada con Éxito !...")
        else:
            print("\n\t... ¡ No fue posible realizar la acción, vuelva a intentar por favor ! ...") 

    def menu_estudiante(self):
        while True:
            self.borrarPantalla()
            opcion=self.menu_acciones("Estudiantes")
            if opcion == '1' or opcion=="INSERTAR":
                self.borrarPantalla()
                nombre, nota = self.datos_estudiante("Estudiante")
                respuesta = Estudiante.insertar(nombre, nota)
                self.respuesta_sql(respuesta) 
                self.esperarTecla()    
            elif opcion == '2' or opcion=="CONSULTAR":
                self.borrarPantalla()  
                registros = Estudiante.consultar()
                if len(registros) > 0:
                    num_estudiantes = 1
                    for fila in registros:
                        print(f"\nEstudiante #{num_estudiantes} con ID: {fila[0]} \nNombre: {fila[1]} \nNota: {fila[2]}") 
                        num_estudiantes += 1    
                    self.esperarTecla()
                else:
                    print(f"\n \t \t... ¡ No existen datos que mostrar, por el momento ! ...")
                    self.esperarTecla()            
            elif opcion == '3' or opcion=="ACTUALIZAR":
                self.borrarPantalla()
                print(f"\n \t .:: Actualizar Estudiante ::. \n")
                id = input("\nID del estudiante a actualizar: ")
                nombre, nota = self.datos_estudiante("Estudiante") 
                respuesta = Estudiante.actualizar(nombre, nota, id)
                self.respuesta_sql(respuesta)  
                self.esperarTecla()      
            elif opcion == '4' or opcion=="ELIMINAR":
                self.borrarPantalla()
                print(f"\n \t .:: Eliminar Estudiante ::. \n")
                id = input("\nID del estudiante a eliminar: ")
                respuesta = Estudiante.eliminar(id)
                self.respuesta_sql(respuesta)  
                self.esperarTecla()    
            elif opcion == '5' or opcion=="REGRESAR":
                break
            else:
                print("\n \t \t Opción no válida. Intenta de nuevo.")
                self.esperarTecla()

    def main(self):
        opcion=1
        while opcion!="2":
            self.borrarPantalla()
            opcion=input("\n\t\t ::: Menu Principal ::.\n\t1.- Ir al menú de Estudiantes\n\t2.- Salir\n\tElige un opción: ").lower().strip()
            match opcion:
                case "1":
                    self.menu_estudiante() 
                case "2":
                    self.borrarPantalla()
                    print("\n\t\t¡Gracias por utilizar el sistema!")
                    self.esperarTecla()    
                case _:
                    input("\nOpcion invalidad ... vuelva a intertarlo ... ") 
     
if __name__ == "__main__":
  app=App()