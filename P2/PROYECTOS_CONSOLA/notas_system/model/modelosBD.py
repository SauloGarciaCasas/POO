from conexionBD import conexion, cursor
import datetime
import hashlib

class UsuarioBD:
    
    @staticmethod
    def _hash_password(contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()

    @staticmethod
    def registrar(nombre, apellidos, email, contrasena):
        try:
            fecha = datetime.datetime.now()
            contrasena_hasheada = UsuarioBD._hash_password(contrasena)
            
            sql="INSERT INTO `usuarios` (nombre, apellidos, email, password, fecha) VALUES (%s, %s, %s, %s, %s)"
            val=(nombre, apellidos, email, contrasena_hasheada, fecha)
            
            cursor.execute(sql,val)
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def iniciar_sesion(email, contrasena):
        try:
            contrasena_hasheada = UsuarioBD._hash_password(contrasena)
            
            sql="SELECT * FROM usuarios WHERE email=%s AND password=%s"
            val=(email, contrasena_hasheada)
            
            cursor.execute(sql,val)
            registros = cursor.fetchone()
            
            if registros:
                return registros
            else:
                return None
        except:
            return False

class NotaBD:
    
    @staticmethod
    def crear(usuario_id, titulo, descripcion):
        try:
            sql="INSERT INTO notas (usuario_id, titulo, descripcion, fecha) VALUES (%s, %s, %s, NOW())"
            val=(usuario_id, titulo, descripcion)
            cursor.execute(sql,val)
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def mostrar(usuario_id):
        try:
            sql = "SELECT * FROM notas WHERE usuario_id=%s"
            val = (usuario_id,)
            cursor.execute(sql, val)
            return cursor.fetchall()
        except:
            return []
        
    @staticmethod
    def cambiar(id, titulo, descripcion):
        try:
            sql = "UPDATE notas SET titulo=%s, descripcion=%s, fecha=NOW() WHERE id=%s"
            cursor.execute(sql, (titulo, descripcion, id))
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def borrar(id):
        try:
            cursor.execute("DELETE FROM notas WHERE id=%s", (id,))
            conexion.commit()
            return True
        except:
            return False