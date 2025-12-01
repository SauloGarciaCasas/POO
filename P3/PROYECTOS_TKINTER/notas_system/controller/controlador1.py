from model import usuario, nota

class Controlador:
    @staticmethod
    def registro(nombre, apellidos, email, password):
        try:
            resultado = usuario.Usuario.registrar(nombre, apellidos, email, password)
            return resultado
        except:
            return False

    @staticmethod
    def login(email, password):
        try:
            registro = usuario.Usuario.iniciar_sesion(email, password)
            if registro:
                return registro
            else:
                return None
        except:
            return None

    @staticmethod
    def crear_nota(usuario_id, titulo, descripcion):
        try:
            resultado = nota.Nota.crear(usuario_id, titulo, descripcion)
            return resultado
        except:
            return False

    @staticmethod
    def mostrar_notas(usuario_id):
        try:
            resultado = nota.Nota.mostrar(usuario_id)
            return resultado
        except:
            return []

    @staticmethod
    def actualizar_nota(id_nota, titulo, descripcion):
        try:
            resultado = nota.Nota.actualizar(id_nota, titulo, descripcion)
            return resultado
        except:
            return False

    @staticmethod
    def eliminar_nota(id_nota):
        try:
            resultado = nota.Nota.eliminar(id_nota)
            return resultado
        except:
            return False